from rest_framework import serializers

from .models import InvestmentAccount, InvestmentAccountUser, Transaction


class InvestmentAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestmentAccount
        fields = ['id', 'name', 'description']


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'amount', 'created']

    def create(self, validated_data):
        account_id = self.context['view'].kwargs.get('account_id')
        validated_data['account_id'] = account_id
        validated_data['user'] = self.context['view'].request.user
        transaction = Transaction.objects.create(**validated_data)
        return transaction


class InvestmentAccountUserSerializer(serializers.ModelSerializer):
    account = InvestmentAccountSerializer()
    permission = serializers.ChoiceField(choices=InvestmentAccountUser.PERMISSION_CHOICES)

    class Meta:
        model = InvestmentAccountUser
        fields = ['user', 'account', 'permission']
