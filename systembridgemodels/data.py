"""Data"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .battery import Battery
from .cpu import Cpu
from .disk import Disk
from .display import Display
from .media import Media
from .memory import Memory
from .network import Network
from .processes import Processes
from .system import System


@dataclass
class Data:
    """Data"""

    battery: Battery
    cpu: Cpu
    disk: Disk
    display: Display
    gpu: dict[str, Any]
    media: Media
    memory: Memory
    network: Network
    processes: Processes
    sensors: dict[str, Any]
    system: System
