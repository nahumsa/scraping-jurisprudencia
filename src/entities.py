from pydantic import BaseModel

from validators import DocumentHref, JudgingBody, Judge, District, JusticeSecret, PublicationDate, JudgementDate, DecisionText

class DecisionData(BaseModel):
    process_number: str
    decision_type: str
    document_href: DocumentHref
    judging_body: JudgingBody
    judge: Judge
    district: District
    justice_secret: JusticeSecret
    publication_date: PublicationDate
    judgement_date: JudgementDate
    decision_text: DecisionText
