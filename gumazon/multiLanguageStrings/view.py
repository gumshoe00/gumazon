class View:
    @staticmethod
    def asjson(instance):
        _output = {
            "model": instance.__name__
        }
        _dictionary = vars(instance)
        for k in _dictionary.keys():
            if k[0] != '_':
                _output[k] = _dictionary[k]

        return _output
