import graphene
from graphene import relay
from graphene_django import DjangoConnectionField

from core.gql.types import AddressNode, TransactionNode, WalletNode, UserNode
from core.models import Example
from core.gql.mutations import AddWallet, AddAddress, RemoveAddress, SyncTransactions


class Query(graphene.ObjectType):
    address = relay.Node.Field(AddressNode)
    addresses = DjangoConnectionField(AddressNode)
    transaction = relay.Node.Field(TransactionNode)
    transactions = DjangoConnectionField(TransactionNode)
    wallet = relay.Node.Field(WalletNode)
    wallets = DjangoConnectionField(WalletNode)
    user = relay.Node.Field(UserNode)
    users = DjangoConnectionField(UserNode)


class Mutation(graphene.ObjectType):
    add_wallet = AddWallet.Field()
    add_address = AddAddress.Field()
    remove_address = RemoveAddress.Field()
    sync_transactions = SyncTransactions.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
