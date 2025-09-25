from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, data=None) -> None:
        pass

class Subject(ABC): # Observable
    def __init__(self) -> None:
        self._observers: list[Observer] = []

    def attach(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, data=None) -> None:
        for observer in self._observers:
            observer.update(data)


class Portfolio:
    """Observable that notifies when risk metrics change"""
    # TODO:
    # Observers: RiskManager, RebalanceEngine, ComplianceChecker
    # Triggers when VaR exceeds limits, correlation changes, etc.
