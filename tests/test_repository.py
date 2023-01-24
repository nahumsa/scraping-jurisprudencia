from repository import DecisionXPathOptions


def test_decision_xpath_options():
    expected_fields = [
        "PROCESS",
        "JUSTICE_SECRET",
        "JUDGE",
        "JUDGING_BODY",
        "DISTRICT",
        "JUDGEMENT_DATE",
        "PUBLICATION_DATE",
        "DECISION_TEXT",
        "DOCUMENT_HREF",
    ]
    got_fields = [field.name for field in DecisionXPathOptions]

    assert set(expected_fields) == set(got_fields)
