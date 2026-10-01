
from start_compiler.import_start import *



class numbers(start):
    def __init__(self, *args):
        self.indexLength = 5
        for i in range(0, self.indexLength):
            self.__dict__[str(i)] = args[i] if len(args) > i else start()
try:
    local_vars['grades'] = start()
    StartError.lineNumber = 6
    check_events()
    _set('grades', local_vars, None)['grades'] = numbers(number(10))
    StartError.lineNumber = 8
    check_events()
    _set(to_key(number(1)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(1))] = _get(to_key(number(0)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(0))]
    StartError.lineNumber = 9
    check_events()
    _set(to_key(number(2)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(2))] = _get(to_key(number(0)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(0))]
    StartError.lineNumber = 10
    check_events()
    _set(to_key(number(3)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(3))] = _get(to_key(number(0)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(0))]
    StartError.lineNumber = 11
    check_events()
    _set(to_key(number(4)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(4))] = _get(to_key(number(0)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(0))]
    StartError.lineNumber = 12
    check_events()
    _set(to_key(number(5)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(5))] = _get(to_key(number(0)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(0))]
    StartError.lineNumber = 14
    check_events()
    _print(_get('grades', local_vars, None)['grades'])
    StartError.lineNumber = 15
    check_events()
    number(42).copy(_set(to_key(number(0)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(0))])
    StartError.lineNumber = 16
    check_events()
    _print(_get('grades', local_vars, None)['grades'])
except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
