"""Media Files."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class MediaFile:
    """Media File."""

    name: str
    path: str
    fullpath: str
    size: int
    last_accessed: float
    created: float
    modified: float
    is_directory: bool
    is_file: bool
    is_link: bool
    mime_type: str | None = None


@dataclass
class MediaFiles:
    """Media Files."""

    files: list[MediaFile]
    path: str
