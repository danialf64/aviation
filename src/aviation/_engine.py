import collections.abc
import typing

from aviation._model import Transform


class SystemsModel:
    def __init__(self, transforms: collections.abc.Sequence[Transform[typing.Any, ...]]) -> None:
        self.transforms = set(transforms)

    def evaluate(self, inputs: dict[str, typing.Any], output: str) -> typing.Any:  # noqa: ANN401
        # If the requested `output` has already been suppleied as an input then this can just be
        # returned directly without any need for computation.
        if output in inputs:
            return inputs[output]
        # The requested `output` isn't in `inputs` so it must be the name of a transform in
        # `self.transforms`. If it is not found in `self.transforms` then there must be an error.
        for transform in self.transforms:
            if transform.name == output:
                break
        else:
            message = f"No transform with name `{output}`."
            raise ValueError(message)
        # To evaluate the `transform`, argument for all of its parameters are required. If a
        # parameter's
        for parameter in transform.parameters:
            if parameter not in inputs:
                inputs[parameter] = self.evaluate(inputs, parameter)

        # Evaluate and return the `transform` associated with the passed `output`.
        arguments = {parameter: inputs[parameter] for parameter in transform.parameters}
        return transform(**arguments)
