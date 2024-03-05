"""Test the media_files model."""

from systembridgemodels.media_files import MediaFile, MediaFiles


def test_media_files():
    """Test the media_files."""
    media_files = MediaFiles(
        files=[
            MediaFile(
                name="file1",
                path="path/to/file1",
                fullpath="/full/path/to/file1",
                size=100,
                last_accessed=100.0,
                created=100.0,
                modified=100.0,
                is_directory=False,
                is_file=True,
                is_link=False,
                mime_type="text/plain",
            ),
        ],
        path="path/to/file",
    )
    assert isinstance(media_files, MediaFiles)
    assert isinstance(media_files.files, list)
    assert isinstance(media_files.files[0], MediaFile)
    assert media_files.files[0].name == "file1"
    assert media_files.files[0].path == "path/to/file1"
    assert media_files.files[0].fullpath == "/full/path/to/file1"
    assert media_files.files[0].size == 100
    assert media_files.files[0].last_accessed == 100.0
    assert media_files.files[0].created == 100.0
    assert media_files.files[0].modified == 100.0
    assert media_files.files[0].is_directory is False
    assert media_files.files[0].is_file is True
    assert media_files.files[0].is_link is False
    assert media_files.files[0].mime_type == "text/plain"
    assert media_files.path == "path/to/file"
