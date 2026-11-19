"""Entry point: this runs when you type `uv run python -m not_decided_yet`.

`python -m <package>` looks for a file called __main__.py inside the package and runs it.
"""

from not_decided_yet.config import load_settings


def main() -> None:
    """Print a short status message showing which settings were loaded."""
    settings = load_settings()
    print(f"Hello from not-decided-yet! Environment: {settings.environment}")
    if settings.azure_subscription_id:
        print("Azure subscription configured.")
    else:
        print("No Azure subscription set yet. Copy .env.example to .env and fill it in.")


# This check means "only run main() when this file is executed directly,
# not when it's imported by another file (e.g. a test)".
if __name__ == "__main__":
    main()
