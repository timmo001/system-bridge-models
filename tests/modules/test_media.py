"""Test the media module model."""

from syrupy.assertion import SnapshotAssertion

from systembridgemodels.fixtures.modules.media import FIXTURE_MEDIA
from systembridgemodels.modules.media import Media


def test_media(snapshot: SnapshotAssertion):
    """Test the media model."""
    media = FIXTURE_MEDIA
    assert isinstance(media, Media)
    assert media == snapshot
