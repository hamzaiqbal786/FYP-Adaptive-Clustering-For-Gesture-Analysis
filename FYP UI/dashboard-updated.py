# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dashboard-updated.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1011, 520)
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
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 90, 491, 191))
        self.groupBox_2.setStyleSheet("background-color: rgb(241, 241, 241);")
        self.groupBox_2.setObjectName("groupBox_2")
        self.video_text_box = QtWidgets.QTextEdit(self.groupBox_2)
        self.video_text_box.setGeometry(QtCore.QRect(10, 50, 471, 31))
        self.video_text_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.video_text_box.setObjectName("video_text_box")
        self.startButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.startButton_2.setGeometry(QtCore.QRect(130, 120, 101, 41))
        self.startButton_2.setAutoFillBackground(False)
        self.startButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.startButton_2.setFlat(False)
        self.startButton_2.setObjectName("startButton_2")

        # opening file dialouge on button click
        self.startButton_2.clicked.connect(self.openFile)

        self.clear_button = QtWidgets.QPushButton(self.groupBox_2)
        self.clear_button.setGeometry(QtCore.QRect(250, 120, 101, 41))
        self.clear_button.setAutoFillBackground(False)
        self.clear_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.clear_button.setFlat(False)
        self.clear_button.setObjectName("clear_button")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(510, 90, 491, 191))
        self.groupBox_3.setStyleSheet("background-color: rgb(241, 241, 241);")
        self.groupBox_3.setObjectName("groupBox_3")
        self.startButton = QtWidgets.QPushButton(self.groupBox_3)
        self.startButton.setGeometry(QtCore.QRect(190, 130, 101, 41))
        self.startButton.setAutoFillBackground(False)
        self.startButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.startButton.setFlat(False)
        self.startButton.setObjectName("startButton")
        self.radioButton_25 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_25.setGeometry(QtCore.QRect(50, 30, 111, 17))
        self.radioButton_25.setChecked(False)
        self.radioButton_25.setAutoRepeat(False)
        self.radioButton_25.setObjectName("radioButton_25")
        self.radioButton_50 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_50.setGeometry(QtCore.QRect(330, 30, 111, 17))
        self.radioButton_50.setChecked(False)
        self.radioButton_50.setObjectName("radioButton_50")
        self.radioButton_75 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_75.setGeometry(QtCore.QRect(50, 80, 111, 17))
        self.radioButton_75.setChecked(True)
        self.radioButton_75.setObjectName("radioButton_75")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 300, 991, 171))
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
        self.label_cluster_predicted_result = QtWidgets.QLabel(self.groupBox_4)
        self.label_cluster_predicted_result.setGeometry(QtCore.QRect(650, 70, 261, 21))
        self.label_cluster_predicted_result.setObjectName("label_cluster_predicted_result")
        self.label_word_true_result = QtWidgets.QLabel(self.groupBox_4)
        self.label_word_true_result.setGeometry(QtCore.QRect(320, 120, 281, 21))
        self.label_word_true_result.setObjectName("label_word_true_result")
        self.label_word_predicted_result = QtWidgets.QLabel(self.groupBox_4)
        self.label_word_predicted_result.setGeometry(QtCore.QRect(640, 120, 281, 21))
        self.label_word_predicted_result.setObjectName("label_word_predicted_result")
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

    def openFile(self,MainWindow):
        fileName = str(QtWidgets.QFileDialog.getOpenFileName(None,"Select File", "","MOV FIles(*.mov);;AVI Files (*.avi);; MP4 FIles(*.mp4)"))
        self.video_text_box.setText(fileName)
        print(fileName)
        


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Adaptive Clustering For Gesture Analysis"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">ADAPTIVE CLUSTERING FOR GESTURE ANALYSIS</span></p></body></html>"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Input Video"))
        self.startButton_2.setText(_translate("MainWindow", "Select Video"))
        self.clear_button.setText(_translate("MainWindow", "Clear"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Frames Percentage"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.radioButton_25.setText(_translate("MainWindow", "First 25% Frames"))
        self.radioButton_50.setText(_translate("MainWindow", "First 50% Frames"))
        self.radioButton_75.setText(_translate("MainWindow", "First 75% Frames"))
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
        self.label_cluster_predicted_result.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">B</span></p><p align=\"center\"><br/></p></body></html>"))
        self.label_word_true_result.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Good Night</span><br/></p><p>410 70 281 21 &lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:10pt; font-weight:600;&quot;&gt;Cluster&lt;/span&gt;&lt;/p&gt;&lt;p&gt;&lt;br/&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt; 410 70 281 21 &lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:10pt; font-weight:600;&quot;&gt;Cluster&lt;/span&gt;&lt;/p&gt;&lt;p&gt;&lt;br/&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt; esources/&gt; </p></body></html>"))
        self.label_word_predicted_result.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Good Night</span><br/></p><p>410 70 281 21 &lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:10pt; font-weight:600;&quot;&gt;Cluster&lt;/span&gt;&lt;/p&gt;&lt;p&gt;&lt;br/&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt; 410 70 281 21 &lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:10pt; font-weight:600;&quot;&gt;Cluster&lt;/span&gt;&lt;/p&gt;&lt;p&gt;&lt;br/&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt; esources/&gt; </p></body></html>"))
        
        

    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    

