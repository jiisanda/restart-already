from monitor.base import BaseMonitor, MonitorResult


class TempFileMonitor(BaseMonitor):
    def check(self) -> MonitorResult:
        ...
