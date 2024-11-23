from monitor.base import BaseMonitor, MonitorResult


class DiskSpaceMonitor(BaseMonitor):
    def check(self) -> MonitorResult:
        ...
