"""Test the OpenPath model."""

from systembridgemodels.open_path import OpenPath


def test_open_path():
    """Test the open_path."""
    open_path = OpenPath(
        path="/path/to/file",
    )
    assert isinstance(open_path, OpenPath)
    assert open_path.path == "/path/to/file"
