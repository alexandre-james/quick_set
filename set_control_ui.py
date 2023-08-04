# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:/pydev/Sets_control/sets_control.ui'
#
# Created: Sat Jan 11 13:53:37 2020
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_Sets(object):
    def setupUi(self, Sets):
        Sets.setObjectName("Sets")
        Sets.resize(251, 434)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Sets.sizePolicy().hasHeightForWidth())
        Sets.setSizePolicy(sizePolicy)
        # ---------------------------------------Makes custom toolbar stretch forever
        # Sets.setMinimumSize(QtCore.QSize(0, 0))
        Sets.setMaximumSize(QtCore.QSize(600, 1000))
        Sets.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        Sets.setAutoFillBackground(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(Sets)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.b_select = QtWidgets.QPushButton(Sets)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.b_select.sizePolicy().hasHeightForWidth())
        self.b_select.setSizePolicy(sizePolicy)
        self.b_select.setStyleSheet("")
        self.b_select.setText("Select")
        self.b_select.setObjectName("b_select")
        self.horizontalLayout.addWidget(self.b_select)

        self.b_auto = QtWidgets.QCheckBox(Sets)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.b_auto.sizePolicy().hasHeightForWidth())
        self.b_auto.setSizePolicy(sizePolicy)
        self.b_auto.setStyleSheet("border:none")
        self.b_auto.setText("Auto")
        self.b_auto.setObjectName("b_auto")
        self.horizontalLayout.addWidget(self.b_auto)

        self.b_add = QtWidgets.QPushButton(Sets)
        self.b_add.setEnabled(True)
        self.b_add.setStyleSheet("border:none")
        self.b_add.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/add.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.b_add.setIcon(icon)
        self.b_add.setObjectName("b_add")
        self.horizontalLayout.addWidget(self.b_add)

        self.b_remove = QtWidgets.QPushButton(Sets)
        self.b_remove.setStyleSheet("border:none")
        self.b_remove.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/remove.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.b_remove.setIcon(icon1)
        self.b_remove.setAutoExclusive(True)
        self.b_remove.setObjectName("b_remove")
        self.horizontalLayout.addWidget(self.b_remove)

        self.b_clear = QtWidgets.QPushButton(Sets)
        self.b_clear.setStyleSheet("border:none")
        self.b_clear.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(
            "../../Sets_control/icons/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap("icons/clear.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.b_clear.setIcon(icon2)
        self.b_clear.setObjectName("b_clear")
        self.horizontalLayout.addWidget(self.b_clear)
        self.b_color = QtWidgets.QPushButton(Sets)
        self.b_color.setStyleSheet("border:none")
        self.b_color.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/Color.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.b_color.setIcon(icon3)
        self.b_color.setAutoExclusive(True)
        self.b_color.setObjectName("b_color")
        self.horizontalLayout.addWidget(self.b_color)
        self.b_delete = QtWidgets.QPushButton(Sets)
        self.b_delete.setStyleSheet("border:none")
        self.b_delete.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/delete.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.b_delete.setIcon(icon4)
        self.b_delete.setAutoExclusive(True)
        self.b_delete.setObjectName("b_delete")
        self.horizontalLayout.addWidget(self.b_delete)
        self.b_menu = QtWidgets.QPushButton(Sets)
        self.b_menu.setStyleSheet("border:none")
        self.b_menu.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/Menu.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.b_menu.setIcon(icon5)
        self.b_menu.setAutoExclusive(True)
        self.b_menu.setObjectName("b_menu")
        self.horizontalLayout.addWidget(self.b_menu)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(
            20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem)
        self.tableWidget = QtWidgets.QTableWidget(Sets)
        self.tableWidget.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(60)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableWidget)
        self.b_new = QtWidgets.QPushButton(Sets)
        self.b_new.setMinimumSize(QtCore.QSize(0, 35))
        self.b_new.setMaximumSize(QtCore.QSize(16777215, 35))
        self.b_new.setObjectName("b_new")
        self.verticalLayout.addWidget(self.b_new)

        self.retranslateUi(Sets)
        QtCore.QMetaObject.connectSlotsByName(Sets)

    def retranslateUi(self, Sets):
        Sets.setWindowTitle(
            QtWidgets.QApplication.translate("Sets", "Sets", None, -1))
        self.b_add.setToolTip(
            QtWidgets.QApplication.translate("Sets", "Add", None, -1))
        self.b_remove.setToolTip(
            QtWidgets.QApplication.translate("Sets", "Remove", None, -1))
        self.b_clear.setToolTip(
            QtWidgets.QApplication.translate("Sets", "Clear", None, -1))
        self.b_color.setToolTip(
            QtWidgets.QApplication.translate("Sets", "Delete", None, -1))
        self.b_delete.setToolTip(
            QtWidgets.QApplication.translate("Sets", "Delete", None, -1))
        self.b_menu.setToolTip(
            QtWidgets.QApplication.translate("Sets", "Delete", None, -1))
        self.b_new.setText(QtWidgets.QApplication.translate(
            "Sets", "New Set", None, -1))
