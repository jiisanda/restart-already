from monitor.base import BaseMonitor, MonitorResult


class UptimeMonitor(BaseMonitor):
    def check(self) -> MonitorResult:
        ...
