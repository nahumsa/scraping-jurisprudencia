from enum import Enum


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
