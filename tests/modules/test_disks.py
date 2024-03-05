"""Test the disks model."""

from dataclasses import asdict

from systembridgemodels.modules.disks import (
    Disk,
    DiskIOCounters,
    DiskPartition,
    Disks,
    DiskUsage,
)

model = Disks(
    devices=[
        Disk(
            name="name",
            partitions=[
                DiskPartition(
                    device="device",
                    mount_point="mountpoint",
                    filesystem_type="fstype",
                    options="options",
                    max_file_size=1,
                    max_path_length=2,
                    usage=DiskUsage(
                        total=1,
                        used=2,
                        free=3,
                        percent=40.2,
                    ),
                ),
            ],
            io_counters=DiskIOCounters(
                read_bytes=1,
                write_bytes=2,
                read_count=3,
                write_count=4,
                read_time=5,
                write_time=6,
            ),
        )
    ],
    io_counters=DiskIOCounters(
        read_bytes=1,
        write_bytes=2,
        read_count=3,
        write_count=4,
        read_time=5,
        write_time=6,
    ),
)


def _test_disk_partition(partition: DiskPartition):
    assert isinstance(partition, DiskPartition)
    assert partition.device == "device"
    assert partition.mount_point == "mountpoint"
    assert partition.filesystem_type == "fstype"
    assert partition.options == "options"
    assert partition.max_file_size == 1
    assert partition.max_path_length == 2
    assert isinstance(partition.usage, DiskUsage)
    assert partition.usage.total == 1
    assert partition.usage.used == 2
    assert partition.usage.free == 3
    assert partition.usage.percent == 40.2


def _test_disk(disk: Disk):
    assert isinstance(disk, Disk)
    assert disk.name == "name"
    assert isinstance(disk.partitions, list)
    assert isinstance(disk.partitions[0], DiskPartition)
    _test_disk_partition(disk.partitions[0])
    assert isinstance(disk.io_counters, DiskIOCounters)
    assert disk.io_counters.read_bytes == 1
    assert disk.io_counters.write_bytes == 2
    assert disk.io_counters.read_count == 3
    assert disk.io_counters.write_count == 4
    assert disk.io_counters.read_time == 5
    assert disk.io_counters.write_time == 6


def test_disks(disks: Disks = model):
    """Test the disks model."""
    assert isinstance(disks, Disks)
    assert isinstance(disks.devices, list)
    _test_disk(disks.devices[0])


def test_disks_dict():
    """Test disks dict."""
    disks_dict = asdict(model)
    assert isinstance(disks_dict, dict)
    assert isinstance(disks_dict["devices"], list)
    assert isinstance(disks_dict["devices"][0], dict)
    assert disks_dict["devices"][0]["name"] == "name"
    assert isinstance(disks_dict["devices"][0]["partitions"], list)
    assert isinstance(disks_dict["devices"][0]["partitions"][0], dict)
    assert disks_dict["devices"][0]["partitions"][0]["device"] == "device"
    assert disks_dict["devices"][0]["partitions"][0]["mount_point"] == "mountpoint"
    assert disks_dict["devices"][0]["partitions"][0]["filesystem_type"] == "fstype"
    assert disks_dict["devices"][0]["partitions"][0]["options"] == "options"
    assert disks_dict["devices"][0]["partitions"][0]["max_file_size"] == 1
    assert disks_dict["devices"][0]["partitions"][0]["max_path_length"] == 2
    assert isinstance(disks_dict["devices"][0]["partitions"][0]["usage"], dict)
    assert disks_dict["devices"][0]["partitions"][0]["usage"]["total"] == 1
    assert disks_dict["devices"][0]["partitions"][0]["usage"]["used"] == 2
    assert disks_dict["devices"][0]["partitions"][0]["usage"]["free"] == 3
    assert disks_dict["devices"][0]["partitions"][0]["usage"]["percent"] == 40.2
    assert isinstance(disks_dict["devices"][0]["io_counters"], dict)
    assert disks_dict["devices"][0]["io_counters"]["read_bytes"] == 1
    assert disks_dict["devices"][0]["io_counters"]["write_bytes"] == 2
    assert disks_dict["devices"][0]["io_counters"]["read_count"] == 3
    assert disks_dict["devices"][0]["io_counters"]["write_count"] == 4
    assert disks_dict["devices"][0]["io_counters"]["read_time"] == 5
    assert disks_dict["devices"][0]["io_counters"]["write_time"] == 6
    assert isinstance(disks_dict["io_counters"], dict)
    assert disks_dict["io_counters"]["read_bytes"] == 1
    assert disks_dict["io_counters"]["write_bytes"] == 2
    assert disks_dict["io_counters"]["read_count"] == 3
    assert disks_dict["io_counters"]["write_count"] == 4
    assert disks_dict["io_counters"]["read_time"] == 5
    assert disks_dict["io_counters"]["write_time"] == 6

    disks_converted = Disks(**disks_dict)
    test_disks(disks_converted)


def test_disks_devices_dict():
    """Test disks devices dict."""
    disk_dict = asdict(model.devices[0])
    assert disk_dict["name"] == "name"
    assert isinstance(disk_dict["partitions"], list)
    assert isinstance(disk_dict["partitions"][0], dict)
    assert disk_dict["partitions"][0]["device"] == "device"
    assert disk_dict["partitions"][0]["mount_point"] == "mountpoint"
    assert disk_dict["partitions"][0]["filesystem_type"] == "fstype"
    assert disk_dict["partitions"][0]["options"] == "options"
    assert disk_dict["partitions"][0]["max_file_size"] == 1
    assert disk_dict["partitions"][0]["max_path_length"] == 2
    assert isinstance(disk_dict["partitions"][0]["usage"], dict)
    assert disk_dict["partitions"][0]["usage"]["total"] == 1
    assert disk_dict["partitions"][0]["usage"]["used"] == 2
    assert disk_dict["partitions"][0]["usage"]["free"] == 3
    assert disk_dict["partitions"][0]["usage"]["percent"] == 40.2
    assert isinstance(disk_dict["io_counters"], dict)
    assert disk_dict["io_counters"]["read_bytes"] == 1
    assert disk_dict["io_counters"]["write_bytes"] == 2
    assert disk_dict["io_counters"]["read_count"] == 3
    assert disk_dict["io_counters"]["write_count"] == 4
    assert disk_dict["io_counters"]["read_time"] == 5
    assert disk_dict["io_counters"]["write_time"] == 6

    disk_converted = Disk(**disk_dict)
    _test_disk(disk_converted)


def test_disks_devices_partition_dict():
    """Test disks devices partition dict."""
    partition_dict = asdict(model.devices[0].partitions[0])
    assert partition_dict["device"] == "device"
    assert partition_dict["mount_point"] == "mountpoint"
    assert partition_dict["filesystem_type"] == "fstype"
    assert partition_dict["options"] == "options"
    assert partition_dict["max_file_size"] == 1
    assert partition_dict["max_path_length"] == 2
    assert isinstance(partition_dict["usage"], dict)
    assert partition_dict["usage"]["total"] == 1
    assert partition_dict["usage"]["used"] == 2
    assert partition_dict["usage"]["free"] == 3
    assert partition_dict["usage"]["percent"] == 40.2

    partition_converted = DiskPartition(**partition_dict)
    _test_disk_partition(partition_converted)
