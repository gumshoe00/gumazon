#!/usr/bin/env python


import sqlalchemy as sa
import sqlalchemy.orm as orm
from db_base import Base


class Session:
    def __init__(self, db_file):
        self.factory = None
        self.__connect(db_file)

    def connect(self, db_file):
        if self.factory:
            return

        if not db_file or not db_file.strip():
            raise Exception("You must specify a db file!")

        connection_string = 'sqlite:///' + db_file.strip()
        print(f"Connecting to database: {connection_string}")

        engine = sa.create_engine(connection_string, echo=False)
        self.factory = orm.sessionmaker(bind=engine)

        Base.metadata.create_all(engine)

    __connect = connect
