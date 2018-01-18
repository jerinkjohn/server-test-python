from .database import db_session
from models import (User as UserModel)
from models import Role


class User:
    def check_user_exist(self, email):
        return db_session.query(UserModel.user_id).filter_by(email=email).count() > 0

# Authorization stuff

    def authenticate(self, email, password):
        user = db_session.query(UserModel).filter((UserModel.email == email)).one_or_none()

        if user and user.password == password:
            return user
        return None

    def identity(self, payload):
        email = payload['identity']
        return db_session.query(UserModel).filter(UserModel.email == email).one_or_none()

    def init_table(self, fake_data=False):
        if fake_data:
            print('Inserting seed Data...')

            tracy = db_session.query(UserModel).filter((UserModel.email == 'tracy.tim@cognizant.com')).one_or_none()
            if tracy is None:
                tracy = UserModel(
                                first_name='Tracy',
                                last_name='Tim',
                                email='tracy.tim@cognizant.com',
                                password='password'
                                )

                db_session.add(tracy)

            claim_adjuster = db_session.query(Role).filter((Role.name == 'Claim Adjuster')).one_or_none()
            if claim_adjuster:
                tracy.role = claim_adjuster

            db_session.commit()

            print('Completed inserting seed data.')
