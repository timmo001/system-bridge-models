"""CPU."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CPUFrequency:
    """CPU Frequency."""

    current: float | None = None
    min: float | None = None
    max: float | None = None


@dataclass
class CPUStats:
    """CPU Stats."""

    ctx_switches: int | None = None
    interrupts: int | None = None
    soft_interrupts: int | None = None
    syscalls: int | None = None


@dataclass
class CPUTimes:
    """CPU Times."""

    user: float | None = None
    system: float | None = None
    idle: float | None = None
    interrupt: float | None = None
    dpc: float | None = None


@dataclass
class CPU:
    """CPU."""

    count: int | None = None
    frequency: CPUFrequency | None = None
    frequency_per_cpu: list[CPUFrequency] | None = None
    load_average: float | None = None
    power_package: float | None = None
    power_per_cpu: list[float] | None = None
    stats: CPUStats | None = None
    temperature: float | None = None
    times: CPUTimes | None = None
    times_per_cpu: list[CPUTimes] | None = None
    times_percent: CPUTimes | None = None
    times_percent_per_cpu: list[CPUTimes] | None = None
    usage: float | None = None
    usage_per_cpu: list[float] | None = None
    voltage: float | None = None
