# generated by datamodel-codegen:
#   filename:  system.json

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class LastUpdated(BaseModel):
    """
    Last updated
    """

    boot_time: float
    fqdn: float
    hostname: float
    ip_address_4: float
    mac_address: float
    platform: float
    platform_version: float
    uptime: float
    uuid: float
    version: float
    version_latest: Optional[float] = None
    version_newer_available: Optional[float] = None


class System(BaseModel):
    """
    System
    """

    id: Optional[str] = Field(None, description="Event ID")
    active_user_id: Optional[float] = None
    active_user_name: Optional[str] = None
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
    version_latest: Optional[str] = None
    version_newer_available: Optional[bool] = None
    last_updated: Optional[LastUpdated] = Field(None, description="Last updated")
