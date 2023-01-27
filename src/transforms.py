import pandas as pd
from pydantic import BaseModel


def transform_process_text(process_text: str, delimiter: str = "\n") -> tuple[str, str]:
    """_summary_

    Args:
        process_text (str): _description_
        delimiter (str, optional): text delimiter for the process. Defaults to "\n".

    Raises:
        ValueError: if the keyword (first word) is not `"Processo:"`.

    Returns:
        str: process number
        str: decision
    """
    keyword, process_number, decision = process_text.split(delimiter)

    if keyword != "Processo:":
        raise ValueError(f"wrong text for process text, found {keyword}")

    return process_number, decision


def convert_model_list_to_dataframe(model_list: list[BaseModel]) -> pd.DataFrame:
    """Converts a pydantic model to a dataframe.

    Args:
        model_list (list[BaseModel]): List with the base model.

    Returns:
        pd.Dataframe: dataframe with the BaseModel data.
    """
    return pd.DataFrame([model.dict() for model in model_list])
