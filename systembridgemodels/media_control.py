"""Media Control."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any


class MediaAction(Enum):
    """Media Action."""

    play = "PLAY"
    pause = "PAUSE"
    stop = "STOP"
    previous = "PREVIOUS"
    next = "NEXT"
    seek = "SEEK"
    rewind = "REWIND"
    fastforward = "FASTFORWARD"
    shuffle = "SHUFFLE"
    repeat = "REPEAT"
    mute = "MUTE"
    volumedown = "VOLUMEDOWN"
    volumeup = "VOLUMEUP"


@dataclass
class MediaControl:
    """Media Control."""

    action: str  # MediaAction
    value: Any | None = None
