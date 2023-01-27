from pydantic import BaseModel

from validators.entities import (
    DecisionText,
    District,
    DocumentHref,
    Judge,
    JudgementDate,
    JudgingBody,
    JusticeSecret,
    PublicationDate,
)


class DecisionData(BaseModel):
    """Entity for the decision data, it helds bussiness information and validation for each entry besides `process_number` and `decision_type`. For more information see `validators.entities`."""

    # TODO: add bussiness logic for process number and decision type
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
