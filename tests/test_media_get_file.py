"""Test the media_get_file model."""

from systembridgemodels.media_get_file import MediaGetFile


def test_media_get_file():
    """Test the media_get_file."""
    media_get_file = MediaGetFile(
        base="music",
        path="path/to/file",
    )
    assert isinstance(media_get_file, MediaGetFile)
    assert media_get_file.base == "music"
    assert media_get_file.path == "path/to/file"
