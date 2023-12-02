import graphene
from graphene import relay, Connection
from graphene_django import DjangoObjectType
from core.models import Address, Transaction
from core.gql.types.transaction_node import TransactionNode
from blockcypher import get_address_overview


class AddressNode(DjangoObjectType):
    balance = graphene.NonNull(graphene.Int)
    transactions = graphene.List(graphene.NonNull(TransactionNode))
    address_string = graphene.NonNull(graphene.String)

    class Meta:
        model = Address
        interfaces = (relay.Node,)
        connection_class = Connection
        filter_fields = {
            "id": ["exact"],
            "wallet_id": ["exact"],
        }

    def resolve_transactions(parent, _info):
        # Should be using dataloaders to prevent N+1. Bypassing for time constraint
        return Transaction.objects.filter(address_id=parent.id)

    def resolve_balance(parent, _info):
        address_details = get_address_overview(parent.address_string)
        if not address_details:
            return 0
        return address_details["balance"]
