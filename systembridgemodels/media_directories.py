"""Media directories."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class MediaDirectory:
    """Directory."""

    key: str
    path: str
