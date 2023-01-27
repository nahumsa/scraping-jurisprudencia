from entities.decision_data import DecisionData

class TestDecisionData:
    def test_decision_data_with_none_values(self):
        decision_data = DecisionData(
        process_number = "0000.0000",
        document_href = "javascript:document.location.replace('/jurisprudencia/publico/visualizacao.do?tjpr.url.crypto=8a6c53f8698c7ff76db3047d195cb6a50e1bad728475d917206904084c03d1a7e341e6d089e3dce5f94a697fefb84d63d82ea4c16cd92563d1565373ab804d09fba37b2809a05b1db0c8c3cf6544d248')",
        decision_text = "a\n\nb",
        decision_type = "asd",
        judgement_date = "Data do Julgamento: 01/01/2023 00:00:00"
        )

        expected_dict = {
            'process_number': '0000.0000',
            'decision_type': 'asd',
            'document_href': "https://portal.tjpr.jus.br/jurisprudencia/publico/visualizacao.do?tjpr.url.crypto=8a6c53f8698c7ff76db3047d195cb6a50e1bad728475d917206904084c03d1a7e341e6d089e3dce5f94a697fefb84d63d82ea4c16cd92563d1565373ab804d09fba37b2809a05b1db0c8c3cf6544d248')",
            'judgement_date': '20230101',
            'decision_text': 'b',
            'judging_body': None,
            'judge': None,
            'district': None,
            'justice_secret': None,
            'publication_date': None
        }

        assert decision_data.dict() == expected_dict