"""Media directories"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Directory:
    """Directory"""

    key: str
    path: str


@dataclass
class MediaDirectories(list[Directory]):
    """Media directories"""
