import abc

class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def get(self, reference):
        raise NotImplementedError