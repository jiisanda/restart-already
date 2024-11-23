from typing import Dict, Any, List

from monitor.base import MonitorResult, BaseMonitor


class MonitoringSystem:
    def __init__(self, config: Dict[str, Any]):
        self.monitors = {}
        self.config = config

    def _monitors_setup(self):
        """monitors with specific configs"""
        ...

    def check_all(self) -> List[MonitorResult]:
        """run monitors anc check all"""
        ...

    def get_monitor(self, name: str) -> BaseMonitor:
        """get monitor by name"""
        return self.monitors.get(name)
