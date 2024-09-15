from django_filters import rest_framework as filters

from investment.models import Transaction


class TransactionFilter(filters.FilterSet):
    class Meta:
        model = Transaction
        fields = {
            'account': ['exact', ],
            'user__email': ['exact', 'icontains', 'in'],
            'user__username': ['exact', 'icontains', 'in'],
            'amount': ['exact', 'lt', 'gt'],
            'created': ['exact', 'lt', 'gt'],
        }
