class Application:
    def __init__(self, *args, **kwargs):
        print(self.__class__.__name__, '__init__')
        print(list(args), kwargs.copy())

    def __call__(self, *args, **kwargs):
        print(self.__class__.__name__, '__call__')
        print(list(args), kwargs.copy())
