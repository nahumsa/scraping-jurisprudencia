import abc
from enum import Enum

from selenium import webdriver
from selenium.webdriver.common.by import By


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def get(self, reference):
        raise NotImplementedError


class DecisionXPathOptions(Enum):
    PROCESS = "//*[@id='pesquisaForm']/div/table/tbody/tr[3]/td/table[2]/tbody/tr[2]/td"
    JUSTICE_SECRET = (
        "//*[@id='pesquisaForm']/div/table/tbody/tr[3]/td/table[2]/tbody/tr[3]/td"
    )
    JUDGE = "//*[@id='pesquisaForm']/div/table/tbody/tr[3]/td/table[2]/tbody/tr[4]/td"
    JUDGING_BODY = (
        "//*[@id='pesquisaForm']/div/table/tbody/tr[3]/td/table[2]/tbody/tr[5]/td"
    )
    DISTRICT = (
        "//*[@id='pesquisaForm']/div/table/tbody/tr[3]/td/table[2]/tbody/tr[6]/td"
    )
    JUDGEMENT_DATE = (
        "//*[@id='pesquisaForm']/div/table/tbody/tr[3]/td/table[2]/tbody/tr[7]/td"
    )
    PUBLICATION_DATE = (
        "//*[@id='pesquisaForm']/div/table/tbody/tr[3]/td/table[2]/tbody/tr[8]/td"
    )
    DECISION_TEXT = (
        "//*[@id='pesquisaForm']/div/table/tbody/tr[3]/td/table[2]/tbody/tr[9]/td"
    )
    DOCUMENT_HREF = (
        "//*[@id='pesquisaForm']/div/table/tbody/tr[3]/td/table[2]/tbody/tr[1]/td[3]/a"
    )


class AcordaoXPathOptions(Enum):

    PROCESS = "//*[@id='pesquisaForm']/div/table/tbody/tr[3]/td/table[2]/tbody/tr[3]/td"

    JUSTICE_SECRET = (
        "//*[@id='pesquisaForm']/div/table/tbody/tr[3]/td/table[2]/tbody/tr[4]/td"
    )
    JUDGE = "//*[@id='pesquisaForm']/div/table/tbody/tr[3]/td/table[2]/tbody/tr[5]/td"
    JUDGING_BODY = (
        "//*[@id='pesquisaForm']/div/table/tbody/tr[3]/td/table[2]/tbody/tr[7]/td"
    )
    DISTRICT = (
        "//*[@id='pesquisaForm']/div/table/tbody/tr[3]/td/table[2]/tbody/tr[8]/td"
    )
    JUDGEMENT_DATE = (
        "//*[@id='pesquisaForm']/div/table/tbody/tr[3]/td/table[2]/tbody/tr[9]/td"
    )
    PUBLICATION_DATE = (
        "//*[@id='pesquisaForm']/div/table/tbody/tr[3]/td/table[2]/tbody/tr[10]/td"
    )
    DECISION_TEXT = (
        "//*[@id='pesquisaForm']/div/table/tbody/tr[3]/td/table[2]/tbody/tr[11]/td"
    )
    DOCUMENT_HREF = (
        "//*[@id='pesquisaForm']/div/table/tbody/tr[3]/td/table[2]/tbody/tr[1]/td[3]/a"
    )


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
