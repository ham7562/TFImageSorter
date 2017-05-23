# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
      
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800,300 )
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.startDirT = QtWidgets.QTextEdit(self.centralwidget)
        self.startDirT.setGeometry(QtCore.QRect(20, 40, 631, 41))
        self.startDirT.setObjectName("startDirT")
        
        
        self.startDirB = QtWidgets.QPushButton(self.centralwidget)
        self.startDirB.setGeometry(QtCore.QRect(660, 40, 121, 41))
        self.startDirB.setObjectName("startDirB")
        self.startDirB.clicked.connect(self.dirBClicked)
        
        
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 171, 16))
        self.label.setObjectName("label")
        self.endDirT = QtWidgets.QTextEdit(self.centralwidget)
        self.endDirT.setGeometry(QtCore.QRect(20, 120, 631, 41))
        self.endDirT.setObjectName("endDirT")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 171, 16))
        self.label_2.setObjectName("label_2")
        self.endDirB = QtWidgets.QPushButton(self.centralwidget)
        self.endDirB.setGeometry(QtCore.QRect(660, 120, 121, 41))
        self.endDirB.setObjectName("endDirB")
        self.startB = QtWidgets.QPushButton(self.centralwidget)
        self.startB.setGeometry(QtCore.QRect(500, 190, 131, 41))
        self.startB.setObjectName("startB")
        self.closeB = QtWidgets.QPushButton(self.centralwidget)
        self.closeB.setGeometry(QtCore.QRect(650, 190, 131, 41))
        self.closeB.setObjectName("closeB")
        
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        
        
        
    def dirBClicked(self):
       dirtxt = QFileDialog.getExistingDirectory(self)
       self.startDirT.setText(dirtxt)
        
        


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "이미지 분류기"))
        self.startDirB.setText(_translate("MainWindow", "경로"))
        self.label.setText(_translate("MainWindow", "분류할 이미지 경로 지정"))
        self.label_2.setText(_translate("MainWindow", "분류될 경로 지정"))
        self.endDirB.setText(_translate("MainWindow", "경로"))
        self.startB.setText(_translate("MainWindow", "분류 시작"))
        self.closeB.setText(_translate("MainWindow", "종료"))
        
    
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

