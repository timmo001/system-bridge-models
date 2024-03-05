"""Test the media model."""

from systembridgemodels.modules.media import Media


def test_media():
    """Test the media model."""
    media = Media(
        album_artist="Album Artist",
        album_title="Album Title",
        artist="Artist",
        duration=100,
        is_fast_forward_enabled=True,
        is_next_enabled=True,
        is_pause_enabled=True,
        is_play_enabled=True,
        is_previous_enabled=True,
        is_rewind_enabled=True,
        is_stop_enabled=True,
        playback_rate=1.0,
        position=100,
        repeat="repeat",
        shuffle=True,
        status="status",
        subtitle="subtitle",
        thumbnail="thumbnail",
        title="title",
        track_number=1,
        type="type",
        updated_at=100,
    )
    assert isinstance(media, Media)
    assert media.album_artist == "Album Artist"
    assert media.album_title == "Album Title"
    assert media.artist == "Artist"
    assert media.duration == 100
    assert media.is_fast_forward_enabled is True
    assert media.is_next_enabled is True
    assert media.is_pause_enabled is True
    assert media.is_play_enabled is True
    assert media.is_previous_enabled is True
    assert media.is_rewind_enabled is True
    assert media.is_stop_enabled is True
    assert media.playback_rate == 1.0
    assert media.position == 100
    assert media.repeat == "repeat"
    assert media.shuffle is True
    assert media.status == "status"
    assert media.subtitle == "subtitle"
    assert media.thumbnail == "thumbnail"
    assert media.title == "title"
    assert media.track_number == 1
    assert media.type == "type"
    assert media.updated_at == 100
