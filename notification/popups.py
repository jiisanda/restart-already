from monitor.base import MonitorResult, MonitorStatus


class NotificationObserver:
    def update(self, notification: MonitorResult):
        if notification.status != MonitorStatus.OK:
            ...
