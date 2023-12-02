from django.db import models


class Wallet(models.Model):
    name = models.CharField(max_length=64)
    user_id = models.IntegerField(db_index=True)

    class Meta:
        models.UniqueConstraint(
            fields=["name", "user_id"],
            name="unique_wallet_name",
        )
