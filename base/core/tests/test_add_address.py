from django.test import TestCase
from core.tests.factories import UserFactory, WalletFactory
from core.interactors import AddAddress, AddAddressInput
from core.models import Address


class TestAddAddress(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.wallet = WalletFactory(user_id=self.user.id)

    def test_It_AddsAnAddress(self):
        input = AddAddressInput(wallet_id=self.wallet.id, address_string="abc")
        AddAddress(input)

        address = Address.objects.filter(wallet_id=self.wallet.id).first()
        self.assertIsNotNone(address)
        self.assertEqual(address.address_string, "abc")
