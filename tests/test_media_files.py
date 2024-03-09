"""Test the media_files model."""

from dataclasses import asdict

from systembridgemodels.fixtures.media_files import FIXTURE_MEDIA_FILES
from systembridgemodels.media_files import MediaFile, MediaFiles


def test_media_files(media_files: MediaFiles = FIXTURE_MEDIA_FILES):
    """Test the media_files."""
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


def test_media_files_dict():
    """Test media files dict."""
    media_files_dict = asdict(FIXTURE_MEDIA_FILES)
    assert isinstance(media_files_dict, dict)
    assert isinstance(media_files_dict["files"], list)
    assert isinstance(media_files_dict["files"][0], dict)
    assert media_files_dict["files"][0]["name"] == "file1"
    assert media_files_dict["files"][0]["path"] == "path/to/file1"
    assert media_files_dict["files"][0]["fullpath"] == "/full/path/to/file1"
    assert media_files_dict["files"][0]["size"] == 100
    assert media_files_dict["files"][0]["last_accessed"] == 100.0
    assert media_files_dict["files"][0]["created"] == 100.0
    assert media_files_dict["files"][0]["modified"] == 100.0
    assert media_files_dict["files"][0]["is_directory"] is False
    assert media_files_dict["files"][0]["is_file"] is True
    assert media_files_dict["files"][0]["is_link"] is False
    assert media_files_dict["files"][0]["mime_type"] == "text/plain"
    assert media_files_dict["path"] == "path/to/file"

    media_files_converted = MediaFiles(**media_files_dict)
    test_media_files(media_files_converted)
