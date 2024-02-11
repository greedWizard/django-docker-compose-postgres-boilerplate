from abc import ABC, abstractmethod


class BaseSenderService(ABC):
    @abstractmethod
    def send_code(self, code: str) -> None:
        ...
