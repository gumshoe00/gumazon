import sqlalchemy as db
from .dbadaptor import Base


class User(Base):
    __tablename__ = 'user'

    id = db.Column(db.Integer, db.Sequence('user_id_seq'), primary_key=True)
    username = db.Column(db.String(50), unique=True)
    group = db.Column(db.String(50))
    uix = db.UniqueConstraint('group', 'username')
    dateCreated = db.Column(db.TIMESTAMP, nullable=False, server_default=db.text("CURRENT_TIMESTAMP"))

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__,
                               ', '.join(
                                   ['{}={}'.format(k, self.__dict__[k]) for k in self.__dict__.keys() if k[0] != '_']))


