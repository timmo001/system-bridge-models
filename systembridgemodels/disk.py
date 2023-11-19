# generated by datamodel-codegen:
#   filename:  disk.json

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class LastUpdated:
    """
    Last updated
    """

    devices: float
    partitions: float
    io_counters_read_count: float | None = None
    io_counters_write_count: float | None = None
    io_counters_read_bytes: float | None = None
    io_counters_write_bytes: float | None = None
    io_counters_read_time: float | None = None
    io_counters_write_time: float | None = None


@dataclass
class Disk:
    """
    Disk
    """

    devices: list
    partitions: list
    id: str | None = None
    io_counters_read_count: int | None = None
    io_counters_write_count: int | None = None
    io_counters_read_bytes: int | None = None
    io_counters_write_bytes: int | None = None
    io_counters_read_time: int | None = None
    io_counters_write_time: int | None = None
    last_updated: LastUpdated | None = None
