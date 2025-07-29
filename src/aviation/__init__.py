"""A simple of global aviation.

Modules:
    fleet: Modelling of the global fleet based on average passenger and aircraft
        data.
"""

__all__ = ("DemandChangeModel", "transforms")

from aviation.demand import (
    DemandChangeModel,
    demand_change_model,
    demand_change_rate,
    passengers_per_year,
)
from aviation.fleet import passengers_per_day, required_global_fleet

transforms = (
    demand_change_model,
    demand_change_rate,
    passengers_per_day,
    passengers_per_year,
    required_global_fleet,
)
