from dataclasses import dataclass
from core.models import Wallet
from django.core.exceptions import ValidationError


@dataclass
class AddWalletInput:
    name: str
    user_id: int


def AddWallet(input: AddWalletInput):
    # Check existing
    if Wallet.objects.filter(name=input.name, user_id=input.user_id).exists():
        raise ValidationError("Wallet with this name already exists for user")

    wallet = Wallet.objects.create(name=input.name, user_id=input.user_id)

    return wallet
