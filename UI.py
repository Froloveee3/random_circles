from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 1000)
        self.DrawCircles = QtWidgets.QPushButton(Form)
        self.DrawCircles.setGeometry(QtCore.QRect(400, 475, 200, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.DrawCircles.setFont(font)
        self.DrawCircles.setObjectName("DrawCircles")
        self.Ground = QtWidgets.QLabel(Form)
        self.Ground.setGeometry(QtCore.QRect(0, 0, 1000, 1000))
        self.Ground.setText("")
        self.Ground.setObjectName("Ground")
        self.Ground.raise_()
        self.Ground.setPixmap(QPixmap(1000, 1000))
        self.DrawCircles.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.DrawCircles.setText(_translate("Form", "Нарисовать окружности"))
