"""Disk"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class DiskIOCounters:
    """Disk IO Counters"""

    read_count: int
    write_count: int
    read_bytes: int
    write_bytes: int
    read_time: int
    write_time: int
    busy_time: int | None = None
    read_merged_count: int | None = None
    write_merged_count: int | None = None


@dataclass
class DiskUsage:
    """Disk Usage"""

    total: int
    used: int
    free: int
    percent: float


@dataclass
class DiskPartition:
    """Disk Partition"""

    device: str
    mount_point: str
    fs_type: str
    options: str
    max_file_size: int
    max_path_length: int
    usage: DiskUsage | None = None


@dataclass
class DiskDevice:
    """Disk Device"""

    name: str
    partitions: list[DiskPartition]
    io_counters: DiskIOCounters | None = None


@dataclass
class Disk:
    """Disk"""

    devices: list[DiskDevice]
    io_counters: DiskIOCounters
