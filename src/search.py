from selenium import webdriver
from selenium.webdriver.common.by import By


def fill_judgement_start(driver: webdriver, start_date: str) -> None:
    judgment_start_element = driver.find_element(by=By.ID, value="dataJulgamentoInicio")
    judgment_start_element.clear()
    judgment_start_element.send_keys(start_date)
    return judgment_start_element


def fill_judgement_end(driver: webdriver, end_date: str) -> None:
    judgment_end_element = driver.find_element(by=By.ID, value="dataJulgamentoFim")
    judgment_end_element.clear()
    judgment_end_element.send_keys(end_date)
    return judgment_end_element


def post_search(driver: webdriver):
    search_element = driver.find_element(by=By.NAME, value="iniciar")
    search_element.click()
    return search_element
