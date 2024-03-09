"""Test the OpenPath model."""

from dataclasses import asdict

from systembridgemodels.fixtures.notification import FIXTURE_NOTIFICATION
from systembridgemodels.notification import Action, Audio, Notification


def test_notification(notification: Notification = FIXTURE_NOTIFICATION):
    """Test the notification."""
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


def test_notification_dict():
    """Test notification dict."""
    notification_dict = asdict(FIXTURE_NOTIFICATION)
    assert isinstance(notification_dict, dict)
    assert notification_dict["title"] == "Title"
    assert notification_dict["message"] == "Message"
    assert notification_dict["icon"] == "https://www.example.com/icon.png"
    assert notification_dict["image"] == "https://www.example.com/image.png"
    assert isinstance(notification_dict["actions"], list)
    assert isinstance(notification_dict["actions"][0], dict)
    assert notification_dict["actions"][0]["command"] == "COMMAND_TEST"
    assert notification_dict["actions"][0]["label"] == "LABEL_TEST"
    assert notification_dict["actions"][0]["data"] == {"test": "test"}
    assert notification_dict["timeout"] == 1000
    assert isinstance(notification_dict["audio"], dict)
    assert notification_dict["audio"]["source"] == "https://www.example.com/audio.mp3"
    assert notification_dict["audio"]["volume"] == 100

    notification_converted = Notification(**notification_dict)
    test_notification(notification_converted)
