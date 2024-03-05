"""Test the settings model."""

from systembridgemodels.settings import Settings, SettingsAPI, SettingsMedia


def test_settings():
    """Test the settings."""
    settings = Settings()
    assert isinstance(settings, Settings)
    assert isinstance(settings.api, SettingsAPI)
    assert isinstance(settings.api.token, str)
    assert isinstance(settings.api.port, int)
    assert isinstance(settings.autostart, bool)
    assert isinstance(settings.keyboard_hotkeys, list)
    assert isinstance(settings.log_level, str)
    assert isinstance(settings.media, SettingsMedia)
    assert isinstance(settings.media.directories, list)
