from pathlib import Path
from sqlite3 import IntegrityError, ProgrammingError

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .err import ItemNotStored, ItemAlreadyStored

Base = declarative_base()


def db_engine(dbname=':memory:'):
    return create_engine('sqlite:///{}'.format(dbname), echo=True)


def db_session(dbname=':memory:'):
    engine = db_engine(dbname)
    Base.metadata.create_all(bind=engine)
    return sessionmaker(bind=engine)


DB_NAME = '{}.sqlite'.format(Path.cwd().name)


def connect(func):
    """Decorator to (re)open a sqlite database connection when needed.

    A database connection must be open when we want to perform a database query
    but we are in one of the following situations:
    1) there is no connection
    2) the connection is closed

    Parameters
    ----------
    func : function
        function which performs the database query

    Returns
    -------
    inner func : function
    """

    def inner_func(conn, *args, **kwargs):
        try:
            print(conn.info)
        except (AttributeError, ProgrammingError):
            conn = db_session(DB_NAME)
        return func(conn, *args, **kwargs)

    return inner_func


def disconnect(dbname=None, conn=None):
    if dbname is not DB_NAME:
        print("You are trying to disconnect from a wrong DB")
    if conn is not None:
        conn.close()


@connect
def save(conn, data_type, key, value, **kwargs):
    _kws = {key: value}
    _kws.update(**kwargs.copy())

    new_instance = data_type(**_kws)
    try:
        conn.add(new_instance)
    except Exception as e:
        raise ItemAlreadyStored(
            '{}: "{}" already stored in table "{}"'.format(e, value, data_type))
    else:
        conn.commit()


@connect
def show(conn, data_type, key, value):
    result = conn.query(data_type).filter_by(**{key: value}).first()

    if result is not None:
        return result
    else:
        raise ItemNotStored(
            'Can\'t read "{}" because it\'s not stored in table "{}"'
                .format(value, data_type))


@connect
def index(conn, data_type):
    _output = []
    try:
        result = conn.query(data_type).all()
    except Exception as e:
        print(e)
    else:
        _output.extend([r for r in result])
    return _output


@connect
def update(conn, data_type, key, value, **kwargs):
    _kws = {key: value}
    _kws.update(**kwargs.copy())
    pass
    # data_type = scrub(data_type)
    # sql_check = 'SELECT EXISTS(SELECT 1 FROM {} WHERE {}=? LIMIT 1)' \
    #     .format(data_type, key)
    # sql_update = 'UPDATE {} SET {} WHERE {}=?' \
    #     .format(data_type, ', '.join(['{}=?'.format(k) for k in kwargs.keys()]), key)
    # c = conn.execute(sql_check, (value,))  # we need the comma
    # result = c.fetchone()
    # if result[0]:
    #     c.execute(sql_update, (v, for v in kwargs.values()))
    #     conn.commit()
    # else:
    #     raise err.ItemNotStored(
    #         'Can\'t update "{}" because it\'s not stored in table "{}"'
    #             .format(value, data_type))


@connect
def delete(conn, data_type, key, value):
    pass
    # data_type = scrub(data_type)
    # sql_check = 'SELECT EXISTS(SELECT 1 FROM {} WHERE {}=? LIMIT 1)' \
    #     .format(data_type, key)
    # data_type = scrub(data_type)
    # sql_delete = 'DELETE FROM {} WHERE {}=?'.format(data_type, key)
    # c = conn.execute(sql_check, (value,))  # we need the comma
    # result = c.fetchone()
    # if result[0]:
    #     c.execute(sql_delete, (value,))  # we need the comma
    #     conn.commit()
    # else:
    #     raise err.ItemNotStored(
    #         'Can\'t delete "{}" because it\'s not stored in table "{}"'
    #             .format(value, data_type))
