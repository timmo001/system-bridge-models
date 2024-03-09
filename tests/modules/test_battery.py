"""Test the battery module model."""

from systembridgemodels.fixtures.modules.battery import FIXTURE_BATTERY
from systembridgemodels.modules.battery import Battery


def test_battery():
    """Test the battery model."""
    battery = FIXTURE_BATTERY
    assert isinstance(battery, Battery)
    assert battery.is_charging is True
    assert battery.percentage == 98.4
    assert battery.time_remaining == 12
