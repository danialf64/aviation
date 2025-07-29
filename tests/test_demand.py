import typing

import pytest
import pytest_camia
from camia_model.units import Quantity, percent, year

from aviation.demand import DemandChangeModel, demand_change_rate, passengers_per_year
from aviation.units import passenger


@pytest.mark.parametrize(
    ("demand_change_model", "expected_demand_change_rate"),
    (
        (DemandChangeModel.EXPONENTIAL, -2.0 * percent / year),
        (DemandChangeModel.LINEAR, -1.0 * percent / year),
        (DemandChangeModel.CONSTANT, 0.0 * percent / year),
    ),
)
def test_demand_change_rate(
    demand_change_model: DemandChangeModel,
    expected_demand_change_rate: typing.Annotated[Quantity, percent / year],
) -> None:
    assert (
        demand_change_rate(demand_change_model=demand_change_model) == expected_demand_change_rate
    )


@pytest.mark.parametrize(
    ("context", "modeling_year", "demand_change_rate", "expected_passengers_per_year"),
    (
        (
            {"demand_change_model": DemandChangeModel.EXPONENTIAL},
            2025,
            3.0 * percent / year,
            5_000_000_000.0 * passenger / year,
        ),
        (
            {"demand_change_model": DemandChangeModel.EXPONENTIAL},
            2025,
            5.0 * percent / year,
            5_000_000_000.0 * passenger / year,
        ),
        (
            {"demand_change_model": DemandChangeModel.EXPONENTIAL},
            2050,
            -2.0 * percent / year,
            3_017_323_649.0 * passenger / year,
        ),
    ),
)
def test_passengers_per_year(
    context: dict[str, DemandChangeModel],
    modeling_year: int,
    demand_change_rate: typing.Annotated[Quantity, percent / year],
    expected_passengers_per_year: typing.Annotated[Quantity, passenger / year],
) -> None:
    with passengers_per_year.context(**context):
        assert passengers_per_year(modeling_year, demand_change_rate) == pytest_camia.approx(
            expected_passengers_per_year
        )
