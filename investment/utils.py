from investment.models import InvestmentAccount

INVESTMENT_ACCOUNT_1 = 'INVESTMENT_ACCOUNT_1'

INVESTMENT_ACCOUNT_2 = 'INVESTMENT_ACCOUNT_2'

INVESTMENT_ACCOUNT_3 = 'INVESTMENT_ACCOUNT_3'

INVESTMENT_ACCOUNTS_MAPPING = {
    INVESTMENT_ACCOUNT_1: {
        'name': 'Investment Account 1',
        'descriptions': 'The user should only have view rights and should not be able to make transactions.'
    },
    INVESTMENT_ACCOUNT_2: {
        'name': 'Investment Account 2',
        'descriptions': 'The user should have full CRUD (Create, Read, Update, Delete) permissions.'
    },
    INVESTMENT_ACCOUNT_3: {
        'name': 'Investment Account 3',
        'descriptions': 'The user should only be able to post transactions, but not view them.'
    }
}


def create_update_investment_accounts(*args, **kwargs):
    """
    This method creates or updates user investment accounts.
    :return:
    """
    for account in INVESTMENT_ACCOUNTS_MAPPING:
        investment_account, _ = InvestmentAccount.objects.get_or_create(
            name=INVESTMENT_ACCOUNTS_MAPPING[account]['name'], )
        investment_account.description = INVESTMENT_ACCOUNTS_MAPPING[account]['descriptions']
        investment_account.save()
