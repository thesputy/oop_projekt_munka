from abc import ABC, abstractmethod

class Auto(ABC):
    def __init__(self, id, rendszam, tipus, berletidij):
        self.rendszam = rendszam
        self.tipus = tipus
        self.berletidij = berletidij
        self.id = id

    @abstractmethod
    def rent(self):
        pass

    @abstractmethod
    def unrent(self):
        pass