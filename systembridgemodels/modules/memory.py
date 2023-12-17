"""Memory."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class MemorySwap:
    """Memory Swap."""

    total: int | None = None
    used: int | None = None
    free: float | None = None
    percent: float | None = None
    sin: int | None = None
    sout: int | None = None


@dataclass
class MemoryVirtual:
    """Memory Virtual."""

    total: int | None = None
    available: int | None = None
    percent: float | None = None
    used: int | None = None
    free: int | None = None
    active: int | None = None
    inactive: int | None = None
    buffers: int | None = None
    cached: int | None = None
    wired: int | None = None
    shared: int | None = None


@dataclass
class Memory:
    """Memory."""

    swap: MemorySwap
    virtual: MemoryVirtual
