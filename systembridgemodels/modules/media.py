"""Media."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Media:
    """Media Info."""

    album_artist: str | None = None
    album_title: str | None = None
    artist: str | None = None
    duration: float | None = None
    is_fast_forward_enabled: bool | None = None
    is_next_enabled: bool | None = None
    is_pause_enabled: bool | None = None
    is_play_enabled: bool | None = None
    is_previous_enabled: bool | None = None
    is_rewind_enabled: bool | None = None
    is_stop_enabled: bool | None = None
    playback_rate: float | None = None
    position: float | None = None
    repeat: str | None = None
    shuffle: bool | None = None
    status: str | None = None
    subtitle: str | None = None
    thumbnail: str | None = None
    title: str | None = None
    track_number: int | None = None
    type: str | None = None
    updated_at: float | None = None
