from django.db import models
from core.models.wallet import Wallet
from core.models.address import Address


class Transaction(models.Model):
    wallet_id = models.IntegerField()
    address_id = models.IntegerField(db_index=True)
    transaction_hash = models.CharField(max_length=128)

    class Meta:
        models.UniqueConstraint(
            fields=["address_id", "transaction_hash"],
            name="unique_address_tx",
        )
