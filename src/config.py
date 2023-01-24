import toml

def load(config_path: str="config.toml"):

    with open(config_path, "r") as f:
        configs = toml.load(f)

    return configs