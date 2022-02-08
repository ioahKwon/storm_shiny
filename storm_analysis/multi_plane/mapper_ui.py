# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mapper.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(922, 734)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.channelGraphicsView = MapperView(self.centralwidget)
        self.channelGraphicsView.setObjectName("channelGraphicsView")
        self.horizontalLayout_2.addWidget(self.channelGraphicsView)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.maxSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.maxSpinBox.setMaximum(100000)
        self.maxSpinBox.setProperty("value", 1000)
        self.maxSpinBox.setObjectName("maxSpinBox")
        self.verticalLayout.addWidget(self.maxSpinBox)
        self.rangeSliderWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rangeSliderWidget.sizePolicy().hasHeightForWidth())
        self.rangeSliderWidget.setSizePolicy(sizePolicy)
        self.rangeSliderWidget.setObjectName("rangeSliderWidget")
        self.verticalLayout.addWidget(self.rangeSliderWidget)
        self.minSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.minSpinBox.setMaximum(100000)
        self.minSpinBox.setProperty("value", 100)
        self.minSpinBox.setObjectName("minSpinBox")
        self.verticalLayout.addWidget(self.minSpinBox)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.contrastLabel = QtWidgets.QLabel(self.centralwidget)
        self.contrastLabel.setObjectName("contrastLabel")
        self.horizontalLayout.addWidget(self.contrastLabel)
        self.channelComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.channelComboBox.setObjectName("channelComboBox")
        self.horizontalLayout.addWidget(self.channelComboBox)
        self.frameLabel = QtWidgets.QLabel(self.centralwidget)
        self.frameLabel.setObjectName("frameLabel")
        self.horizontalLayout.addWidget(self.frameLabel)
        self.flipLRPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.flipLRPushButton.setObjectName("flipLRPushButton")
        self.horizontalLayout.addWidget(self.flipLRPushButton)
        self.flipUDPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.flipUDPushButton.setObjectName("flipUDPushButton")
        self.horizontalLayout.addWidget(self.flipUDPushButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.groupsLabel = QtWidgets.QLabel(self.centralwidget)
        self.groupsLabel.setObjectName("groupsLabel")
        self.horizontalLayout.addWidget(self.groupsLabel)
        self.maxDistLabel = QtWidgets.QLabel(self.centralwidget)
        self.maxDistLabel.setObjectName("maxDistLabel")
        self.horizontalLayout.addWidget(self.maxDistLabel)
        self.maxDistDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.maxDistDoubleSpinBox.setProperty("value", 8.0)
        self.maxDistDoubleSpinBox.setObjectName("maxDistDoubleSpinBox")
        self.horizontalLayout.addWidget(self.maxDistDoubleSpinBox)
        self.mapItPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.mapItPushButton.setObjectName("mapItPushButton")
        self.horizontalLayout.addWidget(self.mapItPushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 922, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad_Channel = QtWidgets.QAction(MainWindow)
        self.actionLoad_Channel.setObjectName("actionLoad_Channel")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionSave_Mapping = QtWidgets.QAction(MainWindow)
        self.actionSave_Mapping.setObjectName("actionSave_Mapping")
        self.actionReset = QtWidgets.QAction(MainWindow)
        self.actionReset.setObjectName("actionReset")
        self.actionClear_Groups = QtWidgets.QAction(MainWindow)
        self.actionClear_Groups.setObjectName("actionClear_Groups")
        self.menuFile.addAction(self.actionLoad_Channel)
        self.menuFile.addAction(self.actionSave_Mapping)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClear_Groups)
        self.menuFile.addAction(self.actionReset)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Multi-Channel Mapping Utility"))
        self.label.setText(_translate("MainWindow", "Contrast"))
        self.contrastLabel.setText(_translate("MainWindow", "Channel"))
        self.frameLabel.setText(_translate("MainWindow", "Frame:"))
        self.flipLRPushButton.setText(_translate("MainWindow", "Flip L/R"))
        self.flipUDPushButton.setText(_translate("MainWindow", "Flip U/D"))
        self.groupsLabel.setText(_translate("MainWindow", "0 groups"))
        self.maxDistLabel.setText(_translate("MainWindow", "Max Distance (pixels)"))
        self.mapItPushButton.setText(_translate("MainWindow", "Map It"))
        self.menuFile.setTitle(_translate("MainWindow", "Fi&le"))
        self.actionLoad_Channel.setText(_translate("MainWindow", "&Load Channel"))
        self.actionQuit.setText(_translate("MainWindow", "&Quit"))
        self.actionSave_Mapping.setText(_translate("MainWindow", "&Save Mapping"))
        self.actionReset.setText(_translate("MainWindow", "&Reset"))
        self.actionClear_Groups.setText(_translate("MainWindow", "Clear Groups"))

from storm_analysis.multi_plane.mapperView import MapperView
