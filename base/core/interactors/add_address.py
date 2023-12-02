from dataclasses import dataclass
from core.models import Address


@dataclass
class AddAddressInput:
    wallet_id: int
    address_string: str


def AddAddress(input: AddAddressInput):
    address = Address.objects.create(
        wallet_id=input.wallet_id,
        address_string=input.address_string,
    )

    return address
