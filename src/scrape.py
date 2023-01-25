import time
from enum import Enum

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import local_config
from extract import extract_decision_data
from repository import DecisionDetailsPageRepository, DecisionXPathOptions
from search import fill_judgement_end, fill_judgement_start, post_search


def change_to_window_handle(driver: webdriver, window_position: int) -> None:
    window = driver.window_handles[window_position]
    driver.switch_to.window(window)


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
def get_decision_element(number_in_list: int):
    decision = driver.find_element(
        By.XPATH,
        f"/html/body/div/div[3]/div/form/div[2]/div/div/table/tbody/tr[3]/td[2]/table/tbody/tr[{number_in_list + 1}]/td[1]/div[2]/a/div/div",
    )
    return decision


decision = get_decision_element(1)
decision.click()

change_to_window_handle(driver, 1)

decision_detail_repository = DecisionDetailsPageRepository(session=driver)

data = extract_decision_data(
    repository=decision_detail_repository, x_path_enum=DecisionXPathOptions
)

driver.close()

change_to_window_handle(driver, 0)

print(data)
