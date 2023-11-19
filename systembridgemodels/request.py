"""Request"""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Request:
    """Request"""

    api_key: str = field(repr=False)
    id: str
    event: str
    data: dict[str, Any]
