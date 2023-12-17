"""Disks."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class DiskIOCounters:
    """Disk IO Counters."""

    read_count: int
    write_count: int
    read_bytes: int
    write_bytes: int
    read_time: int
    write_time: int


@dataclass
class DiskUsage:
    """Disk Usage."""

    total: int
    used: int
    free: int
    percent: float


@dataclass
class DiskPartition:
    """Disk Partition."""

    device: str
    mount_point: str
    filesystem_type: str
    options: str
    max_file_size: int
    max_path_length: int
    usage: DiskUsage | None = None


@dataclass
class Disk:
    """Disk."""

    name: str
    partitions: list[DiskPartition]
    io_counters: DiskIOCounters | None = None


@dataclass
class Disks:
    """Disks."""

    devices: list[Disk]
    io_counters: DiskIOCounters | None = None
