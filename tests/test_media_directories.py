"""Test the media_directories model."""

from systembridgemodels.media_directories import MediaDirectory


def test_media_directories():
    """Test the media_directories."""
    media_directories = [
        MediaDirectory(
            key="music",
            path="path/to/file",
        )
    ]
    assert isinstance(media_directories, list)
    assert isinstance(media_directories[0], MediaDirectory)
    assert media_directories[0].key == "music"
    assert media_directories[0].path == "path/to/file"
