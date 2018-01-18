#!/usr/bin/env python
import argparse
from database import User
from database import Role
from database import Base, engine


def run(drop=False, fake_data=False):
    if drop:
        print('Dropping all tables...')
        Base.metadata.drop_all(bind=engine)

    Base.metadata.create_all(bind=engine, checkfirst=True)
    user = User()
    role = Role()
    role.init_table()
    user.init_table(fake_data=fake_data)


parser = argparse.ArgumentParser(description="""
Initialize/update the database with data from the people.json file.
You likely want to run this on the heroku instance via:
"heroku run -- './%(prog)s'"
""")
parser.add_argument('-D', '--drop', dest='drop', action='store_true',
                    help='drop all tables first (reinitialize)')

# Ironically, this argument defaults to True, and there's no mechanism to make it false.
# That mechanism will be added later when we have a different data starting point.
parser.add_argument('-P', '--populate-fake', dest='fake_data', action='store_true', default=True,
                    help='populate the database with fake data')

if __name__ == '__main__':
    args = parser.parse_args()
    run(drop=args.drop, fake_data=args.fake_data)
