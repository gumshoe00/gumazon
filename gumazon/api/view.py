def _public_params_dict_1l(instance=None):
    _output = {}
    if instance:
        _dic = {}
        _vars = (vars(instance) or {})
        for _k in _vars.keys():
            if _k[0] != '_':
                _dic[_k] = _vars[_k]
        _name = type(instance).__name__
        _output[_name[0].lower()+_name[1:]] = _dic

    return _output


class View:

    @staticmethod
    def index(item_type, instances):
        _output = []
        for instance in instances:
            _output.append(_public_params_dict_1l(instance))
        return {
            item_type.__tablename__+'s': _output,
            'message': '{} List'.format(item_type.__name__)
        }

    @staticmethod
    def show(item_type, instance):
        output = {}
        output.update(_public_params_dict_1l(instance))
        output['message'] = 'Show {}'.format(item_type.__name__)
        return output

    @staticmethod
    def error(item_type, err, **kwargs):
        _output = {
            item_type.__name__: {},
            'message': '{} ({}) - {}'.format(item_type.__name__, kwargs.copy(), err.args[0])
        }
        return _output

    @staticmethod
    def new(item_type, instance):
        return {
            item_type.__name__: _public_params_dict_1l(instance),
            'message': 'Show New {}'.format(item_type.__name__)
        }

    @staticmethod
    def change(o_type, n_type):
        return {
            n_type.__name__: n_type,
            'message': 'Change Data Type From {} to {}'.format(o_type.__name__, n_type.__name__)
        }

    @staticmethod
    def update(item_type, **kwargs):
        _old = kwargs.get('old', {})
        _new = kwargs.get('new', {})
        try:
            _old = _public_params_dict_1l(vars(_old))
        except Exception as e:
            print(e)
            pass

        try:
            _new = _public_params_dict_1l(vars(_new))
        except Exception as e:
            print(e)
            pass

        return {
            item_type.__name__: _new,
            'message': 'Changed {} from {}'.format(item_type.__name__, _old)
        }

    @staticmethod
    def delete(item_type, key, value, *instances):
        _output = []
        _in_instances = []
        _in_instances.extend(instances)
        for instance in instances:
            _output.append(_public_params_dict_1l(instance))
        return {
            item_type.__tablename__+'s': _output,
            'message': 'Deleted {} - {}: {}'.format(item_type.__name__, key, value)
        }
