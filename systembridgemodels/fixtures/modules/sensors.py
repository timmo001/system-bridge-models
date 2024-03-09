"""Fixture for sensors module."""
from systembridgemodels.modules.sensors import (
    Sensors,
    SensorsNVIDIA,
    SensorsNVIDIAChipset,
    SensorsNVIDIADisplay,
    SensorsNVIDIADriver,
    SensorsNVIDIAGPU,
    SensorsWindows,
    SensorsWindowsHardware,
    SensorsWindowsSensor,
)

FIXTURE_SENSORS = Sensors(
    fans=None,
    temperatures=None,
    windows_sensors=SensorsWindows(
        hardware=[
            SensorsWindowsHardware(
                id="id",
                name="name",
                type="type",
                subhardware=[
                    SensorsWindowsHardware(
                        id="id",
                        name="name",
                        type="type",
                        subhardware=[],
                        sensors=[
                            SensorsWindowsSensor(
                                id="id",
                                name="name",
                                type="type",
                                value=12.3,
                            )
                        ],
                    )
                ],
                sensors=[
                    SensorsWindowsSensor(
                        id="id",
                        name="name",
                        type="type",
                        value=12.3,
                    )
                ],
            )
        ],
        nvidia=SensorsNVIDIA(
            chipset=SensorsNVIDIAChipset(
                id=1234,
                name="name",
                flags="flags",
                vendor_id=1234,
                vendor_name="Vendor Name",
            ),
            displays=[
                SensorsNVIDIADisplay(
                    id=1234,
                    name="name",
                    active=True,
                    available=True,
                    connected=True,
                    dynamic=True,
                    aspect_horizontal=16,
                    aspect_vertical=9,
                    brightness_current=90,
                    brightness_default=80,
                    brightness_max=100,
                    brightness_min=0,
                    color_depth="Color Depth",
                    connection_type="Connection Type",
                    pixel_clock=60,
                    refresh_rate=144,
                    resolution_horizontal=1920,
                    resolution_vertical=1080,
                )
            ],
            driver=SensorsNVIDIADriver(
                branch_version="Branch Version",
                interface_version="Interface Version",
                version=1234,
            ),
            gpus=[
                SensorsNVIDIAGPU(
                    id=1234,
                    name="name",
                    bios_oem_revision=1234,
                    bios_revision=1234,
                    bios_version="bios_version",
                    current_fan_speed_level=1234,
                    current_fan_speed_rpm=1234,
                    driver_model=1234,
                    memory_available=1234,
                    memory_capacity=1234,
                    memory_maker="Memory Maker",
                    serial="abc123",
                    system_type="System Type",
                    type="Type",
                )
            ],
        ),
    ),
)
