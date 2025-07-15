# Aviation

This document describes a simple model of global aviation.

## Constants

The following constants are required for the model and are defined below.

| Constant                     | Symbol                         | Value         | Unit            | Ref       |
| ---------------------------- | ------------------------------ | ------------- | --------------- | --------- |
| Passengers per year          | `passengers_per_year`          | 5,000,000,000 | passengers/year | [^1]      |
| Seats per aircraft           | `seats_per_aircraft`           | 160           | seats           | [^2]      |
| Flights per aircraft per day | `flights_per_aircraft_per_day` | 3.6           | flights/day     | [^1] [^2] |
| Days per year                | `days_per_year`                | 365.25        | days/year       | -         |

ATAG report a global fleet of 29,039 commercial aircraft in operation [^1]. OAG report the average number of commerical flights per day is 103,770. From this it can be derived that the 3.6 flights per aircraft per day.

## Model for Global Feet Size

The passengers per day can be defined using the following equation.

$$
\begin{equation}
\text{passengers\_per\_day} = \frac{\text{passengers\_per\_year}}{\text{days\_per\_year}}
\end{equation}
$$

The required global fleet of aircraft can be calculated using the following equation.

$$
\begin{equation}
\text{required\_global\_feet} = \frac{\text{passengers\_per\_day}}{\text{seats\_per\_aircraft} \times \text{flights\_per\_aircraft\_per\_day}}
\end{equation}
$$

## References

[^1]: Air Transport Action Group. 2025. “Facts & Figures.” ATAG. Accessed July 15, 2025. https://atag.org/facts‑figures.
[^2]: OAG. 2024. “Why Is Average Flight Capacity Increasing at Its Fastest Rate Ever?” OAG Aviation Market Analysis (blog), March 28, 2024. Accessed July 15, 2025. https://www.oag.com/blog/average-flight-capacity-increasing-at-fastest-rate-ever.
[^3]: OAG Aviation Worldwide Limited. “Airline Frequency and Capacity Statistics.” Updated July 2025. OAG Aviation Data. Accessed July 15, 2025. https://www.oag.com/airline-frequency-and-capacity-statistics
