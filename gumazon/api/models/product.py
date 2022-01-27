import sqlalchemy as db
from .dbadaptor import Base


class Product(Base):
    __tablename__ = 'product'

    id = db.Column(db.Integer, db.Sequence('user_id_seq'), primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    price = db.Column(db.Float(2))
    quantity = db.Column(db.Integer())

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__,
                               ', '.join(
                                   ['{}={}'.format(k, self.__dict__[k]) for k in self.__dict__.keys() if k[0] != '_']))
