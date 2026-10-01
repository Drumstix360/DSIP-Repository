
from start_compiler.import_start import *



class savings(start):
    def __init__(self, *args):
        self.indexLength = 3
        for i in range(0, self.indexLength):
            self.__dict__[str(i)] = args[i] if len(args) > i else start()

class client(start):
    def __init__(self, *args):
        self.name = args[0] if len(args) > 0 else start()
        self.bank_numbers = args[1] if len(args) > 1 else start()
        self.balance = args[2] if len(args) > 2 else start()
try:
    local_vars['my_savings'] = start()
    StartError.lineNumber = 17
    check_events()
    _set('my_savings', local_vars, None)['my_savings'] = savings(number(1000), number(15000), number(932))
    local_vars['total_savings'] = start()
    StartError.lineNumber = 24
    check_events()
    _set('total_savings', local_vars, None)['total_savings'] = _add(_add(_get(to_key(number(0)), local_vars, _get('my_savings', local_vars, None)['my_savings'])[to_key(number(0))], _get(to_key(number(1)), local_vars, _get('my_savings', local_vars, None)['my_savings'])[to_key(number(1))]), _get(to_key(number(2)), local_vars, _get('my_savings', local_vars, None)['my_savings'])[to_key(number(2))])
    local_vars['bank_account'] = start()
    StartError.lineNumber = 28
    check_events()
    _set('bank_account', local_vars, None)['bank_account'] = client(text(" Test "), _get('my_savings', local_vars, None)['my_savings'], _get('total_savings', local_vars, None)['total_savings'])
    StartError.lineNumber = 31
    check_events()
    _print(text(" My back account details : "), _get('bank_account', local_vars, None)['bank_account'])
except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
