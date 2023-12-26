# 窗口信息实体
class WindowInfo:
    hwnd: int
    title: str
    task_status: int
    current_task: str

    def __init__(self, hwnd, title):
        self.hwnd = hwnd
        self.title = title
        self.task_status = 0
        self.current_task = ""
