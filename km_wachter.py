# km_wachter.py
# KM-Waechter decides when a Vossberg Mobility car needs a service.
# Written in 2013. Modernized 2024.

SERVICE_INTERVAL_KM = 15000
WARN_AT_PERCENT = 80


def wear_percent(km_since_service: float, interval: float) -> float:
    """Return the percentage of the service interval that has been used up."""
    return (km_since_service / interval) * 100


def needs_service(car: dict) -> bool:
    """Return True if the car has used 80 % or more of its service interval.

    A car with no last_service_km reading is treated as having no data:
    it is not flagged (False), because we cannot compute a valid wear figure.
    """
    if "last_service_km" not in car:
        return False
    km_since = car["odometer"] - car["last_service_km"]
    return wear_percent(km_since, SERVICE_INTERVAL_KM) >= WARN_AT_PERCENT


def check_fleet(fleet: list[dict]) -> list[str]:
    """Flag every car that is due for service and return their IDs."""
    flagged = []
    for car in fleet:
        if needs_service(car):
            flagged.append(car["id"])
            print(f"SERVICE DUE: {car['id']}")
    return flagged
