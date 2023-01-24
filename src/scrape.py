import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

import config
from repository import DecisionDetailsPageRepository, DecisionXPathOptions
from search import fill_judgement_end, fill_judgement_start, post_search

configs = config.load()


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
process_text = decision_detail_repository.get(reference=DecisionXPathOptions.PROCESS)
justice_secret_text = decision_detail_repository.get(
    reference=DecisionXPathOptions.JUSTICE_SECRET
)
judge_text = decision_detail_repository.get(reference=DecisionXPathOptions.JUDGE)
judging_body_text = decision_detail_repository.get(
    reference=DecisionXPathOptions.JUDGING_BODY
)
district_text = decision_detail_repository.get(reference=DecisionXPathOptions.DISTRICT)
judgement_date_text = decision_detail_repository.get(
    reference=DecisionXPathOptions.JUDGEMENT_DATE
)
publication_date_text = decision_detail_repository.get(
    reference=DecisionXPathOptions.PUBLICATION_DATE
)
decision_text = decision_detail_repository.get(
    reference=DecisionXPathOptions.DECISION_TEXT
)
document_href = decision_detail_repository.get(
    reference=DecisionXPathOptions.DOCUMENT_HREF
)

print(process_text)
