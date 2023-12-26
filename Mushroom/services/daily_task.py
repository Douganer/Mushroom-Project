from Mushroom.mediators.log_mediator import LogMediator
from Mushroom.models.daily_task import DailyTask
from Mushroom.services.helpers import move_click

from Mushroom.utils.dm import DM


# 日常任务service
class DailyTaskService:

    def __init__(self, logger: LogMediator):
        self.logger = logger

    def start_task(self, task: DailyTask, dm: DM):
        move_click(dm, 1190, 40)
        self.logger.log("12323123")
