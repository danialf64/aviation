"""Growth in global demand for aviation."""

__all__ = (
    "demand_change_rate",
    "passengers_per_year",
)

import enum
import typing

import camia_model as model
from camia_model.units import DIMENSIONLESS, Quantity, percent, year

from aviation.units import passenger

PASSENGERS_PER_YEAR_IN_2025 = 5_000_000_000.0 * passenger / year


@enum.unique
class DemandChangeModel(enum.Enum):
    """Different models that can be used for change in demand."""

    CONSTANT = enum.auto()
    EXPONENTIAL = enum.auto()
    LINEAR = enum.auto()


@model.transform
def demand_change_model() -> DemandChangeModel:
    """The model used for demand growth."""
    return DemandChangeModel.EXPONENTIAL


@model.transform
def demand_change_rate(
    demand_change_model: DemandChangeModel,
) -> typing.Annotated[Quantity, percent / year]:
    """The rate at which passenger demand may change in the future."""
    match demand_change_model:
        case DemandChangeModel.EXPONENTIAL:
            return -2.0 * percent / year
        case DemandChangeModel.LINEAR:
            return -1.0 * percent / year
        case DemandChangeModel.CONSTANT:
            return 0.0 * percent / year


@model.transform.switch(demand_change_model=DemandChangeModel.LINEAR)
def passengers_per_year(
    modeling_year: int, demand_change_rate: typing.Annotated[Quantity, percent / year]
) -> typing.Annotated[Quantity, passenger / year]:
    """The number of passengers per year globally.

    Args:
        modeling_year: The year in which the numner of passengers per year globally is projected.
        demand_change_rate: The rate at which passenger demand may change in the future.

    """
    years_since_2025 = float(modeling_year - 2025) * year
    growth_factor = 100.0 * percent + demand_change_rate * years_since_2025
    return (PASSENGERS_PER_YEAR_IN_2025 * growth_factor).convert_to(passenger / year)


@model.transform.switch(demand_change_model=DemandChangeModel.EXPONENTIAL)  # type: ignore[no-redef]
def passengers_per_year(  # noqa: F811
    modeling_year: int, demand_change_rate: typing.Annotated[Quantity, percent / year]
) -> typing.Annotated[Quantity, passenger / year]:
    """The number of passengers per year globally."""
    growth_factor = (100.0 * percent + demand_change_rate * 1.0 * year).convert_to(DIMENSIONLESS)
    return PASSENGERS_PER_YEAR_IN_2025 * growth_factor ** (modeling_year - 2025)


@model.transform.switch(demand_change_model=DemandChangeModel.CONSTANT)  # type: ignore[no-redef]
def passengers_per_year() -> typing.Annotated[Quantity, passenger / year]:  # noqa: F811
    """The number of passengers per year globally."""
    return PASSENGERS_PER_YEAR_IN_2025
