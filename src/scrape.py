import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from contexts.strategy import StrategyContext

import load
import local_config
from contexts.new_window_manager import DecisionPageContextManager
from enums import DuvidaXPathOptions, MonocraticDecisionXPathOptions
from errors import ExecutionError, check_page_error, generate_error_dict
from extract import extract_decision_data, extract_duvida_exame_data
from pagination import (
    extract_max_page_number,
    extract_number_of_entries_per_page,
    extract_total_number_of_entries,
    get_next_page_element,
    get_page_information_text,
)
from repositories.decision_details import DecisionDetailsPageRepository
from search import fill_judgement_end, fill_judgement_start, post_search
from strategy.monocratic_decision import MonocraticDecisionStrategy
from transforms import convert_model_list_to_dataframe
from validators.webpage import get_decision_type, is_decision_justice_secret

def main():
    configs = local_config.load()

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://portal.tjpr.jus.br/jurisprudencia/")

    time.sleep(2)

    # search by date
    search_start_date = configs["search"]["start_date"]
    search_end_date = configs["search"]["end_date"]

    _ = fill_judgement_start(driver, start_date=search_start_date)
    _ = fill_judgement_end(driver, end_date=search_end_date)
    _ = post_search(driver)

    # scrape process
    page_information_text = get_page_information_text(driver)
    total_number_of_entries = extract_total_number_of_entries(page_information_text)
    number_of_entries_per_page = extract_number_of_entries_per_page(
        page_information_text
    )
    max_page_number = extract_max_page_number(
        total_number_of_entries, number_of_entries_per_page
    )

    all_data = []
    for current_page_number in range(1, max_page_number + 1):
        try:
            check_page_error(driver, current_page_number)
            for decision_index in range(1, number_of_entries_per_page + 1):
                is_justice_secret = is_decision_justice_secret(driver, decision_index)
                decision_type = get_decision_type(driver, decision_index)

                if not is_justice_secret:
                    decision_context = StrategyContext(None)

                    # TODO: refactor with a strategy design pattern
                    if decision_type == "(Decisão monocrática)":
                        decision_x_path_enum = MonocraticDecisionXPathOptions
                        process_function = extract_decision_data
                        decision_context.set_strategy(MonocraticDecisionStrategy)

                    elif decision_type == "(Dúvida/exame de competência)":
                        decision_x_path_enum = DuvidaXPathOptions

                        with DecisionPageContextManager(driver, decision_index):
                            decision_detail_repository = DecisionDetailsPageRepository(
                                session=driver
                            )

                            data = extract_duvida_exame_data(
                                repository=decision_detail_repository,
                                x_path_enum=decision_x_path_enum,
                            )

                            all_data.append(data)

                    with DecisionPageContextManager(driver, decision_index):
                        decision_detail_repository = DecisionDetailsPageRepository(
                            session=driver
                        )

                        data = decision_context.execute_strategy(
                            xpath=decision_x_path_enum,
                            repository=decision_detail_repository,
                            process_function=process_function
                            )

                        all_data.append(data)

                    decision_detail_df = convert_model_list_to_dataframe(all_data)
                    load.to_csv(
                        df=decision_detail_df,
                        base_folder="data",
                        court_acronym="TJPR",
                        start_date=search_start_date,
                        end_date=search_end_date,
                    )

        except ExecutionError as e:
            error_json = generate_error_dict(
                page_number=current_page_number,
                max_pages=max_page_number,
                search_start_date=search_start_date,
                search_end_date=search_end_date,
            )
            load.to_json(
                error_json, base_folder="data", file_name="execution_error.json"
            )
            raise e

        get_next_page_element(driver).click()


if __name__ == "__main__":
    main()
