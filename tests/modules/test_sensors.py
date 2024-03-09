"""Test the sensors module model."""

from dataclasses import asdict

from systembridgemodels.fixtures.modules.sensors import FIXTURE_SENSORS
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


def test_sensors(sensors: Sensors = FIXTURE_SENSORS):
    """Test the sensors model."""
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


def test_sensors_dict():
    """Test the sensors model to dict."""
    sensors_dict = asdict(FIXTURE_SENSORS)
    assert isinstance(sensors_dict, dict)

    assert sensors_dict["fans"] is None

    assert sensors_dict["temperatures"] is None

    assert sensors_dict["windows_sensors"] is not None
    assert isinstance(sensors_dict["windows_sensors"], dict)
    assert isinstance(sensors_dict["windows_sensors"]["hardware"], list)
    assert isinstance(sensors_dict["windows_sensors"]["hardware"][0], dict)
    assert sensors_dict["windows_sensors"]["hardware"][0]["id"] == "id"
    assert sensors_dict["windows_sensors"]["hardware"][0]["name"] == "name"
    assert sensors_dict["windows_sensors"]["hardware"][0]["type"] == "type"
    assert isinstance(
        sensors_dict["windows_sensors"]["hardware"][0]["subhardware"], list
    )
    assert isinstance(
        sensors_dict["windows_sensors"]["hardware"][0]["subhardware"][0], dict
    )
    assert (
        sensors_dict["windows_sensors"]["hardware"][0]["subhardware"][0]["id"] == "id"
    )
    assert (
        sensors_dict["windows_sensors"]["hardware"][0]["subhardware"][0]["name"]
        == "name"
    )
    assert (
        sensors_dict["windows_sensors"]["hardware"][0]["subhardware"][0]["type"]
        == "type"
    )
    assert isinstance(
        sensors_dict["windows_sensors"]["hardware"][0]["subhardware"][0]["subhardware"],
        list,
    )
    assert isinstance(
        sensors_dict["windows_sensors"]["hardware"][0]["subhardware"][0]["sensors"],
        list,
    )
    assert isinstance(
        sensors_dict["windows_sensors"]["hardware"][0]["subhardware"][0]["sensors"][0],
        dict,
    )
    assert (
        sensors_dict["windows_sensors"]["hardware"][0]["subhardware"][0]["sensors"][0][
            "id"
        ]
        == "id"
    )
    assert (
        sensors_dict["windows_sensors"]["hardware"][0]["subhardware"][0]["sensors"][0][
            "name"
        ]
        == "name"
    )
    assert (
        sensors_dict["windows_sensors"]["hardware"][0]["subhardware"][0]["sensors"][0][
            "type"
        ]
        == "type"
    )
    assert (
        sensors_dict["windows_sensors"]["hardware"][0]["subhardware"][0]["sensors"][0][
            "value"
        ]
        == 12.3
    )
    assert isinstance(sensors_dict["windows_sensors"]["hardware"][0]["sensors"], list)
    assert isinstance(
        sensors_dict["windows_sensors"]["hardware"][0]["sensors"][0], dict
    )
    assert sensors_dict["windows_sensors"]["hardware"][0]["sensors"][0]["id"] == "id"
    assert (
        sensors_dict["windows_sensors"]["hardware"][0]["sensors"][0]["name"] == "name"
    )
    assert (
        sensors_dict["windows_sensors"]["hardware"][0]["sensors"][0]["type"] == "type"
    )
    assert sensors_dict["windows_sensors"]["hardware"][0]["sensors"][0]["value"] == 12.3
    assert sensors_dict["windows_sensors"]["nvidia"] is not None
    assert isinstance(sensors_dict["windows_sensors"]["nvidia"], dict)
    assert isinstance(sensors_dict["windows_sensors"]["nvidia"]["chipset"], dict)
    assert sensors_dict["windows_sensors"]["nvidia"]["chipset"]["id"] == 1234
    assert sensors_dict["windows_sensors"]["nvidia"]["chipset"]["name"] == "name"
    assert sensors_dict["windows_sensors"]["nvidia"]["chipset"]["flags"] == "flags"
    assert sensors_dict["windows_sensors"]["nvidia"]["chipset"]["vendor_id"] == 1234
    assert (
        sensors_dict["windows_sensors"]["nvidia"]["chipset"]["vendor_name"]
        == "Vendor Name"
    )
    assert isinstance(sensors_dict["windows_sensors"]["nvidia"]["displays"], list)
    assert isinstance(sensors_dict["windows_sensors"]["nvidia"]["displays"][0], dict)
    assert sensors_dict["windows_sensors"]["nvidia"]["displays"][0]["id"] == 1234
    assert sensors_dict["windows_sensors"]["nvidia"]["displays"][0]["name"] == "name"
    assert sensors_dict["windows_sensors"]["nvidia"]["displays"][0]["active"] is True
    assert sensors_dict["windows_sensors"]["nvidia"]["displays"][0]["available"] is True
    assert sensors_dict["windows_sensors"]["nvidia"]["displays"][0]["connected"] is True
    assert sensors_dict["windows_sensors"]["nvidia"]["displays"][0]["dynamic"] is True
    assert (
        sensors_dict["windows_sensors"]["nvidia"]["displays"][0]["aspect_horizontal"]
        == 16
    )
    assert (
        sensors_dict["windows_sensors"]["nvidia"]["displays"][0]["aspect_vertical"] == 9
    )
    assert (
        sensors_dict["windows_sensors"]["nvidia"]["displays"][0]["brightness_current"]
        == 90
    )
    assert (
        sensors_dict["windows_sensors"]["nvidia"]["displays"][0]["brightness_default"]
        == 80
    )
    assert (
        sensors_dict["windows_sensors"]["nvidia"]["displays"][0]["brightness_max"]
        == 100
    )
    assert (
        sensors_dict["windows_sensors"]["nvidia"]["displays"][0]["brightness_min"] == 0
    )
    assert (
        sensors_dict["windows_sensors"]["nvidia"]["displays"][0]["color_depth"]
        == "Color Depth"
    )
    assert (
        sensors_dict["windows_sensors"]["nvidia"]["displays"][0]["connection_type"]
        == "Connection Type"
    )
    assert sensors_dict["windows_sensors"]["nvidia"]["displays"][0]["pixel_clock"] == 60
    assert (
        sensors_dict["windows_sensors"]["nvidia"]["displays"][0]["refresh_rate"] == 144
    )
    assert (
        sensors_dict["windows_sensors"]["nvidia"]["displays"][0][
            "resolution_horizontal"
        ]
        == 1920
    )
    assert (
        sensors_dict["windows_sensors"]["nvidia"]["displays"][0]["resolution_vertical"]
        == 1080
    )
    assert isinstance(sensors_dict["windows_sensors"]["nvidia"]["driver"], dict)
    assert (
        sensors_dict["windows_sensors"]["nvidia"]["driver"]["branch_version"]
        == "Branch Version"
    )
    assert (
        sensors_dict["windows_sensors"]["nvidia"]["driver"]["interface_version"]
        == "Interface Version"
    )
    assert sensors_dict["windows_sensors"]["nvidia"]["driver"]["version"] == 1234
    assert isinstance(sensors_dict["windows_sensors"]["nvidia"]["gpus"], list)
    assert isinstance(sensors_dict["windows_sensors"]["nvidia"]["gpus"][0], dict)
    assert sensors_dict["windows_sensors"]["nvidia"]["gpus"][0]["id"] == 1234
    assert sensors_dict["windows_sensors"]["nvidia"]["gpus"][0]["name"] == "name"
    assert (
        sensors_dict["windows_sensors"]["nvidia"]["gpus"][0]["bios_oem_revision"]
        == 1234
    )
    assert sensors_dict["windows_sensors"]["nvidia"]["gpus"][0]["bios_revision"] == 1234
    assert (
        sensors_dict["windows_sensors"]["nvidia"]["gpus"][0]["bios_version"]
        == "bios_version"
    )
    assert (
        sensors_dict["windows_sensors"]["nvidia"]["gpus"][0]["current_fan_speed_level"]
        == 1234
    )
    assert (
        sensors_dict["windows_sensors"]["nvidia"]["gpus"][0]["current_fan_speed_rpm"]
        == 1234
    )
    assert sensors_dict["windows_sensors"]["nvidia"]["gpus"][0]["driver_model"] == 1234
    assert (
        sensors_dict["windows_sensors"]["nvidia"]["gpus"][0]["memory_available"] == 1234
    )
    assert (
        sensors_dict["windows_sensors"]["nvidia"]["gpus"][0]["memory_capacity"] == 1234
    )
    assert (
        sensors_dict["windows_sensors"]["nvidia"]["gpus"][0]["memory_maker"]
        == "Memory Maker"
    )
    assert sensors_dict["windows_sensors"]["nvidia"]["gpus"][0]["serial"] == "abc123"
    assert (
        sensors_dict["windows_sensors"]["nvidia"]["gpus"][0]["system_type"]
        == "System Type"
    )
    assert sensors_dict["windows_sensors"]["nvidia"]["gpus"][0]["type"] == "Type"

    sensors_converted = Sensors(**sensors_dict)
    test_sensors(sensors_converted)
