
from start_compiler.import_start import *


try:
    local_vars['a'] = start()
    local_vars['b'] = start()
    local_vars['firstname'] = start()
    local_vars['lastname'] = start()
    StartError.lineNumber = 6
    check_events()
    _set('a', local_vars, None)['a'] = number(8).clone()
    StartError.lineNumber = 7
    check_events()
    _set('b', local_vars, None)['b'] = number(2).clone()
    StartError.lineNumber = 9
    check_events()
    _set('firstname', local_vars, None)['firstname'] = text("Banana ").clone()
    StartError.lineNumber = 10
    check_events()
    _set('lastname', local_vars, None)['lastname'] = text("Apple").clone()
    local_vars['fullname'] = start()
    StartError.lineNumber = 13
    check_events()
    _set('fullname', local_vars, None)['fullname'] = _append(_get('firstname', local_vars, None)['firstname'], _append(text(" "), _get('lastname', local_vars, None)['lastname'])).clone()
    local_vars['c'] = start()
    StartError.lineNumber = 16
    check_events()
    _set('c', local_vars, None)['c'] = _add(_get('a', local_vars, None)['a'], _get('b', local_vars, None)['b']).clone()
    local_vars['d'] = start()
    StartError.lineNumber = 19
    check_events()
    _set('d', local_vars, None)['d'] = _sub(_get('a', local_vars, None)['a'], _get('b', local_vars, None)['b']).clone()
    local_vars['e'] = start()
    StartError.lineNumber = 22
    check_events()
    _set('e', local_vars, None)['e'] = _and(_get('a', local_vars, None)['a'], _get('b', local_vars, None)['b']).clone()
    local_vars['f'] = start()
    StartError.lineNumber = 25
    check_events()
    _set('f', local_vars, None)['f'] = _lt(_get('a', local_vars, None)['a'], _get('b', local_vars, None)['b']).clone()
    StartError.lineNumber = 27
    check_events()
    _print(text("The sum of a and b is "), _get('c', local_vars, None)['c'], text(" the difference is "), _get('d', local_vars, None)['d'], text(" , a and b (logical and) is "), _get('e', local_vars, None)['e'], text(" , a smaller than b is "), _get('f', local_vars, None)['f'], text(" , the full name is "), _get('fullname', local_vars, None)['fullname'])
except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
