"""Disk"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Disk:
    """Disk"""

    devices: list
    partitions: list
    io_counters_read_count: int | None = None
    io_counters_write_count: int | None = None
    io_counters_read_bytes: int | None = None
    io_counters_write_bytes: int | None = None
    io_counters_read_time: int | None = None
    io_counters_write_time: int | None = None
