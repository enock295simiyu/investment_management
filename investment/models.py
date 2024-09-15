from django.db import models

# Create your models here.
from django.contrib.auth.models import User, Permission
from django.db import models
from django.utils import timezone

from investment.base import BaseModel


class InvestmentAccount(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    users = models.ManyToManyField(User, through='InvestmentAccountUser', related_name='investment_accounts')


class InvestmentAccountUser(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    investment_account = models.ForeignKey(InvestmentAccount, on_delete=models.CASCADE)

    VIEW_ONLY = 'view'
    FULL_ACCESS = 'full'
    POST_ONLY = 'post'

    PERMISSION_CHOICES = [
        (VIEW_ONLY, 'View only'),
        (FULL_ACCESS, 'Full access'),
        (POST_ONLY, 'Post transactions only'),
    ]

    permission = models.CharField(max_length=10, choices=PERMISSION_CHOICES, default=VIEW_ONLY)

    class Meta:
        unique_together = ('user', 'investment_account')


class Transaction(BaseModel):
    account = models.ForeignKey(InvestmentAccount, on_delete=models.CASCADE, related_name='transactions')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
