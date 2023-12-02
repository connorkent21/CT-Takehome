import factory
from core.models import Address, Wallet, Transaction, User


class AddressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Address


class WalletFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("name")

    class Meta:
        model = Wallet


class UserFactory(factory.django.DjangoModelFactory):
    first_name = factory.Faker("name")
    last_name = factory.Faker("name")

    class Meta:
        model = User


class TransactionFactory(factory.django.DjangoModelFactory):
    wallet_id = factory.Sequence(lambda n: n)
    transaction_hash = factory.Faker("name")

    class Meta:
        model = Transaction
