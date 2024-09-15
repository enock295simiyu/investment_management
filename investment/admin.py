from django.contrib import admin

from investment.models import InvestmentAccount, InvestmentAccountUser, Transaction


# Register your models here.
class InvestmentAccountAdmin(admin.ModelAdmin):
    search_fields = (
        'id', 'name'
    )
    list_filter = ('created', 'modified')
    list_display = (
        'id', 'name', 'created', 'modified', 'created_by',
        'modified_by',
    )
    list_display_links = list_display
    raw_id_fields = ('users',)


class InvestmentAccountUserAdmin(admin.ModelAdmin):
    search_fields = (
        'id', 'name'
    )
    list_filter = ('created', 'modified')
    list_display = (
        'id', 'investment_account', 'created', 'modified', 'created_by',
        'modified_by',
    )
    list_display_links = list_display
    raw_id_fields = ('investment_account',)


class TransactionAdmin(admin.ModelAdmin):
    search_fields = (
        'id', 'name'
    )
    list_filter = ('created', 'modified')
    list_display = (
        'id', 'account', 'amount', 'user', 'created', 'modified', 'created_by',
        'modified_by',
    )
    list_display_links = list_display
    raw_id_fields = ('account', 'user')


admin.site.register(InvestmentAccount, InvestmentAccountAdmin)
admin.site.register(InvestmentAccountUser, InvestmentAccountUserAdmin)
admin.site.register(Transaction, TransactionAdmin)
