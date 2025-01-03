"""Test the displays module model."""

from dataclasses import asdict
from syrupy.assertion import SnapshotAssertion

from systembridgemodels.fixtures.modules.displays import FIXTURE_DISPLAYS
from systembridgemodels.modules.displays import Display


def test_displays(snapshot: SnapshotAssertion):
    """Test the displays model."""
    displays = FIXTURE_DISPLAYS
    assert isinstance(displays, list)
    assert isinstance(displays[0], Display)
    assert displays == snapshot

def test_display_asdict(snapshot: SnapshotAssertion):
    displays = [asdict(displays) for displays in FIXTURE_DISPLAYS]
    assert displays[0]["power_state"] == displays[1]["power_state"]
    assert displays[0]["input_source"] == displays[1]["input_source"]
    assert displays == snapshot

def test_enums():
    displays = FIXTURE_DISPLAYS
    assert displays[0].power_state == displays[1].power_state
    assert displays[0].input_source == displays[1].input_source
