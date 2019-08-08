from abc import ABC, abstractmethod


class State(ABC):
    def __init__(self, state_machine):
        self._state_machine = state_machine

    @abstractmethod
    def init(self):
        pass

    @abstractmethod
    def cleanup(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def resume(self):
        pass

    @abstractmethod
    def pause(self):
        pass

    @abstractmethod
    def __repr__(self) -> str:
        return __class__.__name__
