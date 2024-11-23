from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional, Dict, Any


class MonitorStatus(Enum):
    OK = "ok"
    WARNING = "warning"
    CRITICAL = "critical"


class Severity(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3


@dataclass
class MonitorResult:
    status: MonitorStatus
    severity: Severity
    message: str
    details: Optional[Dict[str, Any]] = None
    timestamp: Optional[datetime] = None


class BaseMonitor(ABC):
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self._observers = []

    @abstractmethod
    def check(self) -> MonitorResult:
        """monitoring logic"""
        ...

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self, result: MonitorResult):
        ...
