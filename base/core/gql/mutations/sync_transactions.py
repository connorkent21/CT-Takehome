import graphene
from core.interactors import (
    SyncTransactions as SyncTransactionsInteractor,
    SyncTransactionsInput,
)
from core.gql.helpers import parse_global_relay_id


class SyncTransactions(graphene.ClientIDMutation):
    class Input:
        wallet_id = graphene.NonNull(graphene.ID)

    ok = graphene.NonNull(graphene.Boolean)

    @classmethod
    def mutate_and_get_payload(cls, root, info, wallet_id):
        SyncTransactionsInteractor(
            SyncTransactionsInput(wallet_id=parse_global_relay_id(wallet_id))
        )
        return SyncTransactions(ok=True)
