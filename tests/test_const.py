"""Test const."""

from collections.abc import Callable

from systembridgemodels.const import MODEL_MAP


def test_model_map():
    """Test the model_map."""
    assert isinstance(MODEL_MAP, dict)
    for key, value in MODEL_MAP.items():
        assert isinstance(key, str)
        assert isinstance(value, Callable)
