"""Media Get Files."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class MediaGetFiles:
    """Media Get Files."""

    base: str
    path: str | None = None
