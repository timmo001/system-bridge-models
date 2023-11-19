"""Request"""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Request:
    """Request"""

    event: str
    api_key: str | None = field(default=None, repr=False)
    id: str | None = None
