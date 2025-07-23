import typing

import pytest
from camia_model.units import Quantity, day, year

from aviation.fleet import passengers_per_day, required_global_fleet
from aviation.units import aircraft, journey, passenger


@pytest.mark.parametrize(
    ("passengers_per_year", "days_per_year", "expected_passengers_per_day"),
    (
        (365_000_000.0 * passenger / year, 365.0 * day / year, 1_000_000.0 * passenger / day),
        (732_000_000.0 * passenger / year, 366.0 * day / year, 2_000_000.0 * passenger / day),
    ),
)
def test_passengers_per_day(
    passengers_per_year: typing.Annotated[Quantity, passenger / year],
    days_per_year: typing.Annotated[Quantity, day / year],
    expected_passengers_per_day: typing.Annotated[Quantity, passenger / year],
) -> None:
    assert passengers_per_day(passengers_per_year, days_per_year) == expected_passengers_per_day


@pytest.mark.parametrize(
    ("days_per_year", "expected_required_global_fleet"),
    (
        (365.0 * day / year, 22831.050228310505 * aircraft),
        (365.25 * day / year, 22815.423226100844 * aircraft),
        (366.0 * day / year, 22768.670309653917 * aircraft),
    ),
)
def test_required_global_fleet(
    days_per_year: typing.Annotated[Quantity, day / year],
    expected_required_global_fleet: typing.Annotated[Quantity, aircraft],
) -> None:
    passengers_per_year = 5_000_000_000.0 * passenger / year
    seats_per_aircraft = 200.0 * passenger / aircraft
    flights_per_aircraft_per_day = 3.0 * journey / (aircraft * day)

    result = required_global_fleet(
        passengers_per_day(passengers_per_year, days_per_year),
        seats_per_aircraft,
        flights_per_aircraft_per_day,
    )
    assert result == expected_required_global_fleet
