"""Disks."""
from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import cast


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

    def __post_init__(self) -> None:
        """Post Init."""
        if isinstance(self.partitions, list) and all(
            isinstance(item, dict) for item in self.partitions
        ):
            new_partitions: list[DiskPartition] = []
            for p in self.partitions:
                partition: dict = cast(dict, p)
                usage = partition.get("usage")
                new_partitions.append(
                    DiskPartition(
                        device=partition["device"],
                        mount_point=partition["mount_point"],
                        filesystem_type=partition["filesystem_type"],
                        options=partition["options"],
                        max_file_size=partition["max_file_size"],
                        max_path_length=partition["max_path_length"],
                        usage=(DiskUsage(**usage) if usage else None),
                    )
                )
            self.partitions = new_partitions


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
            new_devices: list[Disk] = []
            for d in self.devices:
                device: dict = cast(dict, d)
                partitions: list[DiskPartition] = []
                for partition in device.get("partitions", []):
                    partitions.append(DiskPartition(**partition))
                io_counters = device.get("io_counters")
                new_devices.append(
                    Disk(
                        name=device["name"],
                        partitions=partitions,
                        io_counters=(
                            DiskIOCounters(**io_counters) if io_counters else None
                        ),
                    )
                )
            self.devices = new_devices
