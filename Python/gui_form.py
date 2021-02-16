from typing import Callable

from PyQt5.QtWidgets import QWidget, QBoxLayout, QPushButton
from PyQt5.QtCore import Qt


class GUIForm(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)

        layout = QBoxLayout(QBoxLayout.TopToBottom)

        self.btn_save = QPushButton(parent=self, text='정보 저장')
        self.btn_run = QPushButton(parent=self, text='클라이언트 실행')

        layout.addWidget(self.btn_save)
        layout.addWidget(self.btn_run)

        self.setLayout(layout)
