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
class PerCPU:
    """Per CPU."""

    id: int
    frequency: CPUFrequency | None = None
    power: float | None = None
    times: CPUTimes | None = None
    times_percent: CPUTimes | None = None
    usage: float | None = None
    voltage: float | None = None


@dataclass
class CPU:
    """CPU."""

    count: int | None = None
    frequency: CPUFrequency | None = None
    load_average: float | None = None
    per_cpu: list[PerCPU] | None = None
    power: float | None = None
    stats: CPUStats | None = None
    temperature: float | None = None
    times: CPUTimes | None = None
    times_percent: CPUTimes | None = None
    usage: float | None = None
    voltage: float | None = None
