from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def atualizar(self, mensagem: str):
        print(f"LOG: {mensagem}")


class LogObserver(Observer):
    def atualizar(self, mensagem: str):
        print(f"LOG: {mensagem}")
