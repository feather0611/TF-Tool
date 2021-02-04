# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from os.path import expanduser

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(541, 339)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setObjectName("label_2")
        self.Origin_context_selButton = QtWidgets.QPushButton(self.centralwidget)
        self.Origin_context_selButton.setGeometry(QtCore.QRect(450, 16, 71, 31))
        self.Origin_context_selButton.setObjectName("Origin_context_selButton")
        self.Split_result_selButton = QtWidgets.QPushButton(self.centralwidget)
        self.Split_result_selButton.setGeometry(QtCore.QRect(450, 56, 71, 31))
        self.Split_result_selButton.setObjectName("Split_result_selButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.TF_output__selButton = QtWidgets.QPushButton(self.centralwidget)
        self.TF_output__selButton.setGeometry(QtCore.QRect(450, 96, 71, 31))
        self.TF_output__selButton.setObjectName("TF_output__selButton")
        self.Origin_context_dir = QtWidgets.QLineEdit(self.centralwidget)
        self.Origin_context_dir.setEnabled(True)
        self.Origin_context_dir.setGeometry(QtCore.QRect(140, 20, 301, 21))
        self.Origin_context_dir.setReadOnly(True)
        self.Origin_context_dir.setObjectName("Origin_context_dir")
        self.Split_result_dir = QtWidgets.QLineEdit(self.centralwidget)
        self.Split_result_dir.setEnabled(True)
        self.Split_result_dir.setGeometry(QtCore.QRect(140, 60, 301, 21))
        self.Split_result_dir.setReadOnly(True)
        self.Split_result_dir.setObjectName("Split_result_dir")
        self.TF_output_dir = QtWidgets.QLineEdit(self.centralwidget)
        self.TF_output_dir.setEnabled(True)
        self.TF_output_dir.setGeometry(QtCore.QRect(140, 100, 301, 21))
        self.TF_output_dir.setReadOnly(True)
        self.TF_output_dir.setObjectName("TF_output_dir")
        self.hintBox = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.hintBox.setEnabled(True)
        self.hintBox.setGeometry(QtCore.QRect(20, 170, 501, 101))
        self.hintBox.setReadOnly(True)
        self.hintBox.setObjectName("hintBox")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 140, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.runButton = QtWidgets.QPushButton(self.centralwidget)
        self.runButton.setGeometry(QtCore.QRect(410, 280, 113, 32))
        self.runButton.setObjectName("runButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Origin_context_selButton.clicked.connect(lambda: self.chooseDir('origin'))
        self.Split_result_selButton.clicked.connect(lambda: self.chooseDir('split'))
        self.TF_output__selButton.clicked.connect(lambda: self.chooseDir('TF'))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "詞頻計算程式"))
        self.label.setText(_translate("MainWindow", "原始文本目錄"))
        self.label_2.setText(_translate("MainWindow", "斷詞結果輸出目錄"))
        self.Origin_context_selButton.setText(_translate("MainWindow", "選取"))
        self.Split_result_selButton.setText(_translate("MainWindow", "選取"))
        self.label_3.setText(_translate("MainWindow", "詞頻結果輸出目錄"))
        self.TF_output__selButton.setText(_translate("MainWindow", "選取"))
        self.label_4.setText(_translate("MainWindow", "訊息提示"))
        self.runButton.setText(_translate("MainWindow", "執行"))

    def chooseDir(self, target):
        dir = QFileDialog.getExistingDirectory(
                None,
                "Open a folder",
                expanduser("~"),
                QFileDialog.ShowDirsOnly)
        if dir!='':
            if target=='origin':
                self.Origin_context_dir.setText(str(dir)+'/')
            elif target=='split':
                self.Split_result_dir.setText(str(dir)+'/')
            elif target=='TF':
                self.TF_output_dir.setText(str(dir)+'/')｀｀