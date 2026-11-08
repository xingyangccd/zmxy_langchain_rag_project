from tests.base_model import User
from tests.sqlalchemy_config import SessionFactory

with SessionFactory() as  session:
    session.get(User,1)
    print(User)
    session.query(User.username).filter(User.username=="admin").all()



