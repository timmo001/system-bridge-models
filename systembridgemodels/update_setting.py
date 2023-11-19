"""Update Setting"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class UpdateSetting:
    """Update Setting"""

    setting: str
    value: Any
