"""Network"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Network:
    """Network"""

    io_counters_bytes_sent: int | None = None
    io_counters_bytes_recv: int | None = None
    io_counters_packets_sent: int | None = None
    io_counters_packets_recv: int | None = None
    io_counters_errin: int | None = None
    io_counters_errout: int | None = None
    io_counters_dropin: int | None = None
    io_counters_dropout: int | None = None
