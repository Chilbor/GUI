import sys
from PyQt5.QtWidgets import QApplication, QWidget


def create_app():
    print("create_app")
    crt_app = QApplication(sys.argv)
    crt_win = QWidget()
    crt_win.resize(400, 200)
    crt_win.move(300, 300)
    crt_win.setWindowTitle("My First Python Application")
    crt_win.show()
    sys.exit(crt_app.exec_())


if __name__ == '__main__':
    create_app()
