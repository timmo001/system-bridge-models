"""Notification."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class Action:
    """Notification Action."""

    command: str
    label: str
    data: dict[str, Any] | None = None


@dataclass
class Audio:
    """Notification Audio."""

    source: str
    volume: float | None = None


@dataclass
class Notification:
    """Notification."""

    title: str
    message: str | None = None
    icon: str | None = None
    image: str | None = None
    actions: list[Action] | None = None
    timeout: float | None = None
    audio: Audio | None = None
