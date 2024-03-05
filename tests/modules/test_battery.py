"""Test the battery model."""

from systembridgemodels.modules.battery import Battery


def test_battery():
    """Test the battery model."""
    battery = Battery(
        is_charging=True,
        percentage=98.4,
        time_remaining=12,
    )
    assert isinstance(battery, Battery)
    assert battery.is_charging is True
    assert battery.percentage == 98.4
    assert battery.time_remaining == 12
