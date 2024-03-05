"""Test the action model."""

from systembridgemodels.action import Action


def test_action():
    """Test action."""
    action = Action(
        command="command",
        data={"key": "value"},
        label="label",
    )
    assert isinstance(action, Action)
    assert action.command == "command"
    assert action.data == {"key": "value"}
    assert action.label == "label"
