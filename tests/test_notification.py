"""Test the OpenPath model."""

from systembridgemodels.notification import Action, Audio, Notification


def test_notification():
    """Test the notification."""
    notification = Notification(
        title="Title",
        message="Message",
        icon="https://www.example.com/icon.png",
        image="https://www.example.com/image.png",
        actions=[
            Action(command="COMMAND_TEST", label="LABEL_TEST", data={"test": "test"})
        ],
        timeout=1000,
        audio=Audio(
            source="https://www.example.com/audio.mp3",
            volume=100,
        ),
    )
    assert isinstance(notification, Notification)
    assert notification.title == "Title"
    assert notification.message == "Message"
    assert notification.icon == "https://www.example.com/icon.png"
    assert notification.image == "https://www.example.com/image.png"
    assert isinstance(notification.actions, list)
    assert isinstance(notification.actions[0], Action)
    assert notification.actions[0].command == "COMMAND_TEST"
    assert notification.actions[0].label == "LABEL_TEST"
    assert notification.actions[0].data == {"test": "test"}
    assert notification.timeout == 1000
    assert isinstance(notification.audio, Audio)
    assert notification.audio.source == "https://www.example.com/audio.mp3"
    assert notification.audio.volume == 100
