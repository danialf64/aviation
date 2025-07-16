# Aviation Model

This document describes a simple model of global aviation.

## Constants

The following constants are required for the model and are defined below.

| Constant                     | Symbol                         | Value           | Unit     | Ref       |
| ---------------------------- | ------------------------------ | --------------- | -------- | --------- |
| Passengers per year          | `passengers_per_year`          | $5 \times 10^9$ | year^-1^ | [^1]      |
| Seats per aircraft           | `seats_per_aircraft`           | 160             | .        | [^2]      |
| Flights per aircraft per day | `flights_per_aircraft_per_day` | 3.6             | day^-1^  | [^1] [^3] |
| Days per year                | `days_per_year`                | 366             | day/year | -         |

ATAG report a global fleet of 29,039 commercial aircraft in operation [^1]. OAG report that the average number of commerical flights per day in 2024 was 103,770 [^3]. From this it can be derived that there is an average of 3.6 flights per aircraft per day. The days per year has been defined as 366 as data from 2024 was used which was a leap year.

## Model for Global Fleet Size

The passengers per day can be defined using the following equation.

$$
\begin{equation}
\text{passengers per day} = \frac{\text{passengers per year}}{\text{days per year}}
\end{equation}
$$

The required global fleet of aircraft can be calculated using the following equation.

$$
\begin{equation}
\text{required global fleet} = \frac{\text{passengers per day}}{\text{seats per aircraft } \times \text{ flights per aircraft per day}}
\end{equation}
$$

## References

[^1]: Air Transport Action Group. 2025. “Facts & Figures.” ATAG. Accessed July 15, 2025. [Link](https://atag.org/facts‑figures).
[^2]: OAG. 2024. “Why Is Average Flight Capacity Increasing at Its Fastest Rate Ever?” OAG Aviation Market Analysis (blog), March 28, 2024. Accessed July 15, 2025. [Link](https://www.oag.com/blog/average-flight-capacity-increasing-at-fastest-rate-ever).
[^3]: OAG Aviation Worldwide Limited. “Airline Frequency and Capacity Statistics.” Updated July 2025. OAG Aviation Data. Accessed July 15, 2025. [Link](https://www.oag.com/airline-frequency-and-capacity-statistics).
