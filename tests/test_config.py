"""Tests for config.py.

pytest automatically finds files named test_*.py and runs every function named test_*.
If an `assert` is false, the test fails and pytest shows you why.
"""

from not_decided_yet.config import load_settings


def test_defaults_when_nothing_is_set(monkeypatch):
    """With no environment variables, we should get the default values.

    `monkeypatch` is a pytest helper that changes environment variables only for
    this test and restores them afterwards, so tests don't affect each other.
    """
    for name in ("APP_ENV", "AZURE_SUBSCRIPTION_ID", "AZURE_TENANT_ID", "AZURE_LOCATION"):
        monkeypatch.delenv(name, raising=False)
    monkeypatch.setattr("not_decided_yet.config.load_dotenv", lambda: None)  # ignore any real .env

    settings = load_settings()

    assert settings.environment == "dev"
    assert settings.azure_location == "eastus"
    assert settings.azure_subscription_id is None


def test_reads_values_from_environment(monkeypatch):
    """Values set in the environment should show up in Settings."""
    monkeypatch.setenv("APP_ENV", "prod")
    monkeypatch.setenv("AZURE_LOCATION", "westeurope")

    settings = load_settings()

    assert settings.environment == "prod"
    assert settings.azure_location == "westeurope"
