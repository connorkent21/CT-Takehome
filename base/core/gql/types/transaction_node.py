from graphene import relay, Connection
from graphene_django import DjangoObjectType
from core.models import Transaction


class TransactionNode(DjangoObjectType):
    class Meta:
        model = Transaction
        only_fields = ["transaction_hash"]
        interfaces = (relay.Node,)
        connection_class = Connection
        filter_fields = {
            "id": ["exact"],
            "address_id": ["exact"],
            "wallet_id": ["exact"],
        }
