# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)
import Icons_rc

class Ui_w_LoginForm(object):
    def setupUi(self, w_LoginForm):
        if not w_LoginForm.objectName():
            w_LoginForm.setObjectName(u"w_LoginForm")
        w_LoginForm.resize(492, 215)
        font = QFont()
        font.setPointSize(12)
        w_LoginForm.setFont(font)
        icon = QIcon()
        icon.addFile(u":/Main/HWU.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        w_LoginForm.setWindowIcon(icon)
        self.gridLayout = QGridLayout(w_LoginForm)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pb_Cancel = QPushButton(w_LoginForm)
        self.pb_Cancel.setObjectName(u"pb_Cancel")
        icon1 = QIcon()
        icon1.addFile(u":/Buttons/cross.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_Cancel.setIcon(icon1)

        self.gridLayout.addWidget(self.pb_Cancel, 2, 2, 1, 1)

        self.pb_Ok = QPushButton(w_LoginForm)
        self.pb_Ok.setObjectName(u"pb_Ok")
        icon2 = QIcon()
        icon2.addFile(u":/Buttons/tick.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_Ok.setIcon(icon2)

        self.gridLayout.addWidget(self.pb_Ok, 2, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.groupBox = QGroupBox(w_LoginForm)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.le_UserId = QLineEdit(self.groupBox)
        self.le_UserId.setObjectName(u"le_UserId")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_UserId)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.le_Password = QLineEdit(self.groupBox)
        self.le_Password.setObjectName(u"le_Password")
        self.le_Password.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.le_Password)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 4)

        self.lb_Message = QLabel(w_LoginForm)
        self.lb_Message.setObjectName(u"lb_Message")

        self.gridLayout.addWidget(self.lb_Message, 4, 0, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 2, 1, 1)


        self.retranslateUi(w_LoginForm)

        QMetaObject.connectSlotsByName(w_LoginForm)
    # setupUi

    def retranslateUi(self, w_LoginForm):
        w_LoginForm.setWindowTitle(QCoreApplication.translate("w_LoginForm", u"Sample Application", None))
        self.pb_Cancel.setText(QCoreApplication.translate("w_LoginForm", u"Cancel", None))
        self.pb_Ok.setText(QCoreApplication.translate("w_LoginForm", u"Ok", None))
        self.groupBox.setTitle(QCoreApplication.translate("w_LoginForm", u"Welcome! Please Login", None))
        self.label.setText(QCoreApplication.translate("w_LoginForm", u"User ID", None))
        self.label_2.setText(QCoreApplication.translate("w_LoginForm", u"Password", None))
        self.lb_Message.setText(QCoreApplication.translate("w_LoginForm", u"Message", None))
    # retranslateUi

