from api.controller import Controller
from api.models.product import Product
from api.models.user import User


def test_products():
    products = Controller(Product)

    # CREATE
    def _create():
        products.save('name', 'bread', price=0.5, quantity=20)
        products.save('name', 'milk', price=1.0, quantity=10)
        products.save('name', 'wine', price=10.0, quantity=5)
        products.save('name', 'beer', price=3.0, quantity=15)

    # READ
    def _read():
        print('___INDEX___')
        print(products.index())
        print('___SHOW___')
        print(products.show('name', 'bread'))

    # UPDATE
    def _update():
        print('___UPDATE___')
        products.update('name', 'bread', price=2.0, quantity=30)
        print('___SHOW___')
        print(products.show('name', 'bread'))

    # DELETE
    def _del():
        print('___DELETE___')
        products.delete('name', 'beer')
        print('__INDEX__')
        print(products.index())

    # print(_create())
    print(_read())
    print(_update())
    print(_del())


def test_users():
    users = Controller(User)

    # CREATE
    def _create():
        users.save('username', 'guest1', group='anonymous')
        users.save('username', 'guest2', group='anonymous')
        users.save('username', 'guest2', group='anonymous')
        users.save('username', 'guest4', group='anonymous')

    # READ
    def _read():
        print('___INDEX___')
        print(users.index())
        print('___SHOW___')
        print(users.show('username', 'guest1'))

    # UPDATE
    def _update():
        print('___UPDATE___')
        users.update('username', 'guest1', group='guest')
        print('___SHOW___')
        print(users.show('username', 'guest1'))

    # DELETE
    def _del():
        print('___DELETE___')
        users.delete('username', 'guest2')
        print('__INDEX__')
        print(users.index())

    # print(_create())
    print(_read())
    print(_update())
    print(_del())


def main():
    test_users()
    test_products()


if __name__ == '__main__':
    main()
