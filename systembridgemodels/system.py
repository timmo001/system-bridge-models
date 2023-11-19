"""System"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class System:
    """System"""

    boot_time: float
    fqdn: str
    hostname: str
    ip_address_4: str
    mac_address: str
    platform: str
    platform_version: str
    uptime: float
    uuid: str
    version: str
    active_user_id: float | None = None
    active_user_name: str | None = None
    camera_usage: list[str] | None = None
    pending_reboot: bool | None = None
    version_latest: str | None = None
    version_newer_available: bool | None = None
