from enum import Enum

from selenium import webdriver
from selenium.webdriver.common.by import By

from .abstract import AbstractRepository


class DecisionDetailsPageRepository(AbstractRepository):
    def __init__(self, session: webdriver) -> None:
        self.session = session

    def get(self, reference: Enum) -> str:
        # TODO: change to match/case
        if reference.name == "DOCUMENT_HREF":
            return self.session.find_element(By.XPATH, reference.value).get_attribute(
                "href"
            )
        else:
            return self.session.find_element(By.XPATH, reference.value).text
