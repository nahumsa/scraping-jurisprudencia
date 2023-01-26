import math


# TODO: group this information in an entity
def extract_total_number_of_entries(page_information_text: str) -> int:
    return int(page_information_text.split("registro(s)")[0].strip())


def extract_number_of_entries_per_page(page_information_text: str) -> int:
    return int(page_information_text.split("até")[1].strip())


def extract_max_page_number(
    total_number_of_entries: int, number_of_entries_per_page: int
) -> int:
    return math.ceil(total_number_of_entries / number_of_entries_per_page)
