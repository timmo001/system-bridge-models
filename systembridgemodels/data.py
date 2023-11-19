"""Data"""
from __future__ import annotations

from dataclasses import dataclass

from .battery import Battery
from .cpu import Cpu
from .disk import Disk
from .display import Display
from .gpu import Gpu
from .memory import Memory
from .network import Network
from .sensors import Sensors
from .system import System


@dataclass
class Data:
    """Data"""

    battery: Battery
    cpu: Cpu
    disk: Disk
    display: Display
    gpu: Gpu
    memory: Memory
    network: Network
    sensors: Sensors
    system: System
