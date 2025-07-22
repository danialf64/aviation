"""Decorate functions as transforms."""

__all__ = ("Transform", "transform")

import collections.abc
import inspect
import typing


class Transform[R, **P](typing.Protocol):
    name: str
    parameters: tuple[str, ...]

    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> R: ...


def transform[R, **P](
    function: collections.abc.Callable[P, R],
) -> Transform[R, P]:
    """Decorator to identify functions as transforms."""
    transform = typing.cast("Transform[R, P]", function)
    transform.name = function.__name__
    transform.parameters = tuple(inspect.signature(function).parameters.keys())
    return transform
