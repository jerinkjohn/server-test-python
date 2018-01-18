#!/usr/bin/env python

import os
from datetime import timedelta, datetime
from flask import Flask
from flask_cors import CORS
from flask_graphql import GraphQLView
from flask_jwt import JWT, jwt_required, current_identity
from database import User
from flask_migrate import Migrate
from database.database import Base, db_session
from config import Config
from schema import schema

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'super-secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
    app.config['DEBUG'] = os.environ.get('DEBUG', 'True').upper() == 'TRUE'
    app.config['JWT_AUTH_USERNAME_KEY'] = 'email'
    app.config['JWT_EXPIRATION_DELTA'] = timedelta(7 * 24 * 60 * 60)
    app.config['JWT_AUTH_URL_RULE'] = '/auth'
    app.config['JWT_USER_IDENTITY_FIELD'] = 'email'


    migrate = Migrate(app, Base)

    CORS(app)

    user = User()
    jwt = JWT(app, user.authenticate, user.identity)


    @jwt.jwt_payload_handler
    def jwt_payload_handler(user):
        iat = datetime.utcnow()
        exp = iat + app.config.get('JWT_EXPIRATION_DELTA')
        nbf = iat + app.config.get('JWT_NOT_BEFORE_DELTA')
        user_identity_field = app.config.get('JWT_USER_IDENTITY_FIELD', 'id')
        email = getattr(user, user_identity_field) or user[user_identity_field]
        return {'exp': exp, 'iat': iat, 'nbf': nbf, 'identity': email}


    # This is a sample route.
    @app.route('/protected')
    @jwt_required()
    def protected():
        return '%s' % current_identity.first_name


    @app.route('/')
    def welcome():
        return """Welcome to the LauchPad 2 Team K project"""


    # Useful for having the GraphiQL interface.
    app.add_url_rule('/graphql', view_func=jwt_required()(GraphQLView.as_view('graphql',
                                                                              schema=schema,
                                                                              graphiql=True,
                                                                              context={'session': db_session})))


    # Dev graphQL endpoints which will NOT require JWT tokens.
    if app.config.get('DEBUG', False):
        app.add_url_rule('/graphql-debug', view_func=GraphQLView.as_view('graphql-debug',
                                                                        schema=schema,
                                                                        graphiql=True,
                                                                        context={'session': db_session}))


    # TODO: Do we need this since we have the CORS(app) above?
    CORS(app, resources={'/graphql': {'origins': '*'}})


    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()
    return app

app = create_app()

if __name__ == '__main__':
    app.run()
