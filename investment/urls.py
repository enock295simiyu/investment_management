from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import InvestmentAccountViewSet, TransactionViewSet, AdminViewSet

app_name = 'investment'
router = DefaultRouter(use_regex_path=False)
router.register('accounts', InvestmentAccountViewSet, basename='account')
router.register('accounts/<uuid:account_id>/transactions', TransactionViewSet, basename='transactions')
router.register('admin', AdminViewSet, basename='admin')

urlpatterns = [
    path('', include(router.urls)),
]
