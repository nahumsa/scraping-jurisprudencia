from enum import Enum


class DuvidaXPathOptions(Enum):

    PROCESS = "//*[@id='pesquisaForm']/div/table/tbody/tr[3]/td/table[2]/tbody/tr[2]/td"

    JUSTICE_SECRET = (
        "//*[@id='pesquisaForm']/div/table/tbody/tr[3]/td/table[2]/tbody/tr[3]/td"
    )
    JUDGEMENT_DATE = (
        "//*[@id='pesquisaForm']/div/table/tbody/tr[3]/td/table[2]/tbody/tr[4]/td"
    )
    DECISION_TEXT = (
        "//*[@id='pesquisaForm']/div/table/tbody/tr[3]/td/table[2]/tbody/tr[5]/td"
    )
    DOCUMENT_HREF = (
        "//*[@id='pesquisaForm']/div/table/tbody/tr[3]/td/table[2]/tbody/tr[1]/td[3]/a"
    )
