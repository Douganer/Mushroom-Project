from PyQt5.QtCore import QThread, pyqtSignal, QSize
from PyQt5.QtWidgets import QMessageBox, QMainWindow

from Mushroom.api.login_api import login, getNotice, unbind
from Mushroom.api.recharge_api import recharge
from Mushroom.api.register_api import register
from Mushroom.api.change_pwd_api import changePwd
from Mushroom.controllers.main_controller import MainController
from Mushroom.utils.credentials_util import CredentialsUtil
from Mushroom.views.login import Ui_LoginWindow


def show_error_message(title, message):
    # 弹出错误提示框
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Information)
    msg_box.setWindowTitle(title)
    msg_box.setText(message)
    msg_box.exec_()


class WorkerThread(QThread):
    update_signal = pyqtSignal(str)

    def run(self):
        # 在此执行需要在子线程中完成的任务
        notice = getNotice()
        self.update_signal.emit(notice)


class LoginController(QMainWindow, Ui_LoginWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.credentialsUtil = CredentialsUtil()
        self.main_controller = None

        # 初始化界面
        self.init_ui()
        self.init_data()

    def init_ui(self):
        # 连接登录按钮的点击事件到 handle_login 方法
        self.loginButton.clicked.connect(self.handle_login)
        self.loginUnBindButton.clicked.connect(self.handle_un_bind)
        self.rechargeButton.clicked.connect(self.handle_recharge)
        self.registerButton.clicked.connect(self.handle_register)
        self.changePwdButton.clicked.connect(self.handle_change_pwd)

    def init_data(self):
        # 连接登录按钮的点击事件到 handle_login 方法
        loginRememberMe = self.credentialsUtil.get_credential("loginRememberMe")

        if loginRememberMe == '1':
            self.loginName.setText(self.credentialsUtil.get_credential("loginName"))
            self.loginPwd.setText(self.credentialsUtil.get_credential("loginPwd"))
            self.loginRememberMe.setChecked(True)
            # 创建并启动工作线程

        self.worker_thread = WorkerThread()
        self.worker_thread.update_signal.connect(self.update_notice)
        self.worker_thread.start()

    def update_notice(self, message):
        self.noticeBrowser.setText(message)

    def handle_login(self):
        login_name = self.loginName.text()
        login_pwd = self.loginPwd.text()
        if login_name is None and login_pwd is None:
            show_error_message("登录失败", "用户名或密码不能为空")
            return

        suc, result = login(login_name, login_pwd)

        if suc:
            if self.loginRememberMe.isChecked():
                self.credentialsUtil.add_credential("loginName", self.loginName.text())
                self.credentialsUtil.add_credential("loginPwd", self.loginPwd.text())
                self.credentialsUtil.add_credential("loginRememberMe", 1)
            else:
                self.credentialsUtil.remove_credential("loginName")
                self.credentialsUtil.remove_credential("loginPwd")
                self.credentialsUtil.add_credential("loginRememberMe", 0)
            # 关闭登录窗口
            self.close()
            self.main_controller = MainController()
            self.main_controller.show()
        else:
            show_error_message("登录失败", result)

    def handle_recharge(self):
        suc, result = recharge(self.rechargeLoginName.text(), self.rechargeCardPwd.text())
        if suc:
            show_error_message("提示", "充值成功")
            self.rechargeLoginName.setText("")
            self.rechargeCardPwd.setText("")
        else:
            show_error_message("充值失败", result)

    def handle_register(self):
        login_name = self.registerLoginName.text()
        login_pwd = self.registerLoginPwd.text()
        login_super_pwd = self.registerLoginSuperPwd.text()
        card_pwd = self.registerCardPwd.text()

        suc, result = register(login_name, login_pwd, login_super_pwd, card_pwd)
        if suc:
            self.registerLoginName.setText("")
            self.registerLoginPwd.setText("")
            self.registerLoginSuperPwd.setText("")
            self.registerCardPwd.setText("")
            self.tabWidget.setCurrentIndex(0)
            show_error_message("提示", "注册成功")
        else:
            show_error_message("注册失败", result)

    def handle_change_pwd(self):
        login_name = self.changeLoginName.text()
        login_pwd_new = self.changeLoginPwdNew.text()
        login_super_pwd = self.changeLoginSuperPwd.text()

        suc, result = changePwd(login_name, login_pwd_new, login_super_pwd)
        if suc:
            self.changeLoginName.setText("")
            self.changeLoginPwdNew.setText("")
            self.changeLoginSuperPwd.setText("")

            show_error_message("提示", "修改成功")

            self.tabWidget.setCurrentIndex(0)
            self.loginPwd.setText("")
            self.loginPwd.setFocus()
        else:
            show_error_message("注册失败", result)

    def handle_un_bind(self):
        login_name = self.loginName.text()
        login_pwd = self.loginPwd.text()
        if login_name is None and login_pwd is None:
            show_error_message("登录失败", "用户名或密码不能为空")
            return

        suc, result = unbind(login_name, login_pwd)
        if suc:
            show_error_message("提示", "解绑成功")
        else:
            show_error_message("提示", result)
