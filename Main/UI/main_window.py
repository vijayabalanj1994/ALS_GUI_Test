# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)
import Icons_rc

class Ui_m_window(object):
    def setupUi(self, m_window):
        if not m_window.objectName():
            m_window.setObjectName(u"m_window")
        m_window.resize(485, 458)
        font = QFont()
        font.setPointSize(12)
        m_window.setFont(font)
        icon = QIcon()
        icon.addFile(u":/Main/HWU.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        m_window.setWindowIcon(icon)
        self.action_Quit = QAction(m_window)
        self.action_Quit.setObjectName(u"action_Quit")
        icon1 = QIcon()
        icon1.addFile(u":/Buttons/cross.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_Quit.setIcon(icon1)
        font1 = QFont()
        font1.setPointSize(8)
        self.action_Quit.setFont(font1)
        self.action_AddPerson = QAction(m_window)
        self.action_AddPerson.setObjectName(u"action_AddPerson")
        self.action_AddPerson.setFont(font1)
        self.centralwidget = QWidget(m_window)
        self.centralwidget.setObjectName(u"centralwidget")
        m_window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(m_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 485, 27))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuPerson = QMenu(self.menubar)
        self.menuPerson.setObjectName(u"menuPerson")
        m_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(m_window)
        self.statusbar.setObjectName(u"statusbar")
        m_window.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuPerson.menuAction())
        self.menuFile.addAction(self.action_Quit)
        self.menuPerson.addAction(self.action_AddPerson)

        self.retranslateUi(m_window)

        QMetaObject.connectSlotsByName(m_window)
    # setupUi

    def retranslateUi(self, m_window):
        m_window.setWindowTitle(QCoreApplication.translate("m_window", u"Sample Application", None))
        self.action_Quit.setText(QCoreApplication.translate("m_window", u"Quit", None))
        self.action_AddPerson.setText(QCoreApplication.translate("m_window", u"Add Person", None))
        self.menuFile.setTitle(QCoreApplication.translate("m_window", u"File", None))
        self.menuPerson.setTitle(QCoreApplication.translate("m_window", u"Person", None))
    # retranslateUi

