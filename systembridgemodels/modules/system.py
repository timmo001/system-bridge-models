"""System."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class SystemUser:
    """System User."""

    name: str
    active: bool
    terminal: str
    host: str
    started: float
    pid: float


@dataclass
class System:
    """System."""

    boot_time: float
    fqdn: str
    hostname: str
    ip_address_4: str
    mac_address: str
    platform_version: str
    platform: str
    uptime: float
    users: list[SystemUser]
    uuid: str
    version: str
    camera_usage: list[str] | None = None
    ip_address_6: str | None = None
    pending_reboot: bool | None = None
    version_latest: str | None = None
    version_newer_available: bool | None = None
