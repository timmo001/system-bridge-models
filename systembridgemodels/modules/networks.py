"""Networks."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class NetworkAddress:
    """Network Address."""

    address: str | None = None
    family: str | None = None
    netmask: str | None = None
    broadcast: str | None = None
    ptp: str | None = None


@dataclass
class NetworkStats:
    """Network Stats."""

    isup: bool | None = None
    duplex: str | None = None
    speed: int | None = None
    mtu: int | None = None
    flags: list[str] | None = None


@dataclass
class NetworkConnection:
    """Network Connection."""

    fd: int | None = None
    family: int | None = None
    type: int | None = None
    laddr: str | None = None
    raddr: str | None = None
    status: str | None = None
    pid: int | None = None


@dataclass
class NetworkIO:
    """Network IO."""

    bytes_sent: int | None = None
    bytes_recv: int | None = None
    packets_sent: int | None = None
    packets_recv: int | None = None
    errin: int | None = None
    errout: int | None = None
    dropin: int | None = None
    dropout: int | None = None


@dataclass
class Network:
    """Network."""

    name: str | None = None
    addresses: list[NetworkAddress] | None = None
    stats: NetworkStats | None = None


@dataclass
class Networks:
    """Networks."""

    connections: list[NetworkConnection] | None = None
    io: NetworkIO | None = None
    networks: list[Network] | None = None
