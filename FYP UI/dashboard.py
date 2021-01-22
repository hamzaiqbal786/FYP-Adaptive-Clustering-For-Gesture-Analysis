# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dashboard.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1011, 709)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-20, 10, 1041, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background-color: rgb(85, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"")
        
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 80, 481, 401))
        self.groupBox.setStyleSheet("background-color: rgb(241, 241, 241);")
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 441, 301))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setLineWidth(7)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.startButton = QtWidgets.QPushButton(self.groupBox)
        self.startButton.setGeometry(QtCore.QRect(130, 350, 101, 41))
        self.startButton.setAutoFillBackground(False)
        self.startButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.startButton.setFlat(False)
        self.startButton.setObjectName("startButton")
        self.stopButton = QtWidgets.QPushButton(self.groupBox)
        self.stopButton.setGeometry(QtCore.QRect(250, 350, 101, 41))
        self.stopButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.stopButton.setObjectName("stopButton")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(510, 290, 491, 191))
        self.groupBox_2.setStyleSheet("background-color: rgb(241, 241, 241);")
        self.groupBox_2.setObjectName("groupBox_2")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit.setGeometry(QtCore.QRect(10, 50, 471, 31))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.startButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.startButton_2.setGeometry(QtCore.QRect(130, 120, 101, 41))
        self.startButton_2.setAutoFillBackground(False)
        self.startButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.startButton_2.setFlat(False)
        self.startButton_2.setObjectName("startButton_2")
        self.startButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.startButton_3.setGeometry(QtCore.QRect(250, 120, 101, 41))
        self.startButton_3.setAutoFillBackground(False)
        self.startButton_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.startButton_3.setFlat(False)
        self.startButton_3.setObjectName("startButton_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(510, 80, 491, 191))
        self.groupBox_3.setStyleSheet("background-color: rgb(241, 241, 241);")
        self.groupBox_3.setObjectName("groupBox_3")
        self.startButton_4 = QtWidgets.QPushButton(self.groupBox_3)
        self.startButton_4.setGeometry(QtCore.QRect(190, 130, 101, 41))
        self.startButton_4.setAutoFillBackground(False)
        self.startButton_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.startButton_4.setFlat(False)
        self.startButton_4.setObjectName("startButton_4")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton.setGeometry(QtCore.QRect(50, 30, 111, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_2.setGeometry(QtCore.QRect(330, 30, 111, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_3.setGeometry(QtCore.QRect(50, 80, 111, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_4.setGeometry(QtCore.QRect(330, 80, 111, 17))
        self.radioButton_4.setObjectName("radioButton_4")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 500, 991, 171))
        self.groupBox_4.setStyleSheet("background-color: rgb(241, 241, 241);")
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setGeometry(QtCore.QRect(410, 20, 131, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(710, 20, 161, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setGeometry(QtCore.QRect(40, 70, 131, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setGeometry(QtCore.QRect(40, 120, 131, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setGeometry(QtCore.QRect(320, 70, 281, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setGeometry(QtCore.QRect(650, 70, 261, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_4)
        self.label_9.setGeometry(QtCore.QRect(320, 120, 281, 21))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_4)
        self.label_10.setGeometry(QtCore.QRect(640, 120, 281, 21))
        self.label_10.setObjectName("label_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1011, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Adaptive Clustering For Gesture Analysis"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">ADAPTIVE CLUSTERING FOR GESTURE ANALYSIS</span></p></body></html>"))
        self.groupBox.setTitle(_translate("MainWindow", "Web-Cam"))
        self.startButton.setText(_translate("MainWindow", "Start Recording"))
        self.stopButton.setText(_translate("MainWindow", "Stop Recording"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Input Video"))
        self.startButton_2.setText(_translate("MainWindow", "Start"))
        self.startButton_3.setText(_translate("MainWindow", "Clear"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Input Video"))
        self.startButton_4.setText(_translate("MainWindow", "Start"))
        self.radioButton.setText(_translate("MainWindow", "First 25% Frames"))
        self.radioButton_2.setText(_translate("MainWindow", "First 50% Frames"))
        self.radioButton_3.setText(_translate("MainWindow", "First 75% Frames"))
        self.radioButton_4.setText(_translate("MainWindow", "100% Frames"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Output"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">True Results</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Predicted Results</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Cluster Name</span></p></body></html><?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
"<ui version=\"4.0\">\n"
" <widget name=\"__qt_fake_top_level\">\n"
"  <widget class=\"QLabel\" name=\"label_3\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>30</x>\n"
"     <y>70</y>\n"
"     <width>131</width>\n"
"     <height>21</height>\n"
"    </rect>\n"
"   </property>\n"
"   <property name=\"text\">\n"
"    <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:12pt; font-weight:600;&quot;&gt;True Results&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>\n"
"   </property>\n"
"  </widget>\n"
" </widget>\n"
" <resources/>\n"
"</ui>\n"
""))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Word Name</span></p><p>30 70 131 21 &lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:12pt; font-weight:600;&quot;&gt;True Results&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt; </p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Cluster</span></p><p align=\"center\"><br/></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Cluster</span></p><p align=\"center\"><br/></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Word</span><br/></p><p>410 70 281 21 &lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:10pt; font-weight:600;&quot;&gt;Cluster&lt;/span&gt;&lt;/p&gt;&lt;p&gt;&lt;br/&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt; 410 70 281 21 &lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:10pt; font-weight:600;&quot;&gt;Cluster&lt;/span&gt;&lt;/p&gt;&lt;p&gt;&lt;br/&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt; esources/&gt; </p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Word</span><br/></p><p>410 70 281 21 &lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:10pt; font-weight:600;&quot;&gt;Cluster&lt;/span&gt;&lt;/p&gt;&lt;p&gt;&lt;br/&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt; 410 70 281 21 &lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:10pt; font-weight:600;&quot;&gt;Cluster&lt;/span&gt;&lt;/p&gt;&lt;p&gt;&lt;br/&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt; esources/&gt; </p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
