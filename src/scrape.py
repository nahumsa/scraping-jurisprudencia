import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import local_config
from errors import ExecutionError, check_page_error, generate_error_dict
from extract import extract_decision_data
from pagination import (
    extract_max_page_number,
    extract_number_of_entries_per_page,
    extract_total_number_of_entries,
)
from repository import DecisionDetailsPageRepository, DecisionXPathOptions
from search import fill_judgement_end, fill_judgement_start, post_search


def change_to_window_handle(driver: webdriver, window_position: int) -> None:
    window = driver.window_handles[window_position]
    driver.switch_to.window(window)


def get_decision_element(number_in_list: int):
    decision = driver.find_element(
        By.XPATH,
        f"/html/body/div/div[3]/div/form/div[2]/div/div/table/tbody/tr[3]/td[2]/table/tbody/tr[{number_in_list + 1}]/td[1]/div[2]/a/div/div",
    )
    return decision


def is_decision_justice_secret(number_in_list: int) -> bool:
    try:
        justice_secret_badge_text = driver.find_element(
            By.XPATH,
            f"/html/body/div/div[3]/div/form/div[2]/div/div/table/tbody/tr[3]/td[2]/table/tbody/tr[{number_in_list + 1}]/td[1]/span",
        ).text

        match justice_secret_badge_text:
            case "Segredo de Justiça":
                return True
            case _:
                raise ValueError("Unexpected value in the justice_secret_badge")
    except:
        return False


def get_next_page_element():
    next_page = driver.find_element(
        By.XPATH,
        "/html/body/div/div[3]/div/form/div[2]/div/div/table/tbody/tr[2]/td[2]/div[1]/div[1]/a[5]",
    )
    return next_page


def get_page_information_text() -> str:
    page_information_text = driver.find_element(
        By.XPATH,
        "/html/body/div/div[3]/div/form/div[2]/div/div/table/tbody/tr[2]/td[2]/div[1]/div[2]",
    ).text
    return page_information_text


configs = local_config.load()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://portal.tjpr.jus.br/jurisprudencia/")

time.sleep(2)

# search by date
search_start_date = configs["search"]["start_date"]
search_end_date = configs["search"]["end_date"]

judgement_start_element = fill_judgement_start(driver, start_date=search_start_date)
judgement_end_element = fill_judgement_end(driver, end_date=search_end_date)
search_element = post_search(driver)

# scrape process
page_information_text = get_page_information_text()
total_number_of_entries = extract_total_number_of_entries(page_information_text)
number_of_entries_per_page = extract_number_of_entries_per_page(page_information_text)
max_page_number = extract_max_page_number(
    total_number_of_entries, number_of_entries_per_page
)


for current_page_number in range(1, max_page_number + 1):
    page_data = []
    try:
        check_page_error(driver, current_page_number)

        for decision_index in range(1, number_of_entries_per_page + 1):
            if not is_decision_justice_secret(decision_index):
                decision = get_decision_element(decision_index)
                decision.click()

                change_to_window_handle(driver, 1)

                decision_detail_repository = DecisionDetailsPageRepository(
                    session=driver
                )

                data = extract_decision_data(
                    repository=decision_detail_repository,
                    x_path_enum=DecisionXPathOptions,
                )

                driver.close()
                change_to_window_handle(driver, 0)

                page_data.append(data)

    except ExecutionError as e:
        error_json = generate_error_dict(
            page_number=current_page_number,
            max_pages=max_page_number,
            search_start_date=search_start_date,
            search_end_date=search_end_date,
        )

        raise e

    get_next_page_element().click()
