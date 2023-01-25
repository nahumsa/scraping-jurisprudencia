from datetime import datetime


class ExecutionError(Exception):
    pass


page_number = 1
max_pages = 10
try:
    if driver.title == "502 Bad Gateway":
        raise ExecutionError(
            f"scrapper received a 502 status code when performing a pagination at page {page_number}"
        )

except ExecutionError as e:
    error_json = {
        "error": {
            "occured_at": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "status_code": 502,
            "message": f"scrapper received a 502 status code when performing a pagination at page {page_number}",
            "scrapper_state": {
                "current_page": page_number,
                "total_of_pages": max_pages,
                "search_params": {
                    "judgment_date": {
                        "start_at": datetime.strptime(
                            search_start_date, "%d/%m/%Y"
                        ).strftime("%Y%m%d"),
                        "end_at": datetime.strptime(
                            search_end_date, "%d/%m/%Y"
                        ).strftime("%Y%m%d"),
                    }
                },
            },
        }
    }

    raise e
