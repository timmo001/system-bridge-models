"""System"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class SensorsWindowsSensor:
    """Sensors Windows Sensor"""

    id: str
    name: str
    type: str
    value: float | int | str | None = None


@dataclass
class SensorsWindowsHardware:
    """Sensors Windows Hardware"""

    id: str
    name: str
    type: str
    subhardware: list[SensorsWindowsHardware]
    sensors: list[SensorsWindowsSensor]


@dataclass
class SensorsWindows:
    """Sensors Windows"""

    hardware: list[SensorsWindowsHardware] | None = None
    nvidia: Any | None = None


@dataclass
class Sensors:
    """Sensors"""

    fans: Any | None = None
    temperatures: Any | None = None
    windows_sensors: SensorsWindows | None = None
