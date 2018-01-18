from graphene_sqlalchemy import SQLAlchemyObjectType
from models import (Role as RoleModel)


class Role(SQLAlchemyObjectType):
    class Meta:
        model = RoleModel


def resolve_roles(args, context, info):
    query = Role.get_query(context)
    if args and 'id' in args:
        query = query.filter_by(id=args.get('id'))
    return query.all()
