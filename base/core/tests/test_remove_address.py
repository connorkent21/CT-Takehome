from django.test import TestCase
from core.tests.factories import (
    UserFactory,
    WalletFactory,
    AddressFactory,
    TransactionFactory,
)
from core.interactors import RemoveAddress, RemoveAddressInput
from core.models import Transaction, Address


class TestRemoveAddress(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.wallet = WalletFactory(user_id=self.user.id)
        self.address = AddressFactory(
            wallet_id=self.wallet.id,
            address_string="abc",
        )
        TransactionFactory(address_id=self.address.id)
        TransactionFactory(address_id=self.address.id)
        TransactionFactory(address_id=self.address.id)

    def test_When_AddressExists_It_RemovesAddressAndRemovesTransactions(self):
        input = RemoveAddressInput(address_id=self.address.id)
        RemoveAddress(input)
        transactions = Transaction.objects.filter(address_id=self.address.id)
        address = Address.objects.filter(wallet_id=self.wallet.id)
        self.assertEqual(address.count(), 0)
        self.assertEqual(transactions.count(), 0)
