"""System."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class SensorsWindowsSensor:
    """Sensors Windows Sensor."""

    id: str
    name: str
    type: str
    value: float | int | str | None = None


@dataclass
class SensorsWindowsHardware:
    """Sensors Windows Hardware."""

    id: str
    name: str
    type: str
    subhardware: list[SensorsWindowsHardware]
    sensors: list[SensorsWindowsSensor]

@dataclass
class Chipset:
    id: int
    name: str
    flags: str
    vendor_id: int
    vendor_name: str


@dataclass
class Display:
    id: int
    name: str
    active: bool
    available: bool
    connected: bool
    dynamic: bool
    aspect_horizontal: int
    aspect_vertical: int
    brightness_current: int
    brightness_default: int
    brightness_max: int
    brightness_min: int
    color_depth: str
    connection_type: str
    pixel_clock: int
    refresh_rate: int
    resolution_horizontal: int
    resolution_vertical: int


@dataclass
class Driver:
    branch_version: str
    interface_version: str
    version: int


@dataclass
class Gpus:
    id: int
    name: str
    bios_oem_revision: int
    bios_revision: int
    bios_version: str
    current_fan_speed_level: int
    current_fan_speed_rpm: int
    driver_model: int
    memory_available: int
    memory_capacity: int
    memory_maker: str
    serial: str
    system_type: str
    type: str


@dataclass
class SensorsNVIDIA:
    chipset: Chipset
    displays: list[Display]
    driver: Driver
    gpus: list[Gpus]

@dataclass
class SensorsWindows:
    """Sensors Windows."""

    hardware: list[SensorsWindowsHardware] | None = None
    nvidia: SensorsNVIDIA | None = None


@dataclass
class Sensors:
    """Sensors."""

    # TODO: Add fan model
    fans: Any | None = None
    # TODO: Add temperatures model
    temperatures: Any | None = None
    windows_sensors: SensorsWindows | None = None
