"""Test the gpus module model."""

from systembridgemodels.fixtures.modules.gpus import FIXTURE_GPUS
from systembridgemodels.modules.gpus import GPU


def test_gpus():
    """Test the GPUs model."""
    gpus = FIXTURE_GPUS
    assert isinstance(gpus, list)
    assert isinstance(gpus[0], GPU)
    assert gpus[0].id == "abc123"
    assert gpus[0].name == "name"
    assert gpus[0].core_clock == 1000.0
    assert gpus[0].core_load == 100.0
    assert gpus[0].fan_speed == 100.0
    assert gpus[0].memory_clock == 1000.0
    assert gpus[0].memory_load == 100.0
    assert gpus[0].memory_free == 1000.0
    assert gpus[0].memory_used == 1000.0
    assert gpus[0].memory_total == 1000.0
    assert gpus[0].power_usage == 100.0
    assert gpus[0].temperature == 100.0
