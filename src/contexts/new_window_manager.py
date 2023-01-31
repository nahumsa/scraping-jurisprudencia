from __future__ import annotations

from selenium import webdriver


class DecisionPageContextManager:
    def __init__(self, driver: webdriver) -> DecisionPageContextManager:
        self.driver = driver

    def __enter__(self):
        self.__change_to_window_handle(self.driver, 1)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.close()
        self.__change_to_window_handle(self.driver, 0)

    def __change_to_window_handle(
        self, driver: webdriver, window_position: int
    ) -> None:
        window = driver.window_handles[window_position]
        driver.switch_to.window(window)
