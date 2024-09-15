# Create your views here.
from django.db.models import Sum
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from .models import InvestmentAccount, Transaction
from .permissions import IsTransactionAllowed
from .serializers import InvestmentAccountSerializer, TransactionSerializer


class InvestmentAccountViewSet(viewsets.ModelViewSet):
    queryset = InvestmentAccount.objects.all()
    serializer_class = InvestmentAccountSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [IsTransactionAllowed]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['created']
    queryset = Transaction.objects.all()

    def get_queryset(self):
        return Transaction.objects.filter(account_id=self.kwargs['account_id'])


class AdminViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated, IsAdminUser]

    @action(detail=False, methods=['get'], url_path='transactions-summary')
    def transactions_summary(self, request):
        user_id = request.query_params.get('user_id')
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        transactions = Transaction.objects.filter(user_id=user_id)
        if start_date and end_date:
            transactions = transactions.filter(created_at__range=[start_date, end_date])

        total_balance = transactions.aggregate(Sum('amount'))['amount__sum'] or 0
        transaction_data = TransactionSerializer(transactions, many=True).data

        return Response({
            'transactions': transaction_data,
            'total_balance': total_balance,
        })
