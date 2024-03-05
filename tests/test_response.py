"""Test the response model."""

from systembridgemodels.response import Response


def test_response():
    """Test the response."""
    response = Response(
        id="abc123",
        type="TYPE_TEST",
        data={"test": "test"},
        subtype="SUBTYPE_TEST",
        message="MESSAGE_TEST",
        module="MODULE_TEST",
    )
    assert isinstance(response, Response)
    assert response.id == "abc123"
    assert response.type == "TYPE_TEST"
    assert response.data == {"test": "test"}
    assert response.subtype == "SUBTYPE_TEST"
    assert response.message == "MESSAGE_TEST"
    assert response.module == "MODULE_TEST"
