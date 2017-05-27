# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os
import inception
import shutil

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 409)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.startDirT = QtWidgets.QTextEdit(self.centralwidget)
        self.startDirT.setGeometry(QtCore.QRect(20, 30, 631, 31))
        self.startDirT.setObjectName("startDirT")
        self.startDirB = QtWidgets.QPushButton(self.centralwidget)
        self.startDirB.setGeometry(QtCore.QRect(660, 30, 121, 31))
        self.startDirB.setObjectName("startDirB")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 171, 16))
        self.label.setObjectName("label")
        self.endDirT = QtWidgets.QTextEdit(self.centralwidget)
        self.endDirT.setGeometry(QtCore.QRect(20, 90, 631, 31))
        self.endDirT.setObjectName("endDirT")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 171, 16))
        self.label_2.setObjectName("label_2")
        self.endDirB = QtWidgets.QPushButton(self.centralwidget)
        self.endDirB.setGeometry(QtCore.QRect(660, 90, 121, 31))
        self.endDirB.setObjectName("endDirB")
        self.startB = QtWidgets.QPushButton(self.centralwidget)
        self.startB.setGeometry(QtCore.QRect(660, 150, 121, 191))
        self.startB.setObjectName("startB")
        self.LogTxet = QtWidgets.QTextEdit(self.centralwidget)
        self.LogTxet.setGeometry(QtCore.QRect(20, 150, 631, 192))
        self.LogTxet.setObjectName("LogTxet")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 56, 12))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.startDirB.clicked.connect(self.startDirBClicked)
        self.endDirB.clicked.connect(self.endDirBClicked)
        self.startB.clicked.connect(self.startBClicked)
        
        
                    
    def startDirBClicked(self):
        dirtxt = QtWidgets.QFileDialog.getExistingDirectory(None,'Open file', 'c:/')
        self.startDirT.setText(dirtxt)
       
    def endDirBClicked(self):
        dirtxt = QtWidgets.QFileDialog.getExistingDirectory(None,'Open file', 'c:/')
        self.endDirT.setPlainText(dirtxt)
       
       
    def startBClicked(self):
        inception.maybe_download_and_extract()
        startDirText = self.startDirT.toPlainText()
        endDirText = self.endDirT.toPlainText()
        filenames = os.listdir(startDirText)
        for filename in filenames:
            full_filename = os.path.join(startDirText, filename)
            self.LogTxet.append(full_filename)
            inception.run_other_program_on_image(full_filename)
            f = open("image.log.txt",'r')
            while True:
                line = f.readline()
                if not line: break
                self.LogTxet.append(line)
                if os.path.isdir(endDirText + '/' + line):
                    shutil.move(full_filename,endDirText + '/' + line +'/' + filename)
                else:
                    os.mkdir(endDirText + '/' + line)
                    shutil.move(full_filename,endDirText + '/' + line +'/' + filename)
            f.close()
            os.remove("image.log.txt")
        
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startDirB.setText(_translate("MainWindow", "경로"))
        self.label.setText(_translate("MainWindow", "분류할 이미지 경로 지정"))
        self.label_2.setText(_translate("MainWindow", "분류될 경로 지정"))
        self.endDirB.setText(_translate("MainWindow", "경로"))
        self.startB.setText(_translate("MainWindow", "분류 시작"))
        self.label_3.setText(_translate("MainWindow", "로그"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

