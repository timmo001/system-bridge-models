"""Displays."""
from __future__ import annotations

from dataclasses import dataclass
import enum

from ..helpers import filter_unexpected_fields

@enum.unique
class PowerMode(enum.IntEnum):
    """Monitor power modes."""

    #: On.
    on = 0x01
    #: Standby.
    standby = 0x02
    #: Suspend.
    suspend = 0x03
    #: Software power off.
    off_soft = 0x04
    #: Hardware power off.
    off_hard = 0x05


@enum.unique
class InputSource(enum.IntEnum):
    """Monitor input sources."""

    OFF = 0x00
    ANALOG1 = 0x01
    ANALOG2 = 0x02
    DVI1 = 0x03
    DVI2 = 0x04
    COMPOSITE1 = 0x05
    COMPOSITE2 = 0x06
    SVIDEO1 = 0x07
    SVIDEO2 = 0x08
    TUNER1 = 0x09
    TUNER2 = 0x0A
    TUNER3 = 0x0B
    CMPONENT1 = 0x0C
    CMPONENT2 = 0x0D
    CMPONENT3 = 0x0E
    DP1 = 0x0F
    DP2 = 0x10
    HDMI1 = 0x11
    HDMI2 = 0x12


@filter_unexpected_fields
@dataclass(slots=True)
class Display:
    """Display."""

    id: str
    name: str
    resolution_horizontal: int
    resolution_vertical: int
    x: int
    y: int
    width: int | None = None
    height: int | None = None
    is_primary: bool | None = None
    pixel_clock: float | None = None
    refresh_rate: float | None = None
    vcp_supported: bool = False
    brightness: int | None = None
    contrast: int | None = None
    volume: int | None = None
    power_state: PowerMode | int | None = None
    input_source: InputSource | int | None = None
    sdr_white_level: int | None = None
