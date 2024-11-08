# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Adam\Projects\UNSW\comp6441\PassCipher\passcipher\ui\sidebar.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(843, 583)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.full_menu_widget = QtWidgets.QWidget(self.centralwidget)
        self.full_menu_widget.setObjectName("full_menu_widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.full_menu_widget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.logo_label_2 = QtWidgets.QLabel(self.full_menu_widget)
        self.logo_label_2.setMinimumSize(QtCore.QSize(40, 40))
        self.logo_label_2.setMaximumSize(QtCore.QSize(40, 40))
        self.logo_label_2.setText("")
        self.logo_label_2.setPixmap(QtGui.QPixmap(":/icon/icon/app_logo.png"))
        self.logo_label_2.setScaledContents(True)
        self.logo_label_2.setObjectName("logo_label_2")
        self.horizontalLayout_2.addWidget(self.logo_label_2)
        self.logo_label_3 = QtWidgets.QLabel(self.full_menu_widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.logo_label_3.setFont(font)
        self.logo_label_3.setObjectName("logo_label_3")
        self.horizontalLayout_2.addWidget(self.logo_label_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.sidebar_btns_2 = QtWidgets.QVBoxLayout()
        self.sidebar_btns_2.setSpacing(8)
        self.sidebar_btns_2.setObjectName("sidebar_btns_2")
        self.vault_text_label = QtWidgets.QLabel(self.full_menu_widget)
        self.vault_text_label.setObjectName("vault_text_label")
        self.sidebar_btns_2.addWidget(self.vault_text_label)
        self.cipher_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/vault(off).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/vault(on).png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.cipher_btn_2.setIcon(icon)
        self.cipher_btn_2.setIconSize(QtCore.QSize(14, 14))
        self.cipher_btn_2.setCheckable(True)
        self.cipher_btn_2.setAutoExclusive(True)
        self.cipher_btn_2.setObjectName("cipher_btn_2")
        self.sidebar_btns_2.addWidget(self.cipher_btn_2)
        self.accounts_text_label = QtWidgets.QLabel(self.full_menu_widget)
        self.accounts_text_label.setObjectName("accounts_text_label")
        self.sidebar_btns_2.addWidget(self.accounts_text_label)
        self.accounts_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icon/all_items(off).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/icon/icon/all_items(on).png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.accounts_btn_2.setIcon(icon1)
        self.accounts_btn_2.setIconSize(QtCore.QSize(14, 14))
        self.accounts_btn_2.setCheckable(True)
        self.accounts_btn_2.setAutoExclusive(True)
        self.accounts_btn_2.setObjectName("accounts_btn_2")
        self.sidebar_btns_2.addWidget(self.accounts_btn_2)
        self.categories_text_label = QtWidgets.QLabel(self.full_menu_widget)
        self.categories_text_label.setObjectName("categories_text_label")
        self.sidebar_btns_2.addWidget(self.categories_text_label)
        self.verticalLayout_4.addLayout(self.sidebar_btns_2)
        spacerItem = QtWidgets.QSpacerItem(20, 391, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.logout_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        self.logout_btn_2.setObjectName("logout_btn_2")
        self.verticalLayout_4.addWidget(self.logout_btn_2)
        self.gridLayout.addWidget(self.full_menu_widget, 0, 1, 1, 1)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.search_bar = QtWidgets.QWidget(self.widget_3)
        self.search_bar.setMinimumSize(QtCore.QSize(0, 40))
        self.search_bar.setObjectName("search_bar")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.search_bar)
        self.horizontalLayout_4.setContentsMargins(0, 0, 10, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.sidebar_btn = QtWidgets.QPushButton(self.search_bar)
        self.sidebar_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/icon/sidebar_list.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sidebar_btn.setIcon(icon2)
        self.sidebar_btn.setIconSize(QtCore.QSize(17, 17))
        self.sidebar_btn.setCheckable(True)
        self.sidebar_btn.setObjectName("sidebar_btn")
        self.horizontalLayout_4.addWidget(self.sidebar_btn)
        spacerItem1 = QtWidgets.QSpacerItem(193, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.search_input = QtWidgets.QLineEdit(self.search_bar)
        self.search_input.setObjectName("search_input")
        self.horizontalLayout.addWidget(self.search_input)
        self.search_btn = QtWidgets.QPushButton(self.search_bar)
        self.search_btn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/icon/search.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_btn.setIcon(icon3)
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout.addWidget(self.search_btn)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(193, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.add_btn = QtWidgets.QPushButton(self.search_bar)
        self.add_btn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/icon/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_btn.setIcon(icon4)
        self.add_btn.setIconSize(QtCore.QSize(20, 20))
        self.add_btn.setObjectName("add_btn")
        self.horizontalLayout_4.addWidget(self.add_btn)
        self.verticalLayout_5.addWidget(self.search_bar)
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget_3)
        self.stackedWidget.setObjectName("stackedWidget")
        self.database_page = QtWidgets.QWidget()
        self.database_page.setObjectName("database_page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.database_page)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.login_username = QtWidgets.QLineEdit(self.database_page)
        self.login_username.setObjectName("login_username")
        self.verticalLayout.addWidget(self.login_username)
        self.login_key = QtWidgets.QLineEdit(self.database_page)
        self.login_key.setObjectName("login_key")
        self.verticalLayout.addWidget(self.login_key)
        self.login_btn = QtWidgets.QPushButton(self.database_page)
        self.login_btn.setObjectName("login_btn")
        self.verticalLayout.addWidget(self.login_btn)
        self.login_register_btn = QtWidgets.QPushButton(self.database_page)
        self.login_register_btn.setObjectName("login_register_btn")
        self.verticalLayout.addWidget(self.login_register_btn)
        self.gridLayout_2.addLayout(self.verticalLayout, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(206, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 1, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(206, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 1, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 257, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem5, 0, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 202, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem6, 2, 1, 1, 1)
        self.stackedWidget.addWidget(self.database_page)
        self.account_page = QtWidgets.QWidget()
        self.account_page.setObjectName("account_page")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.account_page)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.account_table = QtWidgets.QTableWidget(self.account_page)
        self.account_table.setFocusPolicy(QtCore.Qt.NoFocus)
        self.account_table.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.account_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.account_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.account_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.account_table.setShowGrid(False)
        self.account_table.setGridStyle(QtCore.Qt.NoPen)
        self.account_table.setRowCount(0)
        self.account_table.setObjectName("account_table")
        self.account_table.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.account_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.account_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.account_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.account_table.setHorizontalHeaderItem(3, item)
        self.account_table.horizontalHeader().setDefaultSectionSize(120)
        self.account_table.horizontalHeader().setStretchLastSection(True)
        self.account_table.verticalHeader().setVisible(False)
        self.gridLayout_3.addWidget(self.account_table, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.account_page)
        self.view_page = QtWidgets.QWidget()
        self.view_page.setObjectName("view_page")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.view_page)
        self.gridLayout_5.setContentsMargins(30, 30, 30, -1)
        self.gridLayout_5.setVerticalSpacing(25)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.back_btn = QtWidgets.QPushButton(self.view_page)
        self.back_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.back_btn.setMaximumSize(QtCore.QSize(30, 30))
        self.back_btn.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/icon/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_btn.setIcon(icon5)
        self.back_btn.setObjectName("back_btn")
        self.horizontalLayout_6.addWidget(self.back_btn)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.account_title = QtWidgets.QLabel(self.view_page)
        self.account_title.setMinimumSize(QtCore.QSize(200, 0))
        self.account_title.setMaximumSize(QtCore.QSize(200, 16777215))
        self.account_title.setObjectName("account_title")
        self.horizontalLayout_6.addWidget(self.account_title)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem8)
        self.gridLayout_5.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
        self.key_input = QtWidgets.QLineEdit(self.view_page)
        self.key_input.setMinimumSize(QtCore.QSize(0, 50))
        self.key_input.setMaximumSize(QtCore.QSize(16777215, 50))
        self.key_input.setObjectName("key_input")
        self.gridLayout_5.addWidget(self.key_input, 2, 0, 1, 1)
        self.password_output = QtWidgets.QLineEdit(self.view_page)
        self.password_output.setMinimumSize(QtCore.QSize(0, 50))
        self.password_output.setMaximumSize(QtCore.QSize(16777215, 50))
        self.password_output.setReadOnly(True)
        self.password_output.setObjectName("password_output")
        self.gridLayout_5.addWidget(self.password_output, 4, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 57, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem9, 5, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.username_text = QtWidgets.QPlainTextEdit(self.view_page)
        self.username_text.setMinimumSize(QtCore.QSize(0, 30))
        self.username_text.setMaximumSize(QtCore.QSize(16777215, 30))
        self.username_text.setReadOnly(True)
        self.username_text.setObjectName("username_text")
        self.gridLayout_4.addWidget(self.username_text, 0, 2, 1, 1)
        self.username_title = QtWidgets.QLabel(self.view_page)
        self.username_title.setObjectName("username_title")
        self.gridLayout_4.addWidget(self.username_title, 0, 0, 1, 1)
        self.url_title = QtWidgets.QLabel(self.view_page)
        self.url_title.setObjectName("url_title")
        self.gridLayout_4.addWidget(self.url_title, 1, 0, 1, 1)
        self.notes_title = QtWidgets.QLabel(self.view_page)
        self.notes_title.setObjectName("notes_title")
        self.gridLayout_4.addWidget(self.notes_title, 2, 0, 1, 1)
        self.url_text = QtWidgets.QPlainTextEdit(self.view_page)
        self.url_text.setMinimumSize(QtCore.QSize(0, 30))
        self.url_text.setMaximumSize(QtCore.QSize(16777215, 30))
        self.url_text.setReadOnly(True)
        self.url_text.setObjectName("url_text")
        self.gridLayout_4.addWidget(self.url_text, 1, 2, 1, 1)
        self.notes_text = QtWidgets.QPlainTextEdit(self.view_page)
        self.notes_text.setMinimumSize(QtCore.QSize(0, 30))
        self.notes_text.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.notes_text.setBaseSize(QtCore.QSize(30, 30))
        self.notes_text.setReadOnly(True)
        self.notes_text.setObjectName("notes_text")
        self.gridLayout_4.addWidget(self.notes_text, 2, 2, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 1, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem10)
        self.generate_btn = QtWidgets.QPushButton(self.view_page)
        self.generate_btn.setMinimumSize(QtCore.QSize(200, 35))
        self.generate_btn.setMaximumSize(QtCore.QSize(200, 35))
        self.generate_btn.setObjectName("generate_btn")
        self.horizontalLayout_5.addWidget(self.generate_btn)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem11)
        self.gridLayout_5.addLayout(self.horizontalLayout_5, 3, 0, 1, 1)
        self.stackedWidget.addWidget(self.view_page)
        self.config_page = QtWidgets.QWidget()
        self.config_page.setObjectName("config_page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.config_page)
        self.verticalLayout_2.setContentsMargins(30, 30, 39, -1)
        self.verticalLayout_2.setSpacing(25)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.lowecase_label = QtWidgets.QLabel(self.config_page)
        self.lowecase_label.setObjectName("lowecase_label")
        self.gridLayout_6.addWidget(self.lowecase_label, 0, 0, 1, 1)
        self.lowercase_input = QtWidgets.QLineEdit(self.config_page)
        self.lowercase_input.setMinimumSize(QtCore.QSize(0, 30))
        self.lowercase_input.setObjectName("lowercase_input")
        self.gridLayout_6.addWidget(self.lowercase_input, 0, 1, 1, 1)
        self.uppercase_label = QtWidgets.QLabel(self.config_page)
        self.uppercase_label.setObjectName("uppercase_label")
        self.gridLayout_6.addWidget(self.uppercase_label, 1, 0, 1, 1)
        self.uppercase_input = QtWidgets.QLineEdit(self.config_page)
        self.uppercase_input.setMinimumSize(QtCore.QSize(0, 30))
        self.uppercase_input.setObjectName("uppercase_input")
        self.gridLayout_6.addWidget(self.uppercase_input, 1, 1, 1, 1)
        self.numbers_label = QtWidgets.QLabel(self.config_page)
        self.numbers_label.setObjectName("numbers_label")
        self.gridLayout_6.addWidget(self.numbers_label, 2, 0, 1, 1)
        self.numbers_input = QtWidgets.QLineEdit(self.config_page)
        self.numbers_input.setMinimumSize(QtCore.QSize(0, 30))
        self.numbers_input.setObjectName("numbers_input")
        self.gridLayout_6.addWidget(self.numbers_input, 2, 1, 1, 1)
        self.special_label = QtWidgets.QLabel(self.config_page)
        self.special_label.setObjectName("special_label")
        self.gridLayout_6.addWidget(self.special_label, 3, 0, 1, 1)
        self.special_input = QtWidgets.QLineEdit(self.config_page)
        self.special_input.setMinimumSize(QtCore.QSize(0, 30))
        self.special_input.setObjectName("special_input")
        self.gridLayout_6.addWidget(self.special_input, 3, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.config_save = QtWidgets.QPushButton(self.config_page)
        self.config_save.setObjectName("config_save")
        self.horizontalLayout_7.addWidget(self.config_save)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem12)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        spacerItem13 = QtWidgets.QSpacerItem(20, 286, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem13)
        self.stackedWidget.addWidget(self.config_page)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.gridLayout.addWidget(self.widget_3, 0, 2, 1, 1)
        self.icon_only_widget = QtWidgets.QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName("icon_only_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.logo_label_1 = QtWidgets.QLabel(self.icon_only_widget)
        self.logo_label_1.setMinimumSize(QtCore.QSize(50, 50))
        self.logo_label_1.setMaximumSize(QtCore.QSize(50, 50))
        self.logo_label_1.setText("")
        self.logo_label_1.setPixmap(QtGui.QPixmap(":/icon/icon/app_logo.png"))
        self.logo_label_1.setScaledContents(True)
        self.logo_label_1.setObjectName("logo_label_1")
        self.horizontalLayout_3.addWidget(self.logo_label_1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.sidebar_btns_1 = QtWidgets.QVBoxLayout()
        self.sidebar_btns_1.setSpacing(5)
        self.sidebar_btns_1.setObjectName("sidebar_btns_1")
        self.cipher_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.cipher_btn_1.setText("")
        self.cipher_btn_1.setIcon(icon)
        self.cipher_btn_1.setIconSize(QtCore.QSize(20, 20))
        self.cipher_btn_1.setCheckable(True)
        self.cipher_btn_1.setAutoExclusive(True)
        self.cipher_btn_1.setObjectName("cipher_btn_1")
        self.sidebar_btns_1.addWidget(self.cipher_btn_1)
        self.accounts_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.accounts_btn_1.setText("")
        self.accounts_btn_1.setIcon(icon1)
        self.accounts_btn_1.setIconSize(QtCore.QSize(20, 20))
        self.accounts_btn_1.setCheckable(True)
        self.accounts_btn_1.setAutoExclusive(True)
        self.accounts_btn_1.setObjectName("accounts_btn_1")
        self.sidebar_btns_1.addWidget(self.accounts_btn_1)
        self.verticalLayout_3.addLayout(self.sidebar_btns_1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 465, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem14)
        self.logout_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.logout_btn_1.setObjectName("logout_btn_1")
        self.verticalLayout_3.addWidget(self.logout_btn_1)
        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(3)
        self.accounts_btn_1.toggled['bool'].connect(self.accounts_btn_2.setChecked) # type: ignore
        self.accounts_btn_2.toggled['bool'].connect(self.accounts_btn_1.setChecked) # type: ignore
        self.sidebar_btn.toggled['bool'].connect(self.icon_only_widget.setVisible) # type: ignore
        self.sidebar_btn.toggled['bool'].connect(self.full_menu_widget.setHidden) # type: ignore
        self.cipher_btn_2.toggled['bool'].connect(self.cipher_btn_1.setChecked) # type: ignore
        self.cipher_btn_1.toggled['bool'].connect(self.cipher_btn_2.setChecked) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.logo_label_3.setText(_translate("MainWindow", "Sidebar"))
        self.vault_text_label.setText(_translate("MainWindow", "Config"))
        self.cipher_btn_2.setText(_translate("MainWindow", "Cipher"))
        self.accounts_text_label.setText(_translate("MainWindow", "Accounts"))
        self.accounts_btn_2.setText(_translate("MainWindow", "All Items"))
        self.categories_text_label.setText(_translate("MainWindow", "Categories"))
        self.logout_btn_2.setText(_translate("MainWindow", "Logout"))
        self.search_input.setPlaceholderText(_translate("MainWindow", "Seach"))
        self.login_username.setPlaceholderText(_translate("MainWindow", "Username"))
        self.login_key.setPlaceholderText(_translate("MainWindow", "Key"))
        self.login_btn.setText(_translate("MainWindow", "Login"))
        self.login_register_btn.setText(_translate("MainWindow", "Register"))
        item = self.account_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "#"))
        item = self.account_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.account_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Category"))
        item = self.account_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Operation"))
        self.account_title.setText(_translate("MainWindow", "Account View"))
        self.key_input.setPlaceholderText(_translate("MainWindow", "Password key"))
        self.password_output.setPlaceholderText(_translate("MainWindow", "Password display"))
        self.username_title.setText(_translate("MainWindow", "Username"))
        self.url_title.setText(_translate("MainWindow", "URL"))
        self.notes_title.setText(_translate("MainWindow", "Notes"))
        self.generate_btn.setText(_translate("MainWindow", "Generate Password"))
        self.lowecase_label.setText(_translate("MainWindow", "Lowercase"))
        self.lowercase_input.setPlaceholderText(_translate("MainWindow", "abcdefghijklmnopqrstuvwxyz"))
        self.uppercase_label.setText(_translate("MainWindow", "Uppercase"))
        self.uppercase_input.setPlaceholderText(_translate("MainWindow", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        self.numbers_label.setText(_translate("MainWindow", "Numbers"))
        self.numbers_input.setPlaceholderText(_translate("MainWindow", "0123456789"))
        self.special_label.setText(_translate("MainWindow", "Special Characters"))
        self.special_input.setPlaceholderText(_translate("MainWindow", "!@#$%^&*()"))
        self.config_save.setText(_translate("MainWindow", "Save"))
        self.logout_btn_1.setText(_translate("MainWindow", "Exit"))
from .static import resource_rc
