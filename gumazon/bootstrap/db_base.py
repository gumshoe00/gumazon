import sqlalchemy.ext.declarative as dec


class Base:
    @dec.declared_attr
    def __tablename__(cls):
        return cls.__name__[0].lower()+''.join(cls.__name__[1:])

    __table_args__ = {}


# A base class belongs to one database.
# If our application talks to multiple databases, we need multiple base classes.
Base = dec.declarative_base(cls=Base)
