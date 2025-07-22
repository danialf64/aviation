import pytest

from aviation.fleet import passengers_per_day, required_global_fleet


@pytest.mark.parametrize(
    ("passengers_per_year", "days_per_year", "expected_passengers_per_day"),
    (
        (365_000_000.0, 365.0, 1_000_000.0),
        (732_000_000.0, 366.0, 2_000_000.0),
    ),
)
def test_passengers_per_day(passengers_per_year, days_per_year, expected_passengers_per_day):
    assert passengers_per_day(passengers_per_year, days_per_year) == expected_passengers_per_day


@pytest.mark.parametrize("days_per_year", (365.0, 365.25, 366.0))
def test_required_global_fleet(days_per_year):
    passengers_per_year = 5_000_000_000.0
    seats_per_aircraft = 200.0
    flights_per_aircraft_per_day = 3.0

    expected_required_global_fleet = 25_000.0

    result = required_global_fleet(
        passengers_per_day(passengers_per_year, days_per_year),
        seats_per_aircraft,
        flights_per_aircraft_per_day,
    )
    assert result == pytest.approx(expected_required_global_fleet, abs=5_000.0)
