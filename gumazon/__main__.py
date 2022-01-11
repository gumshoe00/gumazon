"""Main module."""

import argparse
import sys


class Gumazon:
    def __init__(self):
        print(self.__class__.__name__)
        print('Hello World!')

    def __call__(self, *args, **kwargs):
        _output = {}
        _output.update({"args": [_arg for _arg in args]})
        _output.update(kwargs.copy())

        def _dict2txt(value):
            _output = ''
            for _k in value.keys():
                _output += _k
                _output += str(value[_k])
            return _output

        def _astxt(value):
            _output = ''

            _output += str(value)
            return _output

        for item in _output.items():
            yield str(item)


def main():
    """Console script for gumazon."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    print(Gumazon()(*args))
    return Gumazon()(*args)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
