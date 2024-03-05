"""Test the displays model."""

from systembridgemodels.modules.displays import Display


def test_displays():
    """Test the displays model."""
    displays = [
        Display(
            id="abc123",
            name="name",
            resolution_horizontal=1920,
            resolution_vertical=1080,
            x=1920,
            y=1080,
            width=1920,
            height=1080,
            is_primary=True,
            pixel_clock=60.0,
            refresh_rate=60.0,
        )
    ]
    assert isinstance(displays, list)
    assert isinstance(displays[0], Display)
    assert displays[0].id == "abc123"
    assert displays[0].name == "name"
    assert displays[0].resolution_horizontal == 1920
    assert displays[0].resolution_vertical == 1080
    assert displays[0].x == 1920
    assert displays[0].y == 1080
    assert displays[0].width == 1920
    assert displays[0].height == 1080
    assert displays[0].is_primary is True
    assert displays[0].pixel_clock == 60.0
    assert displays[0].refresh_rate == 60.0
