"""Test the request model."""

from systembridgemodels.request import Request


def test_request():
    """Test the request."""
    request = Request(
        token="abc123",
        id="abc123",
        event="EVENT_TEST",
        data={"test": "test"},
    )
    assert isinstance(request, Request)
    assert request.token == "abc123"
    assert request.id == "abc123"
    assert request.event == "EVENT_TEST"
    assert request.data == {"test": "test"}
