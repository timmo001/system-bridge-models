"""CPU"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CPU:
    """CPU"""

    count: int | None = None
    frequency_current: float | None = None
    frequency_min: float | None = None
    frequency_max: float | None = None
    load_average: float | None = None
    power_package: float | None = None
    stats_ctx_switches: int | None = None
    stats_interrupts: int | None = None
    stats_soft_interrupts: int | None = None
    stats_syscalls: int | None = None
    temperature: float | None = None
    times_user: float | None = None
    times_system: float | None = None
    times_idle: float | None = None
    times_interrupt: float | None = None
    times_dpc: float | None = None
    times_percent_user: float | None = None
    times_percent_system: float | None = None
    times_percent_idle: float | None = None
    times_percent_interrupt: float | None = None
    times_percent_dpc: float | None = None
    usage: float | None = None
    voltage: float | None = None
