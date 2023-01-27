# pylint: disable=missing-function-docstring
import pandas as pd
import pytest
from pydantic import BaseModel

from transforms import convert_model_list_to_dataframe, transform_process_text


class BaseModelTest(BaseModel):
    test: str


class TestTransformProcessText:
    def test_transform_process_text_happy_path(self):
        input_text = "Processo:\n0000248-42.2023.8.16.0000\n(Decisão monocrática)"
        expected_process_number = "0000248-42.2023.8.16.0000"
        expected_decision = "(Decisão monocrática)"
        got_process_number, got_decision = transform_process_text(input_text)
        assert got_process_number == expected_process_number
        assert got_decision == expected_decision

    def test_transform_process_text_wrong_keyword(self):
        keyword = "Teste:"
        input_text = f"{keyword}\n0000248-42.2023.8.16.0000\n(Decisão monocrática)"

        with pytest.raises(ValueError) as error_info:
            transform_process_text(input_text)

        assert str(error_info.value) == f"wrong text for process text, found {keyword}"


class TestConvertModelListToDataFrame:
    def test_convert_model_list_to_dataframe_happy_path(self):
        base_dict = {"test": "1"}
        model_list = [BaseModelTest(**base_dict)]
        got_df = convert_model_list_to_dataframe(model_list)
        expected_df = pd.DataFrame([base_dict])

        pd.testing.assert_frame_equal(got_df, expected_df)
