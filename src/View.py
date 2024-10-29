from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QTextEdit

class TextEdit(QTextEdit):
    enter_signal = pyqtSignal(str)

    def keyPressEvent(self, event):
        if event.key() == 16777220 or event.key() == 16777221:
                self.enter_signal.emit("Enter")
        super().keyPressEvent(event)

    def mousePressEvent(self, event):
        # Do nothing on mouse press
        pass

class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(804, 720)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 781, 691))
        self.frame.setStyleSheet("QFrame {\n"
"    background-color: #45474B;\n"
"    border-radius: 20px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(parent=self.frame)
        self.frame_2.setGeometry(QtCore.QRect(30, 60, 721, 361))
        self.frame_2.setStyleSheet("QFrame {\n"
"    background-color: #E1E1E1;\n"
"    border-radius: 20px;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.code_input = QtWidgets.QTextEdit(parent=self.frame_2)
        self.code_input.setGeometry(QtCore.QRect(10, 10, 701, 341))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        self.code_input.setFont(font)
        self.code_input.setStyleSheet("")
        self.code_input.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.code_input.setLineWidth(-6)
        self.code_input.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.code_input.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.code_input.setObjectName("code_input")
        self.frame_3 = QtWidgets.QFrame(parent=self.frame)
        self.frame_3.setGeometry(QtCore.QRect(30, 450, 721, 191))
        self.frame_3.setStyleSheet("QFrame {\n"
"    background-color: #E1E1E1;\n"
"    border-radius: 20px;\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.code_output = TextEdit(parent=self.frame_3)
        self.code_output.setGeometry(QtCore.QRect(10, 10, 701, 171))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        self.code_output.setFont(font)
        self.code_output.setObjectName("code_output")
        self.frame_4 = QtWidgets.QFrame(parent=self.frame)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 781, 58))
        self.frame_4.setStyleSheet("QFrame {\n"
"    background-color: rgba(0, 0, 0, 0)\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.exit_button = QtWidgets.QPushButton(parent=self.frame_4)
        self.exit_button.setGeometry(QtCore.QRect(740, 10, 31, 31))
        self.exit_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.exit_button.setStyleSheet("QPushButton {\n"
"    border-radius: 8px;\n"
"    background-color: #45474B;\n"
"    color: white;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    padding-bottom: 2;\n"
"    text-align: center;\n"
"}")
        self.exit_button.setFlat(False)
        self.exit_button.setObjectName("pushButton")
        self.minimize_button = QtWidgets.QPushButton(parent=self.frame_4)
        self.minimize_button.setGeometry(QtCore.QRect(710, 10, 31, 31))
        self.minimize_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.minimize_button.setStyleSheet("QPushButton {\n"
"    border-radius: 8px;\n"
"    background-color: #45474B;\n"
"    color: white;\n"
"    font-size: 36px;\n"
"    font-weight: bold;\n"
"    padding-bottom: 9;\n"
"    text-align: center;\n"
"}")
        self.minimize_button.setObjectName("pushButton_2")
        self.title = QtWidgets.QLabel(parent=self.frame_4)
        self.title.setGeometry(QtCore.QRect(20, 20, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(-1)
        font.setBold(False)
        self.title.setFont(font)
        self.title.setStyleSheet("QLabel {\n"
"    color: rgb(245, 245, 245);\n"
"    font-size: 15px;\n"
"}")
        self.title.setObjectName("label")
        self.language_select = QtWidgets.QComboBox(parent=self.frame_4)
        self.language_select.setGeometry(QtCore.QRect(130, 20, 81, 21))
        self.language_select.setStyleSheet("")
        self.language_select.setObjectName("language_select")
        self.language_select.addItem("")
        self.language_select.addItem("")
        self.language_select.addItem("")
        self.run_button = QtWidgets.QPushButton(parent=self.frame)
        self.run_button.setGeometry(QtCore.QRect(330, 654, 101, 25))
        self.run_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.run_button.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: #76ABAE;\n"
"}")
        self.run_button.setText("")
        self.run_button.setIconSize(QtCore.QSize(16, 16))
        self.run_button.setObjectName("run_button")
        self.run_button_label = QtWidgets.QLabel(parent=self.frame)
        self.run_button_label.setGeometry(QtCore.QRect(362, 659, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        self.run_button_label.setFont(font)
        self.run_button_label.setStyleSheet("QLabel {\n"
"    color: white;\n"
"    background-color: rgb(118, 171, 174);\n"
"}")
        self.run_button_label.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.code_input.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Terminal\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Segoe UI\'; font-size:9pt;\"><br /></p></body></html>"))
        self.title.setText(_translate("MainWindow", "Tiny-IDE"))
        self.exit_button.setText(_translate("MainWindow", "X"))
        self.minimize_button.setText(_translate("MainWindow", "-"))
        self.language_select.setItemText(0, _translate("MainWindow", "Python"))
        self.language_select.setItemText(1, _translate("MainWindow", "JavaScript"))
        self.language_select.setItemText(2, _translate("MainWindow", "C++"))
        self.run_button_label.setText(_translate("MainWindow", "Run"))
