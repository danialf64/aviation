import typing

import pytest
import pytest_camia
from camia_model.units import Quantity, day, year

from aviation.fleet import passengers_per_day, required_global_fleet
from aviation.units import aircraft, journey, passenger


@pytest.mark.parametrize(
    ("passengers_per_year", "expected_passengers_per_day"),
    (
        (365_000_000.0 * passenger / year, 999315.5373 * passenger / day),
        (732_000_000.0 * passenger / year, 2004106.77618 * passenger / day),
    ),
)
def test_passengers_per_day(
    passengers_per_year: typing.Annotated[Quantity, passenger / year],
    expected_passengers_per_day: typing.Annotated[Quantity, passenger / year],
) -> None:
    assert passengers_per_day(passengers_per_year) == pytest_camia.approx(
        expected_passengers_per_day
    )


@pytest.mark.parametrize(
    ("passengers_per_day", "expected_required_global_fleet"),
    (
        (10_000_000.0 * passenger / day, 16_666.6666 * aircraft),
        (12_500_000.0 * passenger / day, 20_833.3333 * aircraft),
        (15_000_000.0 * passenger / day, 25_000.0000 * aircraft),
    ),
)
def test_required_global_fleet(
    passengers_per_day: typing.Annotated[Quantity, passenger / year],
    expected_required_global_fleet: typing.Annotated[Quantity, aircraft],
) -> None:
    seats_per_aircraft = 200.0 * passenger / aircraft
    flights_per_aircraft_per_day = 3.0 * journey / (aircraft * day)

    result = required_global_fleet(
        passengers_per_day,
        seats_per_aircraft,
        flights_per_aircraft_per_day,
    )
    assert result == pytest_camia.approx(expected_required_global_fleet)
