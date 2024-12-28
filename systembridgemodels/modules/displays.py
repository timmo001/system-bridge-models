"""Displays."""
from __future__ import annotations

from dataclasses import dataclass

from ..helpers import filter_unexpected_fields


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
    brightness: int | None = None
    contrast: int | None = None
    volume: int | None = None
    power_state: int | None = None
    input_source: int | None = None
    sdr_white_level: int | None = None
