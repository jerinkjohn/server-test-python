import graphene
from .user_schema import (resolve_user as resolve_user_from_user_schema)
from .user_schema import User
from .role_schema import (resolve_roles as resolve_roles_from_role_schema)
from .role_schema import Role


class Query(graphene.ObjectType):
    roles = graphene.List(Role, description="All known roles", id=graphene.String())
    user = graphene.Field(User, id=graphene.String())

    def resolve_roles(self, args, context, info):
        return resolve_roles_from_role_schema(args, context, info)

    def resolve_user(self, args, context, info):
        return resolve_user_from_user_schema(args, context, info)


schema = graphene.Schema(query=Query, types=(Role, User))
