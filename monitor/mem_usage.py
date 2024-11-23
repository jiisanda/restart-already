from monitor.base import BaseMonitor, MonitorResult


class MemUsageMonitor(BaseMonitor):
    def check(self) -> MonitorResult:
        ...
