import math

from selenium import webdriver
from selenium.webdriver.common.by import By


# TODO: group this information in an value object
def extract_total_number_of_entries(page_information_text: str) -> int:
    return int(page_information_text.split("registro(s)")[0].strip())


def extract_number_of_entries_per_page(page_information_text: str) -> int:
    return int(page_information_text.split("até")[1].strip())


def extract_max_page_number(
    total_number_of_entries: int, number_of_entries_per_page: int
) -> int:
    return math.ceil(total_number_of_entries / number_of_entries_per_page)


def get_next_page_element(driver: webdriver):
    next_page = driver.find_element(
        By.XPATH,
        "/html/body/div/div[3]/div/form/div[2]/div/div/table/tbody/tr[2]/td[2]/div[1]/div[1]/a[5]",
    )
    return next_page


def get_page_information_text(driver: webdriver) -> str:
    page_information_text = driver.find_element(
        By.XPATH,
        "/html/body/div/div[3]/div/form/div[2]/div/div/table/tbody/tr[2]/td[2]/div[1]/div[2]",
    ).text
    return page_information_text
