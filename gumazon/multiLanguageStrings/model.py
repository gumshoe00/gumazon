import sqlalchemy as sa

from gumazon.bootstrap.db_base import Base


class MultiLanguageStrings(Base):

    id = sa.Column(sa.Integer, sa.Sequence('multiLanguageString_id_seq'), primary_key=True)
    username = sa.Column(sa.String(50), unique=True)
    group = sa.Column(sa.String(50))
    uix = sa.UniqueConstraint('group', 'username')
    dateCreated = sa.Column(sa.TIMESTAMP, nullable=False, server_default=sa.text("CURRENT_TIMESTAMP"))

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__,
                               ', '.join(
                                   ['{}={}'.format(k, self.__dict__[k]) for k in self.__dict__.keys() if k[0] != '_']))


if __name__ == '__main__':
    print('working')
