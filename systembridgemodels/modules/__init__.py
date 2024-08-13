"""Modules."""

from __future__ import annotations

from dataclasses import dataclass, fields
from enum import StrEnum

from .battery import Battery
from .cpu import CPU
from .disks import Disks
from .displays import Display
from .gpus import GPU
from .media import Media
from .memory import Memory
from .networks import Networks
from .processes import Process
from .sensors import Sensors
from .system import System


class Module(StrEnum):
    """Module Enum."""

    BATTERY = "battery"
    CPU = "cpu"
    DISKS = "disks"
    DISPLAYS = "displays"
    GPUS = "gpus"
    MEDIA = "media"
    MEMORY = "memory"
    NETWORKS = "networks"
    PROCESSES = "processes"
    SENSORS = "sensors"
    SYSTEM = "system"


def filter_unexpected_fields(cls):
    """Filter unexpected fields from a dataclass.

    Useful when using **kwargs in __init__.
    """
    original_init = cls.__init__

    def new_init(self, *args, **kwargs):
        expected_fields = {field.name for field in fields(cls)}
        cleaned_kwargs = {
            key: value for key, value in kwargs.items() if key in expected_fields
        }
        original_init(self, *args, **cleaned_kwargs)

    cls.__init__ = new_init
    return cls


@dataclass(slots=True)
class GetData:
    """Get Data."""

    modules: list[Module]


@dataclass(slots=True)
class RegisterDataListener(GetData):
    """Register Data Listener."""


@dataclass
class ModulesData:
    """Data."""

    battery: Battery | None = None
    cpu: CPU | None = None
    disks: Disks | None = None
    displays: list[Display] | None = None
    gpus: list[GPU] | None = None
    media: Media | None = None
    memory: Memory | None = None
    networks: Networks | None = None
    processes: list[Process] | None = None
    sensors: Sensors | None = None
    system: System | None = None
