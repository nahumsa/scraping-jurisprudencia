from enum import Enum

class MonocraticDecisionXPathOptions(Enum):
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