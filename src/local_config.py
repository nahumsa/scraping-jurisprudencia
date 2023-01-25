from typing import Any

import toml


def load(config_path: str = "config.toml") -> dict[str, Any]:
    """Loads a toml with the configuration used for scraping.

    Args:
        config_path (str, optional): toml file path. Defaults to "config.toml".

    Returns:
        dict[str, Any]: configuration used for scraping.
    """
    with open(config_path, "r", encoding="utf-8") as file:
        configs = toml.load(file)

    return configs
