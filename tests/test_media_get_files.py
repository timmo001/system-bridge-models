"""Test the media_get_files model."""

from systembridgemodels.media_get_files import MediaGetFiles


def test_media_get_files():
    """Test the media_get_files."""
    media_get_files = MediaGetFiles(
        base="music",
        path="path/to/file",
    )
    assert isinstance(media_get_files, MediaGetFiles)
    assert media_get_files.base == "music"
    assert media_get_files.path == "path/to/file"
