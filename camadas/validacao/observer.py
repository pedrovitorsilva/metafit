from abc import ABC, abstractmethod



class Observer(ABC):
    @abstractmethod
    def atualizar(self, mensagem: str):
        pass


class LogObserver(Observer):
    def atualizar(self, mensagem: str):
        print(f"LOG: {mensagem}")
