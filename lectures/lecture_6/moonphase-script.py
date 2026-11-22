#!/usr/bin/env python3
import datetime
import math

def moon_phase_symbol():
    # Current date
    now = datetime.datetime.utcnow()
    year = now.year
    month = now.month
    day = now.day

    # Conway's simplified moon phase algorithm
    if month < 3:
        year -= 1
        month += 12

    K1 = int(365.25 * (year + 4712))
    K2 = int(30.6 * (month + 1))
    K3 = int(int((year/100) + 49) * 0.75) - 38

    # Julian day approximation
    J = K1 + K2 + day + 59
    if J > 2299160:
        J -= K3

    # Moon phase (0–29.53 days)
    moon_age = (J - 2451550.1) / 29.53058867
    moon_age = moon_age % 1  # fraction of the cycle
    age_days = moon_age * 29.53

    # Map age to Unicode symbols
    phases = [
        (1.0, "🌑 New Moon"),
        (6.3825, "🌒 Waxing Crescent"),
        (9.3825, "🌓 First Quarter"),
        (13.765, "🌔 Waxing Gibbous"),
        (16.765, "🌕 Full Moon"),
        (20.148, "🌖 Waning Gibbous"),
        (23.148, "🌗 Last Quarter"),
        (27.53, "🌘 Waning Crescent"),
        (29.53, "🌑 New Moon")
    ]

    for threshold, symbol in phases:
        if age_days <= threshold:
            return symbol

if __name__ == "__main__":
    print(moon_phase_symbol())
