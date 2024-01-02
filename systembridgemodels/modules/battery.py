"""Battery."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Battery:
    """Battery."""

    is_charging: bool | None = None
    percentage: float | None = None
    time_remaining: float | None = None
