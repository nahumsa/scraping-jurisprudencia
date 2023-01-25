import time
from enum import Enum

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import local_config

from repository import (
    DecisionDetailsPageRepository,
    DecisionXPathOptions,
)
from search import fill_judgement_end, fill_judgement_start, post_search
from extract import extract_decision_data

configs = local_config.load()


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://portal.tjpr.jus.br/jurisprudencia/")

time.sleep(2)


judgement_start_element = fill_judgement_start(
    driver, start_date=configs["search"]["start_date"]
)
judgement_end_element = fill_judgement_end(
    driver, end_date=configs["search"]["end_date"]
)
search_element = post_search(driver)

decision = driver.find_element(
    By.XPATH,
    "/html/body/div/div[3]/div/form/div[2]/div/div/table/tbody/tr[3]/td[2]/table/tbody/tr[2]/td[1]/div[2]/a",
)
decision.click()

window_after = driver.window_handles[1]
driver.switch_to.window(window_after)

decision_detail_repository = DecisionDetailsPageRepository(session=driver)

data = extract_decision_data(
    repository=decision_detail_repository, x_path_enum=DecisionXPathOptions
)

print(data)
