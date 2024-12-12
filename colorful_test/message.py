from .exceptions import SkipTest
from functools import wraps

def output_msg(type, msg):
    match type:
        case 'err': print(f'\033[31m\u00D7 {msg}\033[0m')
        case 'suc': print(f'\033[32m\u2713 {msg}\033[0m')

def show_message(fail=None, success=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
                
                if success: output_msg('suc', success)
                
            except (AssertionError, SkipTest) as err:
                fail_msg = fail
                
                first = err.args[0]['first']
                if fail_msg and '%f' in fail_msg:
                    fail_msg = fail_msg.replace('%f', str(first))
                    
                second = err.args[0]['second']
                if fail_msg and '%s' in fail_msg:
                    fail_msg = fail_msg.replace('%s', str(second))
                
                if fail_msg: output_msg('err', fail_msg)
                
                raise err
            
        return wrapper
    
    return decorator
