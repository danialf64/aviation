import typing

import camia_engine as engine
import pytest
import pytest_camia
from camia_model.units import Quantity, day, year

import aviation
from aviation.units import aircraft, journey, passenger

UnitQuantity = (
    typing.Annotated[Quantity, passenger / year]
    | typing.Annotated[Quantity, aircraft]
    | typing.Annotated[Quantity, day / year]
    | typing.Annotated[Quantity, passenger / day]
    | typing.Annotated[Quantity, journey / (aircraft * day)]
)


@pytest.mark.parametrize(
    ("inputs", "output", "expected"),
    (
        (
            {"passengers_per_year": 5_000_000_000.0 * passenger / year},
            "passengers_per_year",
            5_000_000_000.0 * passenger / year,
        ),
        (
            {"required_global_fleet": 25_000.0 * aircraft},
            "required_global_fleet",
            25_000.0 * aircraft,
        ),
        (
            {
                "passengers_per_year": 5_000_000_000.0 * passenger / year,
            },
            "passengers_per_day",
            13689253.93566 * passenger / day,
        ),
        (
            {
                "passengers_per_day": 13_661_202.186 * passenger / day,
                "seats_per_aircraft": 160.0 * passenger / aircraft,
                "flights_per_aircraft_per_day": 3.6 * journey / (aircraft * day),
            },
            "required_global_fleet",
            23717.3649 * aircraft,
        ),
        (
            {
                "passengers_per_year": 5_000_000_000.0 * passenger / year,
                "seats_per_aircraft": 160.0 * passenger / aircraft,
                "flights_per_aircraft_per_day": 3.6 * journey / (aircraft * day),
            },
            "required_global_fleet",
            23766.06586 * aircraft,
        ),
    ),
)
def test_systems_model_evaluate(
    systems_model: engine.SystemsModel,
    inputs: dict[str, UnitQuantity],
    output: str,
    expected: UnitQuantity,
) -> None:
    assert systems_model.evaluate(inputs, output) == pytest_camia.approx(expected)


@pytest.fixture
def systems_model() -> engine.SystemsModel:
    return engine.SystemsModel(aviation.transforms)
