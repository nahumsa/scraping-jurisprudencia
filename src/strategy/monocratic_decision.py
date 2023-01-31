from enum import Enum
from typing import Callable, Any
from repositories.abstract import AbstractRepository
from .abstract import AbstractStrategy

class MonocraticDecisionStrategy(AbstractStrategy):
    def execute(xpath: Enum,
                repository: AbstractRepository,
                process_function: Callable[[Enum, AbstractRepository], Any]) -> Any:
        return process_function(x_path_enum=xpath, repository=repository)