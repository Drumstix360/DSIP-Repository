
from start_compiler.import_start import *



class savings(start):
    def __init__(self, *args):
        self.indexLength = 3
        for i in range(0, self.indexLength):
            self.__dict__[str(i)] = args[i] if len(args) > i else start()
try:
    local_vars['my_savings'] = start()
    StartError.lineNumber = 9
    check_events()
    _set('my_savings', local_vars, None)['my_savings'] = savings(number(1000), number(15000), number(932))
    local_vars['total_savings'] = start()
    StartError.lineNumber = 16
    check_events()
    _set('total_savings', local_vars, None)['total_savings'] = _add(_add(_get(to_key(number(0)), local_vars, _get('my_savings', local_vars, None)['my_savings'])[to_key(number(0))], _get(to_key(number(1)), local_vars, _get('my_savings', local_vars, None)['my_savings'])[to_key(number(1))]), _get(to_key(number(2)), local_vars, _get('my_savings', local_vars, None)['my_savings'])[to_key(number(2))])
    StartError.lineNumber = 20
    check_events()
    _print(text(" My savings accounts have the following amounts : "), _get('my_savings', local_vars, None)['my_savings'])
    StartError.lineNumber = 21
    check_events()
    _print(text(" which total : "), _get('total_savings', local_vars, None)['total_savings'])
except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
