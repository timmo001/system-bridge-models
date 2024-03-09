"""Test the networks module model."""

from systembridgemodels.fixtures.modules.networks import FIXTURE_NETWORKS
from systembridgemodels.modules.networks import (
    Network,
    NetworkAddress,
    NetworkConnection,
    NetworkIO,
    Networks,
    NetworkStats,
)


def test_networks():
    """Test the networks model."""
    networks = FIXTURE_NETWORKS
    assert isinstance(networks, Networks)
    assert isinstance(networks.connections, list)
    assert isinstance(networks.connections[0], NetworkConnection)
    assert networks.connections[0].fd == 1
    assert networks.connections[0].family == 2
    assert networks.connections[0].type == 3
    assert networks.connections[0].laddr == "laddr"
    assert networks.connections[0].raddr == "raddr"
    assert networks.connections[0].status == "status"
    assert networks.connections[0].pid == 4
    assert isinstance(networks.io, NetworkIO)
    assert networks.io.bytes_sent == 1
    assert networks.io.bytes_recv == 2
    assert networks.io.packets_sent == 3
    assert networks.io.packets_recv == 4
    assert networks.io.errin == 5
    assert networks.io.errout == 6
    assert networks.io.dropin == 7
    assert networks.io.dropout == 8
    assert isinstance(networks.networks, list)
    assert isinstance(networks.networks[0], Network)
    assert networks.networks[0].name == "name"
    assert isinstance(networks.networks[0].addresses, list)
    assert isinstance(networks.networks[0].addresses[0], NetworkAddress)
    assert networks.networks[0].addresses[0].address == "address"
    assert networks.networks[0].addresses[0].netmask == "netmask"
    assert networks.networks[0].addresses[0].broadcast == "broadcast"
    assert networks.networks[0].addresses[0].ptp == "ptp"
    assert isinstance(networks.networks[0].stats, NetworkStats)
    assert networks.networks[0].stats.isup is True
    assert networks.networks[0].stats.duplex == "duplex"
    assert networks.networks[0].stats.speed == 1
    assert networks.networks[0].stats.mtu == 2
    assert isinstance(networks.networks[0].stats.flags, list)
    assert networks.networks[0].stats.flags[0] == "flag1"
    assert networks.networks[0].stats.flags[1] == "flag2"
