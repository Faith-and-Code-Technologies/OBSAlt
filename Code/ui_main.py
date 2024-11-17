# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainpXGyeq.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QDockWidget, QGridLayout, QGroupBox,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(710, 570)
        self.actionChoose_Output_Path = QAction(MainWindow)
        self.actionChoose_Output_Path.setObjectName(u"actionChoose_Output_Path")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.previewBox = QGroupBox(self.centralwidget)
        self.previewBox.setObjectName(u"previewBox")
        self.gridLayout_3 = QGridLayout(self.previewBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.preview = QLabel(self.previewBox)
        self.preview.setObjectName(u"preview")

        self.gridLayout_3.addWidget(self.preview, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.previewBox, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.Recording = QDockWidget(MainWindow)
        self.Recording.setObjectName(u"Recording")
        self.dockWidgetContents_3 = QWidget()
        self.dockWidgetContents_3.setObjectName(u"dockWidgetContents_3")
        self.gridLayout = QGridLayout(self.dockWidgetContents_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.startrec = QPushButton(self.dockWidgetContents_3)
        self.startrec.setObjectName(u"startrec")

        self.gridLayout.addWidget(self.startrec, 0, 0, 1, 1)

        self.stoprec = QPushButton(self.dockWidgetContents_3)
        self.stoprec.setObjectName(u"stoprec")

        self.gridLayout.addWidget(self.stoprec, 1, 0, 1, 1)

        self.Recording.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, self.Recording)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionChoose_Output_Path.setText(QCoreApplication.translate("MainWindow", u"Choose Output Path", None))
        self.previewBox.setTitle(QCoreApplication.translate("MainWindow", u"Preveiw", None))
        self.preview.setText("")
        self.startrec.setText(QCoreApplication.translate("MainWindow", u"Start Recording", None))
        self.stoprec.setText(QCoreApplication.translate("MainWindow", u"Stop Recording", None))
    # retranslateUi

