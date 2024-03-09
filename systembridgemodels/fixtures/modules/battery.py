"""Fixture for battery module."""
from systembridgemodels.modules.battery import Battery

FIXTURE_BATTERY = Battery(
    is_charging=True,
    percentage=98.4,
    time_remaining=12,
)
