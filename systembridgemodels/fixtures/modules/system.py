"""Fixture for system module."""
from systembridgemodels.modules.system import System, SystemUser

FIXTURE_SYSTEM = System(
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
