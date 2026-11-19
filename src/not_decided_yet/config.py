"""Settings for the app, loaded from environment variables.

Why? Values like your Azure subscription ID differ per machine and per environment
(dev vs prod), and secrets must never be written into code. So we read them
from environment variables, which locally come from a `.env` file.
"""

import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass(frozen=True)
class Settings:
    """A simple container for all app settings.

    `@dataclass` auto-generates boilerplate (constructor, printing).
    `frozen=True` makes it read-only, so settings can't change by accident.
    """

    environment: str
    azure_subscription_id: str | None
    azure_tenant_id: str | None
    azure_location: str


def load_settings() -> Settings:
    """Read settings from environment variables (and `.env`, if present).

    Returns:
        A Settings object. Missing optional values become None;
        missing values that have defaults get sensible defaults.
    """
    load_dotenv()  # copies key=value lines from .env into os.environ (doesn't overwrite)
    return Settings(
        environment=os.getenv("APP_ENV", "dev"),
        azure_subscription_id=os.getenv("AZURE_SUBSCRIPTION_ID"),
        azure_tenant_id=os.getenv("AZURE_TENANT_ID"),
        azure_location=os.getenv("AZURE_LOCATION", "eastus"),
    )
