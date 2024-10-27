from PyQt6 import QtCore
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import QCoreApplication

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

import threading

from src.ProgramProcessManager import ProgramProcessManager
from src.View import Ui_MainWindow

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.draggable = False
        self.old_pos = None
        self.process_manager = ProgramProcessManager()

        self.ui.exit_button.clicked.connect(QCoreApplication.quit)
        self.ui.minimize_button.clicked.connect(self.showMinimized)

        self.ui.run_button.clicked.connect(self.run)
        self.ui.code_input.textChanged.connect(self.onTextChanged)
        self.ui.code_output.enter_signal.connect(self.sendInput)

    def sendInput(self):
        text = self.ui.code_output.toPlainText()
        user_input = text[sum(self.process_manager.output_length):len(text)]
        self.process_manager.output_length.append(len(user_input) + 1)
        self.process_manager.writeSTDIN(user_input)

    def run(self):
        self.ui.code_output.clear()
        code = self.ui.code_input.toPlainText()
        language = self.ui.language_select.currentText()
        thread = threading.Thread(target = self.process_manager.runCode, args = (self.ui.code_output.insertPlainText, code, language), daemon = True)
        thread.start()

    def onTextChanged(self):
        markup = highlight(
        self.ui.code_input.toPlainText(),
        get_lexer_by_name(
            self.ui.language_select.currentText(),
            stripnl=False,
            ensurenl=False,
        ),
        HtmlFormatter(
                lineseparator="<br />",
                prestyles=f"white-space:pre-wrap;",
                noclasses=True,
                nobackground=True,
            )
        )

        position = self.ui.code_input.textCursor().position()

        self.ui.code_input.blockSignals(True)
        self.ui.code_input.setHtml(markup)
        self.ui.code_input.blockSignals(False)

        cursor = self.ui.code_input.textCursor()
        cursor.setPosition(position)
        self.ui.code_input.setTextCursor(cursor)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            if self.ui.frame_4.geometry().contains(event.pos()):
                self.draggable = True
                self.old_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if self.draggable:
            delta = event.globalPosition().toPoint() - self.old_pos
            self.move(self.pos() + delta)
            self.old_pos = event.globalPosition().toPoint()

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.draggable = False

            