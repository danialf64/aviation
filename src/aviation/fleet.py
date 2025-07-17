def passengers_per_day(passengers_per_year, days_per_year):
    return passengers_per_year / days_per_year


def required_global_fleet(passengers_per_day, seats_per_aircraft, flights_per_aircraft_per_day):
    return passengers_per_day / (seats_per_aircraft * flights_per_aircraft_per_day)
