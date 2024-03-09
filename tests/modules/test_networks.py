"""Test the networks module model."""

from dataclasses import asdict

from systembridgemodels.fixtures.modules.networks import FIXTURE_NETWORKS
from systembridgemodels.modules.networks import (
    Network,
    NetworkAddress,
    NetworkConnection,
    NetworkIO,
    Networks,
    NetworkStats,
)


def test_networks(networks: Networks = FIXTURE_NETWORKS):
    """Test the networks model."""
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


def test_networks_dict():
    """Test the networks model to dict."""
    networks_dict = asdict(FIXTURE_NETWORKS)
    assert isinstance(networks_dict, dict)
    assert isinstance(networks_dict["connections"], list)
    assert isinstance(networks_dict["connections"][0], dict)
    assert networks_dict["connections"][0]["fd"] == 1
    assert networks_dict["connections"][0]["family"] == 2
    assert networks_dict["connections"][0]["type"] == 3
    assert networks_dict["connections"][0]["laddr"] == "laddr"
    assert networks_dict["connections"][0]["raddr"] == "raddr"
    assert networks_dict["connections"][0]["status"] == "status"
    assert networks_dict["connections"][0]["pid"] == 4
    assert isinstance(networks_dict["io"], dict)
    assert networks_dict["io"]["bytes_sent"] == 1
    assert networks_dict["io"]["bytes_recv"] == 2
    assert networks_dict["io"]["packets_sent"] == 3
    assert networks_dict["io"]["packets_recv"] == 4
    assert networks_dict["io"]["errin"] == 5
    assert networks_dict["io"]["errout"] == 6
    assert networks_dict["io"]["dropin"] == 7
    assert networks_dict["io"]["dropout"] == 8
    assert isinstance(networks_dict["networks"], list)
    assert isinstance(networks_dict["networks"][0], dict)
    assert networks_dict["networks"][0]["name"] == "name"
    assert isinstance(networks_dict["networks"][0]["addresses"], list)
    assert isinstance(networks_dict["networks"][0]["addresses"][0], dict)
    assert networks_dict["networks"][0]["addresses"][0]["address"] == "address"
    assert networks_dict["networks"][0]["addresses"][0]["netmask"] == "netmask"
    assert networks_dict["networks"][0]["addresses"][0]["broadcast"] == "broadcast"
    assert networks_dict["networks"][0]["addresses"][0]["ptp"] == "ptp"
    assert isinstance(networks_dict["networks"][0]["stats"], dict)
    assert networks_dict["networks"][0]["stats"]["isup"] is True
    assert networks_dict["networks"][0]["stats"]["duplex"] == "duplex"
    assert networks_dict["networks"][0]["stats"]["speed"] == 1
    assert networks_dict["networks"][0]["stats"]["mtu"] == 2
    assert isinstance(networks_dict["networks"][0]["stats"]["flags"], list)
    assert networks_dict["networks"][0]["stats"]["flags"][0] == "flag1"
    assert networks_dict["networks"][0]["stats"]["flags"][1] == "flag2"

    networks_converted = Networks(**networks_dict)
    test_networks(networks_converted)
