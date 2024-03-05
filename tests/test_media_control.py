"""Test the media_control model."""

from systembridgemodels.media_control import MediaAction, MediaControl


def test_media_control():
    """Test the media_control."""
    media_control = MediaControl(
        action=MediaAction.PLAY.value,
        value=True,
    )
    assert isinstance(media_control, MediaControl)
    assert media_control.action == MediaAction.PLAY.value
    assert media_control.value is True
