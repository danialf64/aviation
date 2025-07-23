"""Analysis to determine the number of passengers per day globally."""

import camia_engine as engine

import aviation

passengers_per_year = 5_000_000_000.0
days_per_year = 366.0

inputs = {"days_per_year": days_per_year, "passengers_per_year": passengers_per_year}
output = "passengers_per_day"
systems_model = engine.SystemsModel(aviation.transforms)

passengers_per_day = systems_model.evaluate(inputs, output)

print(f"{passengers_per_day=:_}")
