import sys
from PyQt5.QtWidgets import QApplication
from controllers.login_controller import LoginController
import views.button_rc

def main():
    app = QApplication(sys.argv)

    login_controller = LoginController()

    # 显示登录窗口
    login_controller.show()

    # 执行应用程序的事件循环
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
