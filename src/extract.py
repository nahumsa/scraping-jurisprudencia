from enum import Enum

from entities import DecisionData
from repository import AbstractRepository
from transforms import transform_process_text


def extract_decision_data(
    repository: AbstractRepository, x_path_enum: Enum
) -> DecisionData:

    # TODO: build a constructor pattern for this
    process_text = repository.get(reference=x_path_enum.PROCESS)
    process_number, decision_type = transform_process_text(process_text)
    justice_secret_text = repository.get(reference=x_path_enum.JUSTICE_SECRET)
    judge_text = repository.get(reference=x_path_enum.JUDGE)
    judging_body_text = repository.get(reference=x_path_enum.JUDGING_BODY)
    district_text = repository.get(reference=x_path_enum.DISTRICT)
    judgement_date_text = repository.get(reference=x_path_enum.JUDGEMENT_DATE)
    publication_date_text = repository.get(reference=x_path_enum.PUBLICATION_DATE)
    decision_text = repository.get(reference=x_path_enum.DECISION_TEXT)
    document_href = repository.get(reference=x_path_enum.DOCUMENT_HREF)

    data = DecisionData(
        process_number=process_number,
        decision_type=decision_type,
        district=district_text,
        justice_secret=justice_secret_text,
        judgement_date=judgement_date_text,
        publication_date=publication_date_text,
        judge=judge_text,
        judging_body=judging_body_text,
        decision_text=decision_text,
        document_href=document_href,
    )
