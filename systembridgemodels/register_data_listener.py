"""Register Data Listener"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class RegisterDataListener:
    """Register Data Listener"""

    modules: list[str]
