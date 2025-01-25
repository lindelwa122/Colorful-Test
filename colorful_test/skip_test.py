from functools import wraps
from typing import Any, Callable, Dict, Tuple

from .exceptions import SkipTest

type Decorator = Callable[[Callable[[], None]], Callable[[Tuple[Any], Dict[str, Any]], None]]

def skip_test(reason: str | None=None) -> Decorator:
    """
    Calling this during a test method or set_up() skips the current test.
    """

    def decorator(func: Callable[[], None]):
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any):
            raise SkipTest(reason)
        return wrapper
    return decorator


def skip_test_if(condition: bool, reason: str | None=None) -> Decorator:
    """
    Calling this during a test method or set_up() skips the current test if the condition evaluates to True.
    """

    def decorator(func: Callable[[], None]):
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any):
            if condition:
                raise SkipTest(reason)
            else:
                func(*args, **kwargs)
        return wrapper
    return decorator


def skip_test_unless(condition: bool, reason: str | None=None) -> Decorator:
    """
    Calling this during a test method or set_up() skips the current test unless the condition evaluates to True.
    """

    def decorator(func: Callable[[], None]):
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any):
            if not condition:
                raise SkipTest(reason)
            else:
                func(*args, **kwargs)
        return wrapper
    return decorator
