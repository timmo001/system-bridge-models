"""Data"""
from __future__ import annotations

from dataclasses import dataclass

from .battery import Battery
from .cpu import CPU
from .disk import Disk
from .display import Display
from .gpu import GPU
from .media import Media
from .memory import Memory
from .networks import Networks
from .processes import Processes
from .sensors import Sensors
from .system import System


@dataclass
class Data:
    """Data"""

    battery: Battery | None = None
    cpu: CPU | None = None
    disk: Disk | None = None
    display: list[Display] | None = None
    gpu: list[GPU] | None = None
    media: Media | None = None
    memory: Memory | None = None
    network: Networks | None = None
    processes: Processes | None = None
    sensors: Sensors | None = None
    system: System | None = None
