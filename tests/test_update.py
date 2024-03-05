"""Test the update model."""

from systembridgemodels._version import __version__
from systembridgemodels.update import Update


def test_update():
    """Test the update."""
    update = Update(
        version=__version__.public(),
    )
    assert isinstance(update, Update)
    assert isinstance(update.version, str)
    assert update.version == __version__.public()
