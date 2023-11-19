"""Memory"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Memory:
    """Memory"""

    swap_total: int | None = None
    swap_used: int | None = None
    swap_free: float | None = None
    swap_percent: float | None = None
    swap_sin: int | None = None
    swap_sout: int | None = None
    virtual_total: int | None = None
    virtual_available: int | None = None
    virtual_percent: float | None = None
    virtual_used: int | None = None
    virtual_free: int | None = None
