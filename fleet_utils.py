# fleet_utils.py
# Utility helpers for Vossberg Mobility fleet reporting.
# Modernized 2024: removed dead code, fixed km-to-miles constant.

KM_PER_MILE = 1.609344  # exact; 1 mile = 1.609344 km


def km_to_miles(km: float) -> float:
    """Convert kilometres to miles. Used by the nightly UK partner report."""
    return km / KM_PER_MILE


def format_number(value: float) -> str:
    """Format a number to one decimal place."""
    return f"{value:.1f}"
