"""System"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from uuid import uuid4


def generate_token() -> str:
    """Generate token"""
    return str(uuid4())


class SettingAPIEnum(Enum):
    """Setting API Enum"""

    Token = "token"
    Port = "port"


class SettingHotkeyEnum(Enum):
    """Setting Hotkey Enum"""

    Name = "name"
    Key = "key"


class SettingDirectoryEnum(Enum):
    """Setting Media Directory Enum"""

    Name = "name"
    Path = "path"


class SettingMediaEnum(Enum):
    """Setting Media Enum"""

    Directories = "directories"


class SettingEnum(Enum):
    """Setting Enum"""

    API = "api"
    Autostart = "autostart"
    KeyboardHotkeys = "keyboard_hotkeys"
    LogLevel = "log_level"
    Media = "media"


@dataclass
class SettingsAPI:
    """Settings API"""

    token: str = field(default_factory=generate_token)
    port: int = field(default=9174)


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
