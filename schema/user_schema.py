from graphene_sqlalchemy import SQLAlchemyObjectType
from models import (User as UserModel)


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        exclude_fields = ('password')


def resolve_user(args, context, info):
    query = User.get_query(context)
    if args and 'id' in args:
        query = query.filter_by(id=args.get('id'))
    return query.one_or_none()
