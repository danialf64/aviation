# Aviation Model

This document describes a simple model of global aviation.

## Constants

The following constants are required for the model and are defined below.

| Constant                     | Symbol                         | Value           | Unit         | Ref                                         |
| ---------------------------- | ------------------------------ | --------------- | ------------ | ------------------------------------------- |
| Passengers per year          | `passengers_per_year`          | $5 \times 10^9$ | year^-1^     | ATAG[@atagFactsFigures]                     |
| Seats per aircraft           | `seats_per_aircraft`           | 160             | .            | OAG[@oag2024flightcapacity]                 |
| Flights per aircraft per day | `flights_per_aircraft_per_day` | 3.6             | day^-1^      | OAG[@atagFactsFigures] [@oag2025statistics] |
| Days per year                | `days_per_year`                | 366             | day year^-1^ | -                                           |

ATAG report a global fleet of 29,039 commercial aircraft in operation [@atagFactsFigures]. OAG report that the average number of commerical flights per day in 2024 was 103,770 [@oag2025statistics]. From this it can be derived that there is an average of 3.6 flights per aircraft per day. The days per year has been defined as 366 as data from 2024 was used which was a leap year.

## Model for Global Fleet Size

The passengers per day can be defined using the equation $\eqref{eq:passengers_per_day}$.

$$
\begin{equation}
    \text{passengers per day} = \frac{\text{passengers per year}}{\text{days per year}}
    \label{eq:passengers_per_day}
\end{equation}
$$

The required global fleet of aircraft can be calculated using the equation $\eqref{eq:required_global_fleet}$.

$$
\begin{equation}
    \text{required global fleet} = \frac{\text{passengers per day}}{\text{seats per aircraft } \times \text{ flights per aircraft per day}}
    \label{eq:required_global_fleet}
\end{equation}
$$
