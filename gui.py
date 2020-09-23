from PySide2.QtCore import QCoreApplication, QMetaObject, QRect
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import *

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
            Form.setFixedSize(405, 418)
            Form.setWindowIcon(QIcon('img/icon.ico'))
        Form.resize(405, 418)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 191, 31))
        self.label.setStyleSheet(u"font-size: 20px; font: bold; color: #08b4fa;")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 130, 351, 241))
        self.label_2.setStyleSheet(u"font-size: 15px; font: bold;")
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 80, 301, 41))
        self.lineEdit.setStyleSheet(u"font-size: 18px;")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 60, 261, 16))
        self.label_3.setStyleSheet(u"font-size: 15px;")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(320, 80, 75, 41))
        self.pushButton.setStyleSheet(u"font-size: 15px; font:bold;")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"GoWeather", None))
        self.label.setText(QCoreApplication.translate("Form", u"GoWeather", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Введите название города (Поселка)", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Искать", None))