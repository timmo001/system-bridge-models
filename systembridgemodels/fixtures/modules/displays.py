"""Fixtures for displays module."""
from systembridgemodels.modules.displays import Display, InputSource, PowerMode

FIXTURE_DISPLAYS = [
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
        vcp_supported=True,
        brightness=100,
        contrast=100,
        volume=100,
        power_state=0x01,
        input_source=0x0F,
        sdr_white_level=1,
    ),
    Display(
        id="DISPLAY2",
        name="display_with_enums",
        resolution_horizontal=1920,
        resolution_vertical=1080,
        x=1920,
        y=1080,
        power_state=PowerMode(0x01),
        input_source=InputSource(0x0F),
    )
]
