import graphene
from core.interactors import (
    RemoveAddress as RemoveAddressInteractor,
    RemoveAddressInput,
)
from core.gql.helpers import parse_global_relay_id


class RemoveAddress(graphene.ClientIDMutation):
    class Input:
        address_id = graphene.NonNull(graphene.ID)

    ok = graphene.NonNull(graphene.Boolean)

    @classmethod
    def mutate_and_get_payload(cls, root, info, address_id):
        RemoveAddressInteractor(
            RemoveAddressInput(address_id=parse_global_relay_id(address_id))
        )
        return RemoveAddress(ok=True)
