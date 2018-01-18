from .database import db_session
from models import (Role as RoleModel)


class Role:
    def init_table(self):
        claim_adjuster = db_session.query(RoleModel).filter((RoleModel.name == 'Claim Adjuster')).one_or_none()
        if claim_adjuster is None:
            claim_adjuster = RoleModel(name='Claim Adjuster')
            db_session.add(claim_adjuster)

        supervisor = db_session.query(RoleModel).filter((RoleModel.name == 'Supervisor')).one_or_none()
        if supervisor is None:
            supervisor = RoleModel(name='Supervisor')
            db_session.add(supervisor)
        db_session.commit()
