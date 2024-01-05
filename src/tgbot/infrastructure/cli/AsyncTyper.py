from asyncio import run
from collections.abc import Callable
from functools import wraps
from typing import Any

import typer


class AsyncTyper(typer.Typer):
    def async_command(
        self, *args: Any, **kwargs: Any
    ) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
        def decorator(async_func: Callable[..., Any]) -> Callable[..., Any]:
            @wraps(async_func)
            def sync_func(*_args: Any, **_kwargs: Any) -> Any:
                return run(async_func(*_args, **_kwargs))

            self.command(*args, **kwargs)(sync_func)
            return async_func

        return decorator
