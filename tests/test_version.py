"""Test version."""

from systembridgemodels._version import __version__


def test_version():
    """Test the version."""
    assert isinstance(__version__.public(), str)
