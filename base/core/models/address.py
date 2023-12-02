from django.db import models


class Address(models.Model):
    wallet_id = models.IntegerField(db_index=True)
    address_string = models.CharField(max_length=128)

    class Meta:
        models.UniqueConstraint(
            fields=["address_string", "wallet_id"],
            name="unique_address_wallet",
        )
