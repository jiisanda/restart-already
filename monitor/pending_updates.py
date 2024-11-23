from monitor.base import BaseMonitor, MonitorResult


class PendingUpdate(BaseMonitor):
    def check(self) -> MonitorResult:
        ...
