"""Test the networks model."""

from systembridgemodels.modules.processes import Process


def test_networks():
    """Test the processes model."""
    processes = [
        Process(
            id=1234,
            name="name",
            cpu_usage=12.3,
            created=12.3,
            memory_usage=12.3,
            path="/path",
            status="running",
            username="username",
            working_directory="/working/directory",
        )
    ]
    assert isinstance(processes, list)
    assert isinstance(processes[0], Process)
    assert processes[0].id == 1234
    assert processes[0].name == "name"
    assert processes[0].cpu_usage == 12.3
    assert processes[0].created == 12.3
    assert processes[0].memory_usage == 12.3
    assert processes[0].path == "/path"
    assert processes[0].status == "running"
    assert processes[0].username == "username"
    assert processes[0].working_directory == "/working/directory"
