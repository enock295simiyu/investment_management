from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from .models import InvestmentAccount, InvestmentAccountUser, Transaction


class InvestmentAccountTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user1 = User.objects.create_user(username='user1', password='pass')
        self.user2 = User.objects.create_user(username='user2', password='pass')

        self.account1 = InvestmentAccount.objects.create(name='Account 1', description='View only')
        self.account2 = InvestmentAccount.objects.create(name='Account 2', description='Full access')

        InvestmentAccountUser.objects.create(user=self.user1, investment_account=self.account1,
                                             permission=InvestmentAccountUser.VIEW_ONLY)
        InvestmentAccountUser.objects.create(user=self.user1, investment_account=self.account2,
                                             permission=InvestmentAccountUser.FULL_ACCESS)

    def test_view_only_permission(self):
        self.client.login(username='user1', password='pass')
        response = self.client.get(reverse('investment:account-detail', kwargs={'pk': self.account1.pk}))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('investment:transactions-list', kwargs={'account_id': self.account1.pk}),
                                    {'amount': 100})

        self.assertEqual(response.status_code, 403)  # View only, can't post transactions

    def test_full_access_permission(self):
        self.client.login(username='user1', password='pass')
        response = self.client.post(reverse('investment:transactions-list', kwargs={'account_id': self.account2.pk}),
                                    {'amount': 100})
        self.assertEqual(response.status_code, 201)  # Full access, can post transactions

    def test_account_list_get(self):
        url = reverse('investment:account-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_account_create_post(self):
        url = reverse('investment:account-list')
        response = self.client.post(url, data={'name': 'test Account', 'description': 'test description'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_account_retrieve_get(self):
        url = reverse('investment:account-detail', kwargs={'pk': self.account1.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_account_update_put(self):
        url = reverse('investment:account-detail', kwargs={'pk': self.account1.pk})
        response = self.client.put(url,
                                   data={'name': 'updated test Account', 'description': 'updated test description'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_account_partial_update_patch(self):
        url = reverse('investment:account-detail', kwargs={'pk': self.account1.pk})
        response = self.client.patch(url,
                                     data={'name': 'updated test Account', 'description': 'updated test description'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_account_destroy_delete(self):
        url = reverse('investment:account-detail', kwargs={'pk': self.account1.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class AdminViewSetTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin = User.objects.create_user(username='user1', password='pass', is_superuser=True, is_staff=True)
        self.client.login(username=self.admin.username, password='pass')
        self.account1 = InvestmentAccount.objects.create(name='Account 1', description='Test account description')
        self.account2 = InvestmentAccount.objects.create(name='Account 2', description='Test account description')
        self.transaction1 = Transaction.objects.create(account=self.account1, user=self.admin, amount=30)
        self.transaction2 = Transaction.objects.create(account=self.account1, user=self.admin, amount=30)

    def test_admin_list_get(self):
        url = reverse('investment:admin-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_admin_transactions_summary_get(self):
        url = reverse('investment:admin-transactions-summary')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_admin_retrieve_get(self):
        url = reverse('investment:admin-detail', kwargs={'pk': self.transaction2.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_admin_update_put(self):
        url = reverse('investment:admin-detail', kwargs={'pk': self.transaction2.pk})
        response = self.client.put(url, data={'amount': 399})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_admin_partial_update_patch(self):
        url = reverse('investment:admin-detail', kwargs={'pk': self.transaction2.pk})
        response = self.client.patch(url, data={'amount': 499})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
