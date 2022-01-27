from .model import Model
from .view import View
from .models import err


class Controller:
    """Accepts user’s inputs and delegates data representation to the View and data handling to the Model.
    """

    def __init__(self, data_type):
        self.model = Model(data_type)
        self.view = View

    def index(self):
        return self.view.index(self.model.data_type, self.model.index())

    def show(self, key, value):
        try:
            self.view.show(self.model.data_type, self.model.show(key, value))
        except err.ItemNotStored as e:
            self.view.error(self.model.data_type, e, **{key: value})

    def save(self, key, value, **kwargs):
        try:
            self.model.save(key, value, **kwargs.copy())
        except err.ItemAlreadyStored as e:
            self.view.error(self.model.data_type, e, **{key: value})
        else:
            self.view.new(self.model.data_type, self.model.show(key, value))

    def update(self, key, value, **kwargs):
        # assert price > 0, 'price must be greater than 0'
        # assert quantity >= 0, 'quantity must be greater than or equal to 0'

        try:
            older = self.model.show(key, value)
        except err.ItemNotStored as e:
            self.view.error(self.model.data_type, e, **{key: value})
        else:
            self.model.update(key, value, **kwargs.copy())
            self.view.update(self.model.data_type, **{key: value, 'old': older, 'new': self.model.show(key, value)})

    def update_type(self, new_data_type):
        old_data_type = self.model.data_type
        self.model.data_type = new_data_type
        self.view.change(old_data_type, new_data_type)

    def delete(self, key, value):
        try:
            self.model.delete(key, value)
            self.view.delete(self.model.data_type, key, value, *self.model.index())
        except err.ItemNotStored as e:
            self.view.error(self.model.data_type, e, **{key: value})

