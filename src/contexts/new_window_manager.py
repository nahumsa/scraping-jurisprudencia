from __future__ import annotations

from selenium import webdriver

from selenium.webdriver.common.by import By

class DecisionPageContextManager:
    def __init__(self, driver: webdriver, decision_index: int) -> DecisionPageContextManager:
        self.driver = driver
        self.decision_index = decision_index

    def __enter__(self):
        NEXT_PAGE = 1
        self.__click_decision_element(self.driver, self.decision_index)
        self.__change_to_window_handle(self.driver, NEXT_PAGE)

    def __exit__(self, exc_type, exc_val, exc_tb):
        PREVIOUS_PAGE = 0
        self.driver.close()
        self.__change_to_window_handle(self.driver, PREVIOUS_PAGE)

    def __change_to_window_handle(
        self, driver: webdriver, window_position: int
    ) -> None:
        window = driver.window_handles[window_position]
        driver.switch_to.window(window)

    def __get_decision_element(self, driver: webdriver, number_in_list: int):
        decision = driver.find_element(
            By.XPATH,
            f"/html/body/div/div[3]/div/form/div[2]/div/div/table/tbody/tr[3]/td[2]/table/tbody/tr[{number_in_list + 1}]/td[1]/div[2]/a/div/div",
        )
        return decision

    def __click_decision_element(self, driver: webdriver, decision_index: int) -> None:
        decision = self.__get_decision_element(driver, decision_index)
        decision.click()