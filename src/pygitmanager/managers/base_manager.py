from abc import ABC, abstractmethod

class BaseManagerClass(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def get_arguments(self):
        pass