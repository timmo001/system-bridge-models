"""Display settings."""
from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum


class DisplaySetting(StrEnum):
    """Display setting field names."""

    BRIGHTNESS = "brightness"
    CONTRAST = "contrast"
    VOLUME = "volume"
    POWER_STATE = "power_state"
    INPUT_SOURCE = "input_source"
    SDR_WHITE_LEVEL = "sdr_white_level"


@dataclass(slots=True)
class DisplayUpdateSettingOp:
    """Set display parameters."""

    monitor_id: int
    setting: DisplaySetting
    value: int
