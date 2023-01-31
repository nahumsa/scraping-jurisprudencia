
from strategy.abstract import AbstractStrategy


class Context:
    def __init__(self, strategy: AbstractStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: AbstractStrategy):
        self._strategy = strategy

    def execute_strategy(self, a, b):
        return self._strategy.execute(a, b)