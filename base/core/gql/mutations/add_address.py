import graphene
from core.interactors import AddAddress as AddAddressInteractor, AddAddressInput
from core.gql.types import AddressNode
from core.gql.helpers import parse_global_relay_id


class AddAddress(graphene.ClientIDMutation):
    class Input:
        wallet_id = graphene.NonNull(graphene.ID)
        address_string = graphene.NonNull(graphene.String)

    address = graphene.Field(AddressNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, wallet_id, address_string):
        new_address = AddAddressInteractor(
            AddAddressInput(
                wallet_id=parse_global_relay_id(wallet_id),
                address_string=address_string,
            )
        )
        return AddAddress(address=new_address)
