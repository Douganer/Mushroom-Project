from PyQt5.QtCore import QObject, pyqtSignal


class LogMediator(QObject):
    log_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def log(self, message):
        # 发送信号，将日志传递到主窗口
        self.log_signal.emit(message)
