from django.test import TestCase
from core.tests.factories import UserFactory, WalletFactory
from core.interactors import AddWallet, AddWalletInput
from core.models import Address, Wallet
from django.core.exceptions import ValidationError


class TestAddWallet(TestCase):
    def setUp(self):
        self.user = UserFactory()

    def test_It_AddsWallet(self):
        input = AddWalletInput(user_id=self.user.id, name="Test Wallet")
        AddWallet(input)

        wallet = Wallet.objects.filter(user_id=self.user.id).first()
        self.assertIsNotNone(wallet)
        self.assertEqual(wallet.name, "Test Wallet")

    def test_When_WalletWithNameExists_It_RaisesValidationError(self):
        WalletFactory(user_id=self.user.id, name="Test Wallet")
        input = AddWalletInput(user_id=self.user.id, name="Test Wallet")
        with self.assertRaises(ValidationError):
            AddWallet(input)
