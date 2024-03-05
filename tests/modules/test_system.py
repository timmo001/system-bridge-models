"""Test the networks model."""

from systembridgemodels.modules.system import System, SystemUser


def test_networks():
    """Test the system model."""
    system = System(
        boot_time=1234,
        fqdn="hostname.local",
        hostname="hostname",
        ip_address_4="192.168.1.100",
        mac_address="00:00:00:00:00:00",
        platform_version="1.0.0",
        platform="platform",
        uptime=1234,
        users=[
            SystemUser(
                name="username",
                active=True,
                terminal="terminal",
                host="host",
                started=1234,
                pid=1234,
            )
        ],
        uuid="uuid",
        version="1.0.0",
        camera_usage=[
            "camera1",
            "camera2",
        ],
        ip_address_6="::1",
        pending_reboot=True,
        version_latest="4.99.0",
        version_newer_available=True,
    )
    assert isinstance(system, System)
    assert system.boot_time == 1234
    assert system.fqdn == "hostname.local"
    assert system.hostname == "hostname"
    assert system.ip_address_4 == "192.168.1.100"
    assert system.mac_address == "00:00:00:00:00:00"
    assert system.platform_version == "1.0.0"
    assert system.platform == "platform"
    assert system.uptime == 1234
    assert isinstance(system.users, list)
    assert isinstance(system.users[0], SystemUser)
    assert system.users[0].name == "username"
    assert system.users[0].active is True
    assert system.users[0].terminal == "terminal"
    assert system.users[0].host == "host"
    assert system.users[0].started == 1234
    assert system.users[0].pid == 1234
    assert system.uuid == "uuid"
    assert system.version == "1.0.0"
    assert isinstance(system.camera_usage, list)
    assert system.camera_usage[0] == "camera1"
    assert system.camera_usage[1] == "camera2"
    assert system.ip_address_6 == "::1"
    assert system.pending_reboot is True
    assert system.version_latest == "4.99.0"
    assert system.version_newer_available is True
