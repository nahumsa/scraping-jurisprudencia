import json
from datetime import datetime
from pathlib import Path
from typing import Any

import pandas as pd


def create_directory_if_not_exists(folder_name: str) -> Path:
    """Creates a directory, named `folder_name`, if it doesn't exist.

    Args:
        folder_name (str): name of the folder.

    Returns:
        Path: directory path object.
    """

    directory = Path(folder_name)
    directory.mkdir(exist_ok=True)
    return directory


def to_csv(
    df: pd.DataFrame,
    base_folder: str,
    court_acronym: str,
    start_date: str,
    end_date: str,
) -> None:
    """Saves a csv in `base_folder`, if the `base_folder` directory doesn't exists, it creates one. The name of the file has the following structure: `"{court_acronym}_{start_date}_{end_date}.csv"`. The date formats are YYYYMMDD.

    Args:
        df (pd.DataFrame): _description_
        base_folder (str): _description_
        court_acronym (str): _description_
        start_date (str): _description_
        end_date (str): _description_
    """

    directory = create_directory_if_not_exists(base_folder)
    formated_start_date = datetime.strptime(start_date, "%d/%m/%Y").strftime("%Y%m%d")
    formated_end_date = datetime.strptime(end_date, "%d/%m/%Y").strftime("%Y%m%d")
    file_name = f"{court_acronym}_{formated_start_date}_{formated_end_date}.csv"
    df.to_csv(directory / file_name)


def to_json(data: dict[str, Any], base_folder: str, file_name: str) -> None:
    directory = create_directory_if_not_exists(base_folder)

    with open(directory / file_name, "w") as file:
        json.dump(data, file, indent=4)
