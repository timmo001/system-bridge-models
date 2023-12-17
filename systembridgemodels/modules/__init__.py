"""Modules."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from .battery import Battery
from .cpu import CPU
from .disks import Disks
from .displays import Displays
from .gpus import GPUs
from .media import Media
from .memory import Memory
from .networks import Networks
from .processes import Processes
from .sensors import Sensors
from .system import System


class DataEnum(Enum):
    """Data Enum."""

    BATTERY = "battery"
    CPU = "cpu"
    DISKS = "disks"
    DISPLAYS = "displays"
    GPUS = "gpus"
    MEDIA = "media"
    MEMORY = "memory"
    NETWORKS = "networks"
    PROCESSES = "processes"
    SENSORS = "sensor"
    SYSTEM = "system"


@dataclass
class GetData:
    """Get Data."""

    modules: list[str]


@dataclass
class RegisterDataListener(GetData):
    """Register Data Listener."""


@dataclass
class ModulesData:
    """Data."""

    battery: Battery | None = None
    cpu: CPU | None = None
    disks: Disks | None = None
    displays: Displays | None = None
    gpus: GPUs | None = None
    media: Media | None = None
    memory: Memory | None = None
    networks: Networks | None = None
    processes: Processes | None = None
    sensors: Sensors | None = None
    system: System | None = None
