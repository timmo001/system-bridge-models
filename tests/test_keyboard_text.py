"""Test the keyboard_text model."""

from systembridgemodels.keyboard_text import KeyboardText


def test_keyboard_text():
    """Test the keyboard_text."""
    keyboard_text = KeyboardText(
        text="Test",
    )
    assert isinstance(keyboard_text, KeyboardText)
    assert keyboard_text.text == "Test"
