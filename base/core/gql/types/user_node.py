from graphene import relay, Connection
from graphene_django import DjangoObjectType
from core.models import User


class UserNode(DjangoObjectType):
    class Meta:
        model = User
        interfaces = (relay.Node,)
        connection_class = Connection
        filter_fields = {
            "id": ["exact"],
        }
