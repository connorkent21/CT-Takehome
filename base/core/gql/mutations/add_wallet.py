import graphene
from core.interactors.add_wallet import AddWallet as AddWalletInteractor, AddWalletInput
from core.gql.types import WalletNode
from core.gql.helpers import parse_global_relay_id


class AddWallet(graphene.ClientIDMutation):
    class Input:
        name = graphene.NonNull(graphene.String)
        user_id = graphene.NonNull(graphene.ID)
        # Normally this would be the authenticated user from context but
        # for the purposes of this project we will accept a specified user id

    wallet = graphene.Field(WalletNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, user_id, name):
        wallet = AddWalletInteractor(
            AddWalletInput(
                user_id=parse_global_relay_id(user_id),
                name=name,
            )
        )
        return AddWallet(wallet=wallet)
