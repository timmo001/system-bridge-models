"""Data"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .battery import Battery
from .cpu import CPU

# from .disk import Disk
# from .display import Display
# from .media import Media
# from .memory import Memory
# from .network import Network
# from .processes import Processes
# from .system import System


@dataclass
class Data:
    """Data"""

    battery: Battery | None = None
    cpu: CPU | None = None
    # disk: Disk | None = None
    # display: Display | None = None
    # gpu: dict[str, Any] | None = None
    # media: Media | None = None
    # memory: Memory | None = None
    # network: Network | None = None
    # processes: Processes | None = None
    # sensors: dict[str, Any] | None = None
    # system: System | None = None
