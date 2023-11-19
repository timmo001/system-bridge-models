"""System"""
from __future__ import annotations

from dataclasses import dataclass, field
from uuid import uuid4


def generate_token() -> str:
    """Generate token"""
    return str(uuid4())


@dataclass
class SettingHotkey:
    """Setting Hotkey"""

    name: str
    key: str


@dataclass
class SettingDirectory:
    """Setting Directory"""

    name: str
    path: str


@dataclass
class SettingsAPI:
    """Settings API"""

    token: str = field(default_factory=generate_token)
    port: int = field(default=274343)  # T9 dialer for "bridge"


@dataclass
class SettingsMedia:
    """Settings Media"""

    directories: list[SettingDirectory] = field(default_factory=lambda: [])


@dataclass
class Settings:
    """Settings"""

    api: SettingsAPI = field(default_factory=SettingsAPI)
    autostart: bool = field(default=False)
    keyboard_hotkeys: list[SettingHotkey] = field(default_factory=lambda: [])
    log_level: str = field(default="INFO")
    media: SettingsMedia = field(default_factory=SettingsMedia)
