from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from .models import InvestmentAccount, InvestmentAccountUser


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
