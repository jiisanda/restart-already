from monitor.base import BaseMonitor, MonitorResult


class CpuRamMonitor(BaseMonitor):
    def check(self) -> MonitorResult:
        ...
