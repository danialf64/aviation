"""A simple of global aviation.

Modules:
    fleet: Modelling of the global fleet based on average passenger and aircraft
        data.
"""

__all__ = ("passengers_per_day", "required_global_fleet")

from aviation.fleet import passengers_per_day, required_global_fleet

transforms = (passengers_per_day, required_global_fleet)
