from dataclasses import dataclass
from core.models import Address, Transaction
from django.core.exceptions import ValidationError


@dataclass
class RemoveAddressInput:
    address_id: int


def RemoveAddress(input: RemoveAddressInput):
    address = Address.objects.filter(id=input.address_id).first()
    if not address:
        raise ValidationError("Could not find address")

    # Delete all associated transactions
    Transaction.objects.filter(address_id=address.id).delete()

    # Delete Address
    address.delete()
