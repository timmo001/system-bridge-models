"""Media Play."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class MediaPlay:
    """Media Play."""

    url: str
    album: str | None = None
    artist: str | None = None
    autoplay: bool | None = False
    cover: str | None = None
    title: str | None = None
    volume: float | None = 40
