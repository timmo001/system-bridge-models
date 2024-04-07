"""Test the settings model."""

from syrupy.assertion import SnapshotAssertion
from syrupy.filters import props

from systembridgemodels.settings import (
    SettingDirectory,
    SettingHotkey,
    Settings,
    SettingsAPI,
    SettingsMedia,
)


def test_settings(snapshot: SnapshotAssertion):
    """Test the settings."""
    settings = Settings(
        api=SettingsAPI(
            token="token",
        ),
    )
    assert isinstance(settings, Settings)
    assert settings == snapshot


def test_settings_token():
    """Test the settings token."""
    settings = Settings()
    assert settings.api.token != ""
