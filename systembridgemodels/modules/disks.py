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

    def __post_init__(self) -> None:
        """Post Init."""
        if isinstance(self.devices, list) and all(
            isinstance(item, dict) for item in self.devices
        ):
            self.devices = [
                Disk(
                    name=device.name,
                    partitions=[
                        DiskPartition(
                            device=partition.device,
                            mount_point=partition.mount_point,
                            filesystem_type=partition.filesystem_type,
                            options=partition.options,
                            max_file_size=partition.max_file_size,
                            max_path_length=partition.max_path_length,
                            usage=DiskUsage(
                                total=partition.usage.total,
                                used=partition.usage.used,
                                free=partition.usage.free,
                                percent=partition.usage.percent,
                            )
                            if partition.usage
                            else None,
                        )
                        for partition in device.partitions
                    ],
                    io_counters=DiskIOCounters(
                        read_count=device.io_counters.read_count,
                        write_count=device.io_counters.write_count,
                        read_bytes=device.io_counters.read_bytes,
                        write_bytes=device.io_counters.write_bytes,
                        read_time=device.io_counters.read_time,
                        write_time=device.io_counters.write_time,
                    )
                    if device.io_counters
                    else None,
                )
                for device in self.devices
            ]
