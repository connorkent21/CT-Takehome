from django.test import TestCase
from core.tests.factories import UserFactory, WalletFactory, AddressFactory
from core.interactors import SyncTransactions, SyncTransactionsInput
from core.models import Address, Transaction


class TestSyncTransactions(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.wallet = WalletFactory(user_id=self.user.id)
        self.address_1 = AddressFactory(
            wallet_id=self.wallet.id,
            address_string="3E8ociqZa9mZUSwGdSmAEMAoAxBK3FNDcd",
        )  # Small address
        self.address_2 = AddressFactory(
            wallet_id=self.wallet.id,
            address_string="bc1q0sg9rdst255gtldsmcf8rk0764avqy2h2ksqs5",
        )  # Small address
        # self.address_3 = AddressFactory(
        #     wallet_id=self.wallet.id,
        #     address_string="12xQ9k5ousS8MqNsMBqHKtjAtCuKezm2Ju",
        # )  # Large address
        # self.address_4 = AddressFactory(
        #     wallet_id=self.wallet.id,
        #     address_string="bc1qm34lsc65zpw79lxes69zkqmk6ee3ewf0j77s3h",
        # )  # Largest address

    def test_It_SynchronizesTransactionsForAllAddressInWallet(self):
        input = SyncTransactionsInput(wallet_id=self.wallet.id)
        SyncTransactions(input)
        transactions = Transaction.objects.all()

        self.assertIsNotNone(transactions)
