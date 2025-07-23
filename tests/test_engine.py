import pytest

import aviation
from aviation import _engine as engine


@pytest.mark.parametrize(
    ("inputs", "output", "expected"),
    (
        ({"passengers_per_year": 5_000_000_000}, "passengers_per_year", 5_000_000_000),
        ({"required_global_fleet": 25_000}, "required_global_fleet", 25_000),
        (
            {"days_per_year": 366.0, "passengers_per_year": 5_000_000_000},
            "passengers_per_day",
            13_661_202.18579235,
        ),
        (
            {
                "passengers_per_day": 13_661_202.18579235,
                "seats_per_aircraft": 160.0,
                "flights_per_aircraft_per_day": 3.6,
            },
            "required_global_fleet",
            23717.364905889495,
        ),
        (
            {
                "days_per_year": 366.0,
                "passengers_per_year": 5_000_000_000,
                "seats_per_aircraft": 160.0,
                "flights_per_aircraft_per_day": 3.6,
            },
            "required_global_fleet",
            23717.364905889495,
        ),
    ),
)
def test_systems_model_evaluate(
    systems_model: engine.SystemsModel,
    inputs: dict[str, float],
    output: str,
    expected: float,
) -> None:
    assert systems_model.evaluate(inputs, output) == expected


@pytest.fixture
def systems_model() -> engine.SystemsModel:
    return engine.SystemsModel(aviation.transforms)
