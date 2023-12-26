import os

from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
from Mushroom.mediators.log_mediator import LogMediator
from Mushroom.models.daily_task import DailyTask
from Mushroom.models.window_info import WindowInfo
from Mushroom.services.daily_task import DailyTaskService
from Mushroom.utils.dm import DM
from Mushroom.views.main2 import Ui_MainWindow


class MainController(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.windows = []
        dll_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'resources'))
        self.dm = DM(dll_path + './dmreg.dll', dll_path + './dm.dll')
        self.dm.Reg('mh84909b3bf80d45c618136887775ccc90d27d7', 'm6gbr8n5arik7k7')
        # 初始化LogMediator，并传递给MainWindow

        self.log_mediator = LogMediator()
        # 连接LogMediator的信号到槽函数
        self.log_mediator.log_signal.connect(self.handle_log_text)
        self.daily_task_service = DailyTaskService(self.log_mediator)

        # 初始化界面
        self.init_ui()
        self.init_data()

    def init_ui(self):
        # 初始化页面，事件绑定等
        self.windowTab.tabBarClicked.connect(self.handle_change_window)

    def init_data(self):
        self.setStatusTip("[到期时间: 2023-12-31 10:11:12]")
        self.load_windows()

    # 后续考虑使用多线程异步加载
    def load_windows(self):
        hwnds = self.dm.EnumWindow(0, "", "LDPlayerMainFrame", 2)
        if hwnds:
            for index, hwnd in enumerate(hwnds.split(",")):
                title = self.dm.GetWindowTitle(int(hwnd))
                self.windowTab.insertTab(index, QtWidgets.QWidget(), title)
                self.windows.append(WindowInfo(self.dm.GetWindow(int(hwnd), 1), title))

    def handle_change_window(self, index):
        window_info = self.windows[index]
        self.window_name_label.setText(window_info.title)
        self.window_hwnd_label.setText(str(window_info.hwnd))
        #load config

    def hand_bind_window(self):
        print("handle_bind_window")

    def handle_log_text(self, message):
        print(message)

    def handle_start_daily_task(self):
        # 模拟登录成功
        dailyTask = DailyTask()
        dailyTask.daily_task_cl = self.daily_task_cl.isChecked()
        dailyTask.daily_task_cl_level = self.daily_task_cl_level.currentIndex()
        dailyTask.daily_task_cl_buff_1 = self.daily_task_cl_buff_1.isChecked()
        dailyTask.daily_task_cl_buff_2 = self.daily_task_cl_buff_2.isChecked()
        dailyTask.daily_task_cl_buff_3 = self.daily_task_cl_buff_3.isChecked()
        dailyTask.daily_task_cl_buff_4 = self.daily_task_cl_buff_4.isChecked()
        dailyTask.daily_task_cl_buff_5 = self.daily_task_cl_buff_5.isChecked()
        dailyTask.daily_task_cl_buff_6 = self.daily_task_cl_buff_6.isChecked()
        dailyTask.daily_task_jy = self.daily_task_jy.isChecked()
        dailyTask.daily_task_jy_open = self.daily_task_jy_open.isChecked()
        dailyTask.daily_task_jg = self.daily_task_jg.isChecked()
        dailyTask.daily_task_jzt = self.daily_task_jzt.isChecked()
        dailyTask.daily_task_zc = self.daily_task_zc.isChecked()
        if self.daily_task_zc_day_1.isChecked():
            dailyTask.daily_task_zc_day = 1
        elif self.daily_task_zc_day_2.isChecked():
            dailyTask.daily_task_zc_day = 2
        elif self.daily_task_zc_day_3.isChecked():
            dailyTask.daily_task_zc_day = 3
        elif self.daily_task_zc_day_4.isChecked():
            dailyTask.daily_task_zc_day = 4
        elif self.daily_task_zc_day_5.isChecked():
            dailyTask.daily_task_zc_day = 5

        dailyTask.daily_task_ty = self.daily_task_ty.isChecked()
        if self.daily_task_ty_order_1.isChecked():
            dailyTask.daily_task_ty_order = 1
        elif self.daily_task_ty_order_4.isChecked():
            dailyTask.daily_task_ty_order = 2
        elif self.daily_task_ty_order_4.isChecked():
            dailyTask.daily_task_ty_order = 3
        elif self.daily_task_ty_order_4.isChecked():
            dailyTask.daily_task_ty_order = 4

        dailyTask.daily_task_jh = self.daily_task_jh.isChecked()

        dailyTask.daily_task_cy = self.daily_task_cy.isChecked()
        self.daily_task_service.start_task(task=dailyTask, dm=self.dm)
