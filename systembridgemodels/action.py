"""Action."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class Action:
    """Action."""

    command: str
    data: dict[str, Any] | None = None
    label: str | None = None
