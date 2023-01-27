from pydantic import BaseModel, Field

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
    judgement_date: JudgementDate
    decision_text: DecisionText
    judging_body: JudgingBody = Field(default=None)
    judge: Judge = Field(default=None)
    district: District = Field(default=None)
    justice_secret: JusticeSecret = Field(default=None)
    publication_date: PublicationDate = Field(default=None)
