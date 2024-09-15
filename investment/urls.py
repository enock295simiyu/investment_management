from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InvestmentAccountViewSet, TransactionViewSet, AdminViewSet

router = DefaultRouter()
router.register(r'accounts', InvestmentAccountViewSet)
router.register(r'accounts/(?P<account_id>\d+)/transactions', TransactionViewSet)
router.register(r'admin', AdminViewSet, basename='admin')

urlpatterns = [
    path('', include(router.urls)),
]
