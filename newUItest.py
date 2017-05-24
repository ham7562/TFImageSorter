
import sys

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
      
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800,400 )
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.startDirT = QtWidgets.QTextEdit(self.centralwidget)
        self.startDirT.setGeometry(QtCore.QRect(20, 40, 630, 41))
        self.startDirT.setObjectName("startDirT")
        
        
        self.startDirB = QtWidgets.QPushButton(self.centralwidget)
        self.startDirB.setGeometry(QtCore.QRect(660, 40, 120, 40))
        self.startDirB.setObjectName("startDirB")
        
        
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 171, 16))
        self.label.setObjectName("label")
        
        self.endDirT = QtWidgets.QTextEdit(self.centralwidget)
        self.endDirT.setGeometry(QtCore.QRect(20, 120, 630, 41))
        self.endDirT.setObjectName("endDirT")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 171, 16))
        self.label_2.setObjectName("label_2")
        
        self.endDirB = QtWidgets.QPushButton(self.centralwidget)
        self.endDirB.setGeometry(QtCore.QRect(660, 120, 120, 40))
        self.endDirB.setObjectName("endDirB")
        
        self.startB = QtWidgets.QPushButton(self.centralwidget)
        self.startB.setGeometry(QtCore.QRect(660, 200, 120, 40))
        self.startB.setObjectName("startB")
        

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20,190,630,120))
        self.textBrowser.setObjectName("textBrowser")
        
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
        
        
        
        


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "이미지 분류기"))
        self.startDirB.setText(_translate("MainWindow", "경로"))
        self.label.setText(_translate("MainWindow", "분류할 이미지 경로 지정"))
        self.label_2.setText(_translate("MainWindow", "분류될 경로 지정"))
        self.endDirB.setText(_translate("MainWindow", "경로"))
        self.startB.setText(_translate("MainWindow", "분류 시작"))
        
    
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



