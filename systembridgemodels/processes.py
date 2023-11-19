"""Processes"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Process:
    """Process"""

    id: float
    name: str
    cpu_usage: float | None = None
    created: float | None = None
    memory_usage: float | None = None
    path: str | None = None
    status: str | None = None
    username: str | None = None
    working_directory: str | None = None


@dataclass
class Processes:
    """Processes"""

    count: float
    processes: list[Process]
