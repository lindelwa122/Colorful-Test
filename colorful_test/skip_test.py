from functools import wraps 
from .exceptions import SkipTest
   
def skip_test(reason=None):
    """
    Calling this during a test method or set_up() skips the current test.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            raise SkipTest(reason)
        return wrapper
    return decorator


def skip_test_if(condition, reason=None):
    """
    Calling this during a test method or set_up() skips the current test if the condition evaluates to True.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if condition: raise SkipTest(reason)
            else: func(*args, **kwargs)
        return wrapper
    return decorator


def skip_test_unless(condition, reason=None):
    """
    Calling this during a test method or set_up() skips the current test unless the condition evaluates to True.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not condition: raise SkipTest(reason)
            else: func(*args, **kwargs)
        return wrapper
    return decorator
