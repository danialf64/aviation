"""Analysis to determine the required size of the global fleet."""

import camia_engine as engine
from camia_model.units import day

import aviation
from aviation.units import aircraft, journey, passenger

seats_per_aircraft = 160.0 * passenger / aircraft
flights_per_aircraft_per_day = 3.6 * journey / (aircraft * day)
modeling_year = list(range(2025, 2051))
inputs = {
    "demand_change_model": aviation.DemandChangeModel.EXPONENTIAL,
    "modeling_year": modeling_year,
    "seats_per_aircraft": seats_per_aircraft,
    "flights_per_aircraft_per_day": flights_per_aircraft_per_day,
}
output = "required_global_fleet"

systems_model = engine.SystemsModel(aviation.transforms)
required_global_fleet = systems_model.evaluate(inputs, output)
print(f"{required_global_fleet}")
