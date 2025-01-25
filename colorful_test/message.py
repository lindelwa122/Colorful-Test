from functools import wraps
from typing import Any, Callable

from .exceptions import SkipTest
from .skip_test import Decorator


def output_msg(type: str, msg: str) -> None:
    """
    Prints a message with a green tick if the type is 'suc'; otherwise,
    prints it with a red cross.
    """

    match type:
        case 'err':
            print(f'\033[31m\u00d7 {msg}\033[0m')
        case 'suc':
            print(f'\033[32m\u2713 {msg}\033[0m')


def show_message(fail: str | None=None, success: str | None=None) -> Decorator:
    """
    Decorator used to print a failure message if a test fails or a success
    message if a test passes.

    If one or the other is specified, show_message will only print for 
    that case. For example, if you don't want to print anything when a 
    test passes, you can omit the success message.
    """
    
    def decorator(func: Callable[[], None]):
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any):
            try:
                func(*args, **kwargs)

                if success:
                    output_msg('suc', success)

            except (AssertionError, SkipTest) as err:
                fail_msg = fail

                first = err.args[0]['first']
                if fail_msg and '%f' in fail_msg:
                    fail_msg = fail_msg.replace('%f', str(first))

                second = err.args[0]['second']
                if fail_msg and '%s' in fail_msg:
                    fail_msg = fail_msg.replace('%s', str(second))

                if fail_msg:
                    output_msg('err', fail_msg)

                raise err

        return wrapper
    return decorator
