from enum import Enum
from typing import Callable, Any
from repositories.abstract import AbstractRepository
from strategy.abstract import AbstractStrategy

class StrategyContext:
    def __init__(self, strategy: AbstractStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: AbstractStrategy):
        self._strategy = strategy

    def execute_strategy(self,
                         xpath: Enum,
                         repository: AbstractRepository,
                         process_function: Callable[[Enum, AbstractRepository], Any]):

        return self._strategy.execute(xpath=xpath,
                                      repository=repository,
                                      process_function=process_function)