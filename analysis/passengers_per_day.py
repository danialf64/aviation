import aviation

passengers_per_year = 5_000_000_000.0
days_per_year = 366.0

passengers_per_day = aviation.passengers_per_day(passengers_per_year, days_per_year)

print(f"{passengers_per_day=:_}")
