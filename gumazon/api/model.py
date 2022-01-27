
from .models import dbadaptor as db_adaptor


class Model:

    def __init__(self, data_type):
        self._data_type = data_type
        self._connection = db_adaptor.db_session(db_adaptor.DB_NAME)()

    @property
    def connection(self):
        return self._connection

    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value

    def save(self, key, value, **kwargs):
        db_adaptor.save(self.connection, self.data_type, key, value, **kwargs.copy())

    def show(self, key, value):
        return db_adaptor.show(self.connection, self.data_type, key, value)

    def index(self):
        return db_adaptor.index(self.connection, self.data_type)

    def update(self, key, value, **kwargs):
        db_adaptor.update(self.connection, self.data_type, key, value, **kwargs.copy())

    def delete(self, key, value):
        db_adaptor.delete(self.connection, self.data_type, key, value)
