from graphene import relay, Connection
from graphene_django import DjangoObjectType
from core.models import Wallet


class WalletNode(DjangoObjectType):
    class Meta:
        model = Wallet
        interfaces = (relay.Node,)
        connection_class = Connection
        filter_fields = {
            "id": ["exact"],
        }
