"""Displays."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Display:
    """Display."""

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


type Displays = list[Display]
