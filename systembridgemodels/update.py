"""Update."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Update:
    """Update."""

    version: str
