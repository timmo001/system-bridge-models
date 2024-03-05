"""Test the keyboard_key model."""

from systembridgemodels.keyboard_key import KeyboardKey


def test_keyboard_key():
    """Test the keyboard_key."""
    keyboard_key = KeyboardKey(
        key="A",
    )
    assert isinstance(keyboard_key, KeyboardKey)
    assert keyboard_key.key == "A"
