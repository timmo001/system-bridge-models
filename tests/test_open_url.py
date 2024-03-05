"""Test the OpenUrl model."""

from systembridgemodels.open_url import OpenUrl


def test_open_url():
    """Test the open_url."""
    open_url = OpenUrl(
        url="https://www.example.com",
    )
    assert isinstance(open_url, OpenUrl)
    assert open_url.url == "https://www.example.com"
