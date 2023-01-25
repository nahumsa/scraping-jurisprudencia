def transform_process_text(process_text: str, delimiter: str = "\n") -> tuple[str, str]:
    keyword, process_number, decision = process_text.split(delimiter)

    if keyword != "Processo:":
        raise ValueError("wrong text for process text")

    return process_number, decision
