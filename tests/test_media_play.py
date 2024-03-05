"""Test the media_play model."""

from systembridgemodels.media_play import MediaPlay


def test_media_play():
    """Test the media_play."""
    media_play = MediaPlay(
        url="https://www.example.com/audio.mp3",
        album="Album",
        artist="Artist",
        autoplay=True,
        cover="https://www.example.com/cover.png",
        title="Title",
        volume=100,
    )
    assert isinstance(media_play, MediaPlay)
    assert media_play.url == "https://www.example.com/audio.mp3"
    assert media_play.album == "Album"
    assert media_play.artist == "Artist"
    assert media_play.autoplay is True
    assert media_play.cover == "https://www.example.com/cover.png"
    assert media_play.title == "Title"
    assert media_play.volume == 100
