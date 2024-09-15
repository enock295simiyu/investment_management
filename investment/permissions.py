from rest_framework.permissions import BasePermission

from investment.models import InvestmentAccountUser


class IsTransactionAllowed(BasePermission):
    def has_permission(self, request, view):
        account_user = InvestmentAccountUser.objects.get(user=request.user,
                                                         investment_account=view.kwargs['account_id'])

        if view.action in ['create', 'update',
                           'delete'] and account_user.permission != InvestmentAccountUser.FULL_ACCESS:
            return False
        elif view.action == 'create' and account_user.permission == InvestmentAccountUser.VIEW_ONLY:
            return False
        elif view.action == 'list' and account_user.permission == InvestmentAccountUser.POST_ONLY:
            return False
        return True
