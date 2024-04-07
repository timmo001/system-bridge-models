"""Test the networks module model."""

from syrupy.assertion import SnapshotAssertion

from systembridgemodels.fixtures.modules.system import FIXTURE_SYSTEM
from systembridgemodels.modules.system import System


def test_system(snapshot: SnapshotAssertion):
    """Test the system model."""
    system = FIXTURE_SYSTEM
    assert isinstance(system, System)
    assert system == snapshot
