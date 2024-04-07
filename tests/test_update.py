"""Test the update model."""

from syrupy.assertion import SnapshotAssertion

from systembridgemodels._version import __version__
from systembridgemodels.update import Update


def test_update(snapshot: SnapshotAssertion):
    """Test the update."""
    update = Update(
        version=__version__.public(),
    )
    assert isinstance(update, Update)
    assert update == snapshot
