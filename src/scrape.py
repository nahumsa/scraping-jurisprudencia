import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

from search import fill_judgement_start, fill_judgement_end, post_search

import config


configs = config.load()


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://portal.tjpr.jus.br/jurisprudencia/")

time.sleep(2)


judgement_start_element = fill_judgement_start(driver, start_date=configs["search"]["start_date"])
judgement_end_element = fill_judgement_end(driver, end_date=configs["search"]["end_date"])
search_element = post_search(driver)

decision = driver.find_element(By.XPATH,
                               "/html/body/div/div[3]/div/form/div[2]/div/div/table/tbody/tr[3]/td[2]/table/tbody/tr[2]/td[1]/div[2]/a")
decision.click()

window_after = driver.window_handles[1]
driver.switch_to.window(window_after)

process_text = driver.find_element(By.XPATH, "//*[@id='pesquisaForm']/div/table/tbody/tr[3]/td/table[2]/tbody/tr[2]/td").text

secret_justice_text = driver.find_element(By.XPATH, "//*[@id='pesquisaForm']/div/table/tbody/tr[3]/td/table[2]/tbody/tr[3]/td").text

judge_text = driver.find_element(By.XPATH, "//*[@id='pesquisaForm']/div/table/tbody/tr[3]/td/table[2]/tbody/tr[4]/td").text

judging_body_text = driver.find_element(By.XPATH, "//*[@id='pesquisaForm']/div/table/tbody/tr[3]/td/table[2]/tbody/tr[5]/td").text

district_text = driver.find_element(By.XPATH, "//*[@id='pesquisaForm']/div/table/tbody/tr[3]/td/table[2]/tbody/tr[6]/td").text

judgment_date_text = driver.find_element(By.XPATH, "//*[@id='pesquisaForm']/div/table/tbody/tr[3]/td/table[2]/tbody/tr[7]/td").text

publication_date_text = driver.find_element(By.XPATH, "//*[@id='pesquisaForm']/div/table/tbody/tr[3]/td/table[2]/tbody/tr[8]/td").text

decision_text = driver.find_element(By.XPATH, "//*[@id='pesquisaForm']/div/table/tbody/tr[3]/td/table[2]/tbody/tr[9]/td").text

document_href = driver.find_element(By.XPATH, "//*[@id='pesquisaForm']/div/table/tbody/tr[3]/td/table[2]/tbody/tr[1]/td[3]/a")
