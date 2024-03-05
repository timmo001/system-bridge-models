"""Test the networks model."""

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


def test_networks():
    """Test the sensors model."""
    sensors = Sensors(
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
    assert isinstance(sensors, Sensors)

    assert sensors.fans is None

    assert sensors.temperatures is None

    assert sensors.windows_sensors is not None
    assert isinstance(sensors.windows_sensors, SensorsWindows)
    assert isinstance(sensors.windows_sensors.hardware, list)
    assert isinstance(sensors.windows_sensors.hardware[0], SensorsWindowsHardware)
    assert sensors.windows_sensors.hardware[0].id == "id"
    assert sensors.windows_sensors.hardware[0].name == "name"
    assert sensors.windows_sensors.hardware[0].type == "type"
    assert isinstance(sensors.windows_sensors.hardware[0].subhardware, list)
    assert isinstance(
        sensors.windows_sensors.hardware[0].subhardware[0], SensorsWindowsHardware
    )
    assert sensors.windows_sensors.hardware[0].subhardware[0].id == "id"
    assert sensors.windows_sensors.hardware[0].subhardware[0].name == "name"
    assert sensors.windows_sensors.hardware[0].subhardware[0].type == "type"
    assert isinstance(
        sensors.windows_sensors.hardware[0].subhardware[0].subhardware, list
    )
    assert isinstance(sensors.windows_sensors.hardware[0].subhardware[0].sensors, list)
    assert isinstance(
        sensors.windows_sensors.hardware[0].subhardware[0].sensors[0],
        SensorsWindowsSensor,
    )
    assert sensors.windows_sensors.hardware[0].subhardware[0].sensors[0].id == "id"
    assert sensors.windows_sensors.hardware[0].subhardware[0].sensors[0].name == "name"
    assert sensors.windows_sensors.hardware[0].subhardware[0].sensors[0].type == "type"
    assert sensors.windows_sensors.hardware[0].subhardware[0].sensors[0].value == 12.3
    assert isinstance(sensors.windows_sensors.hardware[0].sensors, list)
    assert isinstance(
        sensors.windows_sensors.hardware[0].sensors[0], SensorsWindowsSensor
    )
    assert sensors.windows_sensors.hardware[0].sensors[0].id == "id"
    assert sensors.windows_sensors.hardware[0].sensors[0].name == "name"
    assert sensors.windows_sensors.hardware[0].sensors[0].type == "type"
    assert sensors.windows_sensors.hardware[0].sensors[0].value == 12.3
    assert sensors.windows_sensors.nvidia is not None
    assert isinstance(sensors.windows_sensors.nvidia, SensorsNVIDIA)
    assert isinstance(sensors.windows_sensors.nvidia.chipset, SensorsNVIDIAChipset)
    assert sensors.windows_sensors.nvidia.chipset.id == 1234
    assert sensors.windows_sensors.nvidia.chipset.name == "name"
    assert sensors.windows_sensors.nvidia.chipset.flags == "flags"
    assert sensors.windows_sensors.nvidia.chipset.vendor_id == 1234
    assert sensors.windows_sensors.nvidia.chipset.vendor_name == "Vendor Name"
    assert isinstance(sensors.windows_sensors.nvidia.displays, list)
    assert isinstance(sensors.windows_sensors.nvidia.displays[0], SensorsNVIDIADisplay)
    assert sensors.windows_sensors.nvidia.displays[0].id == 1234
    assert sensors.windows_sensors.nvidia.displays[0].name == "name"
    assert sensors.windows_sensors.nvidia.displays[0].active is True
    assert sensors.windows_sensors.nvidia.displays[0].available is True
    assert sensors.windows_sensors.nvidia.displays[0].connected is True
    assert sensors.windows_sensors.nvidia.displays[0].dynamic is True
    assert sensors.windows_sensors.nvidia.displays[0].aspect_horizontal == 16
    assert sensors.windows_sensors.nvidia.displays[0].aspect_vertical == 9
    assert sensors.windows_sensors.nvidia.displays[0].brightness_current == 90
    assert sensors.windows_sensors.nvidia.displays[0].brightness_default == 80
    assert sensors.windows_sensors.nvidia.displays[0].brightness_max == 100
    assert sensors.windows_sensors.nvidia.displays[0].brightness_min == 0
    assert sensors.windows_sensors.nvidia.displays[0].color_depth == "Color Depth"
    assert (
        sensors.windows_sensors.nvidia.displays[0].connection_type == "Connection Type"
    )
    assert sensors.windows_sensors.nvidia.displays[0].pixel_clock == 60
    assert sensors.windows_sensors.nvidia.displays[0].refresh_rate == 144
    assert sensors.windows_sensors.nvidia.displays[0].resolution_horizontal == 1920
    assert sensors.windows_sensors.nvidia.displays[0].resolution_vertical == 1080
    assert isinstance(sensors.windows_sensors.nvidia.driver, SensorsNVIDIADriver)
    assert sensors.windows_sensors.nvidia.driver.branch_version == "Branch Version"
    assert (
        sensors.windows_sensors.nvidia.driver.interface_version == "Interface Version"
    )
    assert sensors.windows_sensors.nvidia.driver.version == 1234
    assert isinstance(sensors.windows_sensors.nvidia.gpus, list)
    assert isinstance(sensors.windows_sensors.nvidia.gpus[0], SensorsNVIDIAGPU)
    assert sensors.windows_sensors.nvidia.gpus[0].id == 1234
    assert sensors.windows_sensors.nvidia.gpus[0].name == "name"
    assert sensors.windows_sensors.nvidia.gpus[0].bios_oem_revision == 1234
    assert sensors.windows_sensors.nvidia.gpus[0].bios_revision == 1234
    assert sensors.windows_sensors.nvidia.gpus[0].bios_version == "bios_version"
    assert sensors.windows_sensors.nvidia.gpus[0].current_fan_speed_level == 1234
    assert sensors.windows_sensors.nvidia.gpus[0].current_fan_speed_rpm == 1234
    assert sensors.windows_sensors.nvidia.gpus[0].driver_model == 1234
    assert sensors.windows_sensors.nvidia.gpus[0].memory_available == 1234
    assert sensors.windows_sensors.nvidia.gpus[0].memory_capacity == 1234
    assert sensors.windows_sensors.nvidia.gpus[0].memory_maker == "Memory Maker"
    assert sensors.windows_sensors.nvidia.gpus[0].serial == "abc123"
    assert sensors.windows_sensors.nvidia.gpus[0].system_type == "System Type"
    assert sensors.windows_sensors.nvidia.gpus[0].type == "Type"
