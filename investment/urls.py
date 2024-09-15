from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import InvestmentAccountViewSet, TransactionViewSet, AdminViewSet

router = DefaultRouter(use_regex_path=False)
router.register('accounts', InvestmentAccountViewSet)
router.register('accounts/<uuid:account_id>/transactions', TransactionViewSet)
router.register(r'admin', AdminViewSet, basename='admin')

urlpatterns = [
    path('', include(router.urls)),
]
