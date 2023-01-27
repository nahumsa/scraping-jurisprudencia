from selenium import webdriver
from selenium.webdriver.common.by import By


def is_decision_justice_secret(driver: webdriver, number_in_list: int) -> bool:
    try:
        justice_secret_badge_text = driver.find_element(
            By.XPATH,
            f"/html/body/div/div[3]/div/form/div[2]/div/div/table/tbody/tr[3]/td[2]/table/tbody/tr[{number_in_list + 1}]/td[1]/span",
        ).text

        match justice_secret_badge_text:
            case "Segredo de Justiça":
                return True
            case _:
                raise ValueError("Unexpected value in the justice_secret_badge")
    except:
        return False


def get_decision_type(driver: webdriver, number_in_list: int) -> bool:
    try:
        decision_type_text = (
            driver.find_element(
                By.XPATH,
                f"/html/body/div/div[3]/div/form/div[2]/div/div/table/tbody/tr[3]/td[2]/table/tbody/tr[{number_in_list + 1}]/td[1]",
            )
            .text.split("\n\n")[0]
            .split("\n")[-1]
        )

        return decision_type_text.strip()


    except:
        return False
