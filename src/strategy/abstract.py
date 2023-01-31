from enum import Enum
from typing import Callable, Any
from repositories.abstract import AbstractRepository
from abc import ABC, abstractmethod

class AbstractStrategy(ABC):
    @abstractmethod
    def execute(self,
                xpath: Enum,
                repository: AbstractRepository,
                process_function: Callable[[Enum, AbstractRepository], Any]):
        pass