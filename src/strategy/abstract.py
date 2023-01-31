from abc import ABC, abstractmethod

class AbstractStrategy(ABC):
    @abstractmethod
    def execute(self):
        pass