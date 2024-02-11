from typing import Callable

try:
    from typing import ParamSpec  # type: ignore[attr-defined,unused-ignore]
except ImportError:
    from typing_extensions import ParamSpec  # type: ignore[import,unused-ignore]

P = ParamSpec("P")

def func(arg: Callable[P, None]) -> None:
    return None
