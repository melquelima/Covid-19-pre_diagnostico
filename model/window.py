# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(799, 621)
        MainWindow.setStyleSheet("background: #2c3338;\n"
"    color: #a5a8ab;\n"
"    font: 87.5%/1.5em \'Open Sans\', sans-serif;\n"
"    margin: 0;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 781, 291))
        self.groupBox.setObjectName("groupBox")
        self.rb2 = QtWidgets.QRadioButton(self.groupBox)
        self.rb2.setGeometry(QtCore.QRect(30, 150, 181, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.rb2.setFont(font)
        self.rb2.setObjectName("rb2")
        self.rb3 = QtWidgets.QRadioButton(self.groupBox)
        self.rb3.setGeometry(QtCore.QRect(30, 180, 181, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.rb3.setFont(font)
        self.rb3.setObjectName("rb3")
        self.rb1 = QtWidgets.QRadioButton(self.groupBox)
        self.rb1.setEnabled(True)
        self.rb1.setGeometry(QtCore.QRect(30, 120, 181, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.rb1.setFont(font)
        self.rb1.setObjectName("rb1")
        self.next = QtWidgets.QPushButton(self.groupBox)
        self.next.setGeometry(QtCore.QRect(30, 240, 171, 31))
        self.next.setStyleSheet("QPushButton{background: #167aaa;\n"
"    border: 0;\n"
"    width: 100%;\n"
"    height: 40px;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"    cursor: pointer;\n"
"    transition: background 0.3s ease-in-out;\n"
"font-family: \'Open Sans\', Arial, sans-serif;\n"
"    font-size: 16px;\n"
"    line-height: 1.5em;\n"
"    padding: 0;\n"
"    -webkit-appearance: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"  background: #106892;\n"
"}")
        self.next.setObjectName("next")
        self.tb_pergunta = QtWidgets.QTextBrowser(self.groupBox)
        self.tb_pergunta.setGeometry(QtCore.QRect(20, 20, 751, 101))
        self.tb_pergunta.setStyleSheet("QTextBrowser{\n"
"    border: 0;\n"
"   \n"
"}")
        self.tb_pergunta.setObjectName("tb_pergunta")
        self.rb4 = QtWidgets.QRadioButton(self.groupBox)
        self.rb4.setGeometry(QtCore.QRect(210, 120, 301, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.rb4.setFont(font)
        self.rb4.setObjectName("rb4")
        self.rb6 = QtWidgets.QRadioButton(self.groupBox)
        self.rb6.setGeometry(QtCore.QRect(210, 180, 301, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.rb6.setFont(font)
        self.rb6.setObjectName("rb6")
        self.rb5 = QtWidgets.QRadioButton(self.groupBox)
        self.rb5.setGeometry(QtCore.QRect(210, 150, 301, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.rb5.setFont(font)
        self.rb5.setObjectName("rb5")
        self.rb9 = QtWidgets.QRadioButton(self.groupBox)
        self.rb9.setGeometry(QtCore.QRect(510, 180, 261, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.rb9.setFont(font)
        self.rb9.setObjectName("rb9")
        self.rb7 = QtWidgets.QRadioButton(self.groupBox)
        self.rb7.setGeometry(QtCore.QRect(510, 120, 261, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.rb7.setFont(font)
        self.rb7.setObjectName("rb7")
        self.rb8 = QtWidgets.QRadioButton(self.groupBox)
        self.rb8.setGeometry(QtCore.QRect(510, 150, 261, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.rb8.setFont(font)
        self.rb8.setObjectName("rb8")
        self.inputText = QtWidgets.QLineEdit(self.groupBox)
        self.inputText.setGeometry(QtCore.QRect(20, 70, 351, 31))
        self.inputText.setObjectName("inputText")
        self.cb4 = QtWidgets.QCheckBox(self.groupBox)
        self.cb4.setGeometry(QtCore.QRect(210, 120, 291, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cb4.setFont(font)
        self.cb4.setObjectName("cb4")
        self.cb5 = QtWidgets.QCheckBox(self.groupBox)
        self.cb5.setGeometry(QtCore.QRect(210, 150, 291, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cb5.setFont(font)
        self.cb5.setObjectName("cb5")
        self.cb9 = QtWidgets.QCheckBox(self.groupBox)
        self.cb9.setGeometry(QtCore.QRect(510, 180, 261, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cb9.setFont(font)
        self.cb9.setObjectName("cb9")
        self.cb6 = QtWidgets.QCheckBox(self.groupBox)
        self.cb6.setGeometry(QtCore.QRect(210, 180, 291, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cb6.setFont(font)
        self.cb6.setObjectName("cb6")
        self.cb7 = QtWidgets.QCheckBox(self.groupBox)
        self.cb7.setGeometry(QtCore.QRect(510, 120, 261, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cb7.setFont(font)
        self.cb7.setObjectName("cb7")
        self.cb3 = QtWidgets.QCheckBox(self.groupBox)
        self.cb3.setGeometry(QtCore.QRect(30, 180, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cb3.setFont(font)
        self.cb3.setObjectName("cb3")
        self.cb1 = QtWidgets.QCheckBox(self.groupBox)
        self.cb1.setGeometry(QtCore.QRect(30, 120, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cb1.setFont(font)
        self.cb1.setObjectName("cb1")
        self.cb2 = QtWidgets.QCheckBox(self.groupBox)
        self.cb2.setGeometry(QtCore.QRect(30, 150, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cb2.setFont(font)
        self.cb2.setObjectName("cb2")
        self.cb8 = QtWidgets.QCheckBox(self.groupBox)
        self.cb8.setGeometry(QtCore.QRect(510, 150, 261, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cb8.setFont(font)
        self.cb8.setObjectName("cb8")
        self.hiddenchk = QtWidgets.QRadioButton(self.groupBox)
        self.hiddenchk.setGeometry(QtCore.QRect(520, 250, 82, 17))
        self.hiddenchk.setObjectName("hiddenchk")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 360, 781, 201))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 31, 16))
        self.label_2.setObjectName("label_2")
        self.l_nome = QtWidgets.QLabel(self.groupBox_2)
        self.l_nome.setGeometry(QtCore.QRect(60, 22, 139, 13))
        self.l_nome.setObjectName("l_nome")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 40, 47, 13))
        self.label_4.setObjectName("label_4")
        self.l_idade = QtWidgets.QLabel(self.groupBox_2)
        self.l_idade.setGeometry(QtCore.QRect(60, 41, 139, 13))
        self.l_idade.setObjectName("l_idade")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(20, 60, 47, 13))
        self.label_6.setObjectName("label_6")
        self.l_sexo = QtWidgets.QLabel(self.groupBox_2)
        self.l_sexo.setGeometry(QtCore.QRect(60, 60, 139, 13))
        self.l_sexo.setObjectName("l_sexo")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(630, 60, 131, 80))
        self.groupBox_3.setStyleSheet("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.l_gr = QtWidgets.QLabel(self.groupBox_3)
        self.l_gr.setGeometry(QtCore.QRect(10, 20, 111, 51))
        self.l_gr.setStyleSheet("QLabel{\n"
"    background:#ffc107;\n"
"    color:black\n"
"}")
        self.l_gr.setAlignment(QtCore.Qt.AlignCenter)
        self.l_gr.setObjectName("l_gr")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 80, 181, 51))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setGeometry(QtCore.QRect(10, 20, 47, 13))
        self.label_8.setObjectName("label_8")
        self.l_r4 = QtWidgets.QLabel(self.groupBox_4)
        self.l_r4.setGeometry(QtCore.QRect(70, 20, 101, 13))
        self.l_r4.setStyleSheet("QLabel{\n"
"    color:red\n"
"}")
        self.l_r4.setAlignment(QtCore.Qt.AlignCenter)
        self.l_r4.setObjectName("l_r4")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_5.setGeometry(QtCore.QRect(210, 10, 231, 181))
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_10 = QtWidgets.QLabel(self.groupBox_5)
        self.label_10.setGeometry(QtCore.QRect(10, 20, 47, 13))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_5)
        self.label_11.setGeometry(QtCore.QRect(70, 20, 47, 13))
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.groupBox_5)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 40, 211, 131))
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setStyleSheet("QTextBrowser{\n"
"    border: 0;\n"
"   \n"
"}")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_6.setGeometry(QtCore.QRect(20, 140, 181, 51))
        self.groupBox_6.setObjectName("groupBox_6")
        self.label_12 = QtWidgets.QLabel(self.groupBox_6)
        self.label_12.setGeometry(QtCore.QRect(10, 20, 47, 13))
        self.label_12.setObjectName("label_12")
        self.l_r6 = QtWidgets.QLabel(self.groupBox_6)
        self.l_r6.setGeometry(QtCore.QRect(70, 20, 101, 13))
        self.l_r6.setStyleSheet("QLabel{\n"
"    color:red\n"
"}")
        self.l_r6.setAlignment(QtCore.Qt.AlignCenter)
        self.l_r6.setObjectName("l_r6")
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_7.setGeometry(QtCore.QRect(450, 10, 161, 51))
        self.groupBox_7.setObjectName("groupBox_7")
        self.label_14 = QtWidgets.QLabel(self.groupBox_7)
        self.label_14.setGeometry(QtCore.QRect(10, 20, 47, 13))
        self.label_14.setObjectName("label_14")
        self.l_r7 = QtWidgets.QLabel(self.groupBox_7)
        self.l_r7.setGeometry(QtCore.QRect(65, 20, 91, 13))
        self.l_r7.setStyleSheet("QLabel{\n"
"    color:orange\n"
"}")
        self.l_r7.setAlignment(QtCore.Qt.AlignCenter)
        self.l_r7.setObjectName("l_r7")
        self.groupBox_8 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_8.setGeometry(QtCore.QRect(450, 70, 161, 51))
        self.groupBox_8.setObjectName("groupBox_8")
        self.label_18 = QtWidgets.QLabel(self.groupBox_8)
        self.label_18.setGeometry(QtCore.QRect(10, 20, 47, 13))
        self.label_18.setObjectName("label_18")
        self.l_r8 = QtWidgets.QLabel(self.groupBox_8)
        self.l_r8.setGeometry(QtCore.QRect(65, 20, 91, 13))
        self.l_r8.setStyleSheet("QLabel{\n"
"    color:lime\n"
"}")
        self.l_r8.setAlignment(QtCore.Qt.AlignCenter)
        self.l_r8.setObjectName("l_r8")
        self.groupBox_9 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_9.setGeometry(QtCore.QRect(450, 130, 161, 51))
        self.groupBox_9.setObjectName("groupBox_9")
        self.l_pre = QtWidgets.QLabel(self.groupBox_9)
        self.l_pre.setGeometry(QtCore.QRect(10, 20, 141, 16))
        self.l_pre.setStyleSheet("QLabel{\n"
"    color:lime\n"
"}")
        self.l_pre.setAlignment(QtCore.Qt.AlignCenter)
        self.l_pre.setObjectName("l_pre")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 560, 781, 21))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Covid-19 - Questionario"))
        self.groupBox.setTitle(_translate("MainWindow", "Perguntas"))
        self.rb2.setText(_translate("MainWindow", "RadioButton"))
        self.rb3.setText(_translate("MainWindow", "RadioButton"))
        self.rb1.setText(_translate("MainWindow", "RadioButton"))
        self.next.setText(_translate("MainWindow", "Próxima"))
        self.tb_pergunta.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt;\">7. Frequentou algum local nos últimos 7 dias com alguma incidência comprovada de COVID-19, ou ainda algum hospital com casos registrados da doença?</span></p></body></html>"))
        self.rb4.setText(_translate("MainWindow", "RadioButton"))
        self.rb6.setText(_translate("MainWindow", "RadioButton"))
        self.rb5.setText(_translate("MainWindow", "RadioButton"))
        self.rb9.setText(_translate("MainWindow", "RadioButton"))
        self.rb7.setText(_translate("MainWindow", "RadioButton"))
        self.rb8.setText(_translate("MainWindow", "RadioButton"))
        self.cb4.setText(_translate("MainWindow", "CheckBox"))
        self.cb5.setText(_translate("MainWindow", "CheckBox"))
        self.cb9.setText(_translate("MainWindow", "CheckBox"))
        self.cb6.setText(_translate("MainWindow", "CheckBox"))
        self.cb7.setText(_translate("MainWindow", "CheckBox"))
        self.cb3.setText(_translate("MainWindow", "CheckBox"))
        self.cb1.setText(_translate("MainWindow", "CheckBox"))
        self.cb2.setText(_translate("MainWindow", "CheckBox"))
        self.cb8.setText(_translate("MainWindow", "CheckBox"))
        self.hiddenchk.setText(_translate("MainWindow", "RadioButton"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Diagnostico"))
        self.label_2.setText(_translate("MainWindow", "Nome:"))
        self.l_nome.setText(_translate("MainWindow", "--"))
        self.label_4.setText(_translate("MainWindow", "Idade:"))
        self.l_idade.setText(_translate("MainWindow", "--"))
        self.label_6.setText(_translate("MainWindow", "Sexo:"))
        self.l_sexo.setText(_translate("MainWindow", "--"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Grupo de risco"))
        self.l_gr.setText(_translate("MainWindow", "Baixo"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Pergunta 4"))
        self.label_8.setText(_translate("MainWindow", "Resposta:"))
        self.l_r4.setText(_translate("MainWindow", "Sim"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Pergunta 5"))
        self.label_10.setText(_translate("MainWindow", "Resposta:"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:6pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; color:#ffaa00;\">a. Febre</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; color:#ffaa00;\">b. Tosse</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; color:#ffaa00;\">c. Cansaço ou fadiga</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; color:#ff0000;\">d. Dor ou pressão no peito</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; color:#ff0000;\">e. Perda de fala ou de movimento</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; color:#ff0000;\">f. Dificuldade para respirar ou falta de ar</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; color:#ffff00;\">g. Coriza</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; color:#ffff00;\">h. Dor de garganta</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; color:#ffff00;\">i. Dor de cabeça</span></p></body></html>"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Pergunta 6"))
        self.label_12.setText(_translate("MainWindow", "Resposta:"))
        self.l_r6.setText(_translate("MainWindow", "Sim"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Pergunta 7"))
        self.label_14.setText(_translate("MainWindow", "Resposta:"))
        self.l_r7.setText(_translate("MainWindow", "Não sei responder"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Pergunta 8"))
        self.label_18.setText(_translate("MainWindow", "Resposta:"))
        self.l_r8.setText(_translate("MainWindow", "Não"))
        self.groupBox_9.setTitle(_translate("MainWindow", "pre-diagnostico"))
        self.l_pre.setText(_translate("MainWindow", "0.564"))
        self.label.setText(_translate("MainWindow", "Desenvolvedores envolvidos: João Victor de Souza Carli - Thalita Botuem - Melque Lima "))
