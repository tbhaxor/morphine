from PyQt5 import QtCore, QtGui, QtWidgets
from morphine.globals import (
    __intended_audience__,
    __license__,
    __programming_lang__,
    __enviroments__,
    find_packages,
)
from morphine.template import __minimal__ as template
from yapf.yapflib.yapf_api import FormatCode
import os


class Ui_minimal(object):
    def __init__(self, data):
        self.data = data
        pass

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 475)
        MainWindow.setMinimumSize(QtCore.QSize(900, 475))
        MainWindow.setMaximumSize(QtCore.QSize(900, 475))
        self.obj = MainWindow
        resolution = QtWidgets.QDesktopWidget().screenGeometry()
        MainWindow.move(
            (resolution.width() / 2) - (MainWindow.frameSize().width() / 2),
            (resolution.height() / 2) - (MainWindow.frameSize().height() / 2),
        )
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 111, 30))
        self.label.setObjectName("label")
        self.shortDesc = QtWidgets.QLineEdit(self.centralwidget)
        self.shortDesc.setGeometry(QtCore.QRect(120, 10, 771, 30))
        self.shortDesc.setObjectName("shortDesc")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 111, 30))
        self.label_2.setObjectName("label_2")
        self.longDesc = QtWidgets.QLineEdit(self.centralwidget)
        self.longDesc.setGeometry(QtCore.QRect(120, 50, 731, 31))
        self.longDesc.setObjectName("longDesc")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 111, 30))
        self.label_3.setObjectName("label_3")
        self.keywords = QtWidgets.QLineEdit(self.centralwidget)
        self.keywords.setGeometry(QtCore.QRect(120, 130, 311, 30))
        self.keywords.setObjectName("keywords")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(450, 130, 91, 30))
        self.label_4.setObjectName("label_4")
        self.pyreq = QtWidgets.QLineEdit(self.centralwidget)
        self.pyreq.setGeometry(QtCore.QRect(550, 130, 341, 30))
        self.pyreq.setObjectName("pyreq")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 170, 81, 30))
        self.label_5.setObjectName("label_5")
        self.envList = QtWidgets.QComboBox(self.centralwidget)
        self.envList.setGeometry(QtCore.QRect(120, 170, 231, 30))
        self.envList.setObjectName("envList")
        self.envAdd = QtWidgets.QPushButton(self.centralwidget)
        self.envAdd.setGeometry(QtCore.QRect(360, 170, 30, 30))
        self.envAdd.setObjectName("envAdd")
        self.envRem = QtWidgets.QPushButton(self.centralwidget)
        self.envRem.setGeometry(QtCore.QRect(400, 170, 30, 30))
        self.envRem.setObjectName("envRem")
        self.audAdd = QtWidgets.QPushButton(self.centralwidget)
        self.audAdd.setGeometry(QtCore.QRect(820, 170, 30, 30))
        self.audAdd.setObjectName("audAdd")
        self.aduRem = QtWidgets.QPushButton(self.centralwidget)
        self.aduRem.setGeometry(QtCore.QRect(860, 170, 30, 30))
        self.aduRem.setObjectName("aduRem")
        self.audList = QtWidgets.QComboBox(self.centralwidget)
        self.audList.setGeometry(QtCore.QRect(550, 170, 261, 30))
        self.audList.setObjectName("audList")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(450, 170, 81, 30))
        self.label_6.setObjectName("label_6")
        self.licAdd = QtWidgets.QPushButton(self.centralwidget)
        self.licAdd.setGeometry(QtCore.QRect(360, 210, 30, 30))
        self.licAdd.setObjectName("licAdd")
        self.langAdd = QtWidgets.QPushButton(self.centralwidget)
        self.langAdd.setGeometry(QtCore.QRect(820, 210, 30, 30))
        self.langAdd.setObjectName("langAdd")
        self.langRem = QtWidgets.QPushButton(self.centralwidget)
        self.langRem.setGeometry(QtCore.QRect(860, 210, 30, 30))
        self.langRem.setObjectName("langRem")
        self.langList = QtWidgets.QComboBox(self.centralwidget)
        self.langList.setGeometry(QtCore.QRect(550, 210, 261, 30))
        self.langList.setObjectName("langList")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(450, 210, 81, 30))
        self.label_7.setObjectName("label_7")
        self.licRem = QtWidgets.QPushButton(self.centralwidget)
        self.licRem.setGeometry(QtCore.QRect(400, 210, 30, 30))
        self.licRem.setObjectName("licRem")
        self.licList = QtWidgets.QComboBox(self.centralwidget)
        self.licList.setGeometry(QtCore.QRect(120, 210, 231, 30))
        self.licList.setObjectName("licList")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 210, 81, 30))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 250, 81, 30))
        self.label_9.setObjectName("label_9")
        self.classifiers = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.classifiers.setGeometry(QtCore.QRect(120, 250, 771, 181))
        self.classifiers.setReadOnly(True)
        self.classifiers.setObjectName("classifiers")
        self.build = QtWidgets.QPushButton(self.centralwidget)
        self.build.setGeometry(QtCore.QRect(810, 440, 80, 30))
        self.build.setObjectName("build")
        self.browse_long_desc = QtWidgets.QPushButton(self.centralwidget)
        self.browse_long_desc.setGeometry(QtCore.QRect(860, 50, 31, 30))
        self.browse_long_desc.setObjectName("browse_long_desc")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 90, 111, 30))
        self.label_10.setObjectName("label_10")
        self.packages = QtWidgets.QLineEdit(self.centralwidget)
        self.packages.setGeometry(QtCore.QRect(120, 90, 701, 31))
        self.packages.setObjectName("packages")
        self.find_packages = QtWidgets.QPushButton(self.centralwidget)
        self.find_packages.setGeometry(QtCore.QRect(830, 90, 61, 30))
        self.find_packages.setObjectName("find_packages")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(10, 450, 150, 17))
        self.label_11.setAutoFillBackground(False)
        self.label_11.setStyleSheet("color: red;\n"
                                    "text-decoration: underline;\n"
                                    "font-style: italic;")
        self.label_11.setObjectName("label_11")
        self.packages.raise_()
        self.label.raise_()
        self.shortDesc.raise_()
        self.label_2.raise_()
        self.longDesc.raise_()
        self.label_3.raise_()
        self.keywords.raise_()
        self.label_4.raise_()
        self.pyreq.raise_()
        self.label_5.raise_()
        self.envList.raise_()
        self.envAdd.raise_()
        self.envRem.raise_()
        self.audAdd.raise_()
        self.aduRem.raise_()
        self.audList.raise_()
        self.label_6.raise_()
        self.licAdd.raise_()
        self.langAdd.raise_()
        self.langRem.raise_()
        self.langList.raise_()
        self.label_7.raise_()
        self.licRem.raise_()
        self.licList.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.classifiers.raise_()
        self.build.raise_()
        self.browse_long_desc.raise_()
        self.label_10.raise_()
        self.find_packages.raise_()
        self.label_11.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.shortDesc, self.longDesc)
        MainWindow.setTabOrder(self.longDesc, self.browse_long_desc)
        MainWindow.setTabOrder(self.browse_long_desc, self.packages)
        MainWindow.setTabOrder(self.packages, self.find_packages)
        MainWindow.setTabOrder(self.find_packages, self.keywords)
        MainWindow.setTabOrder(self.keywords, self.pyreq)
        MainWindow.setTabOrder(self.pyreq, self.envList)
        MainWindow.setTabOrder(self.envList, self.envAdd)
        MainWindow.setTabOrder(self.envAdd, self.envRem)
        MainWindow.setTabOrder(self.envRem, self.audList)
        MainWindow.setTabOrder(self.audList, self.audAdd)
        MainWindow.setTabOrder(self.audAdd, self.aduRem)
        MainWindow.setTabOrder(self.aduRem, self.licList)
        MainWindow.setTabOrder(self.licList, self.licAdd)
        MainWindow.setTabOrder(self.licAdd, self.licRem)
        MainWindow.setTabOrder(self.licRem, self.langList)
        MainWindow.setTabOrder(self.langList, self.langAdd)
        MainWindow.setTabOrder(self.langAdd, self.langRem)
        MainWindow.setTabOrder(self.langRem, self.classifiers)
        MainWindow.setTabOrder(self.classifiers, self.build)
        self.audList.addItems(__intended_audience__)
        self.envList.addItems(__enviroments__)
        self.langList.addItems(__programming_lang__)
        self.licList.addItems(__license__)
        self.classifiers.appendPlainText(self.data.dev_status)
        # hooking buttons
        self.audAdd.clicked.connect(self.addAud)
        self.aduRem.clicked.connect(self.remAud)
        self.envAdd.clicked.connect(self.addEnv)
        self.envRem.clicked.connect(self.remEnv)
        self.langAdd.clicked.connect(self.addLang)
        self.langRem.clicked.connect(self.remLang)
        self.licAdd.clicked.connect(self.addLic)
        self.licRem.clicked.connect(self.remLic)
        self.find_packages.clicked.connect(self.pac)
        self.build.clicked.connect(self.builder)
        self.browse_long_desc.clicked.connect(self.getdesc)
        pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(
            _translate("MainWindow", "Morphine :: Minimal :: Builder"))
        self.label.setText(_translate("MainWindow", "Short Description"))
        self.label_2.setText(_translate("MainWindow", "Long Description"))
        self.label_3.setText(_translate("MainWindow", "Keywords"))
        self.label_4.setText(_translate("MainWindow", "Python Version"))
        self.label_5.setText(_translate("MainWindow", "Enviroment"))
        self.envAdd.setText(_translate("MainWindow", "+"))
        self.envRem.setText(_translate("MainWindow", "-"))
        self.audAdd.setText(_translate("MainWindow", "+"))
        self.aduRem.setText(_translate("MainWindow", "-"))
        self.label_6.setText(_translate("MainWindow", "Audience"))
        self.licAdd.setText(_translate("MainWindow", "+"))
        self.langAdd.setText(_translate("MainWindow", "+"))
        self.langRem.setText(_translate("MainWindow", "-"))
        self.label_7.setText(_translate("MainWindow", "Prog. Lang."))
        self.licRem.setText(_translate("MainWindow", "-"))
        self.label_8.setText(_translate("MainWindow", "License"))
        self.label_9.setText(_translate("MainWindow", "Classisiers"))
        self.build.setText(_translate("MainWindow", "&Build"))
        self.browse_long_desc.setText(_translate("MainWindow", "..."))
        self.label_10.setText(_translate("MainWindow", "Packages"))
        self.find_packages.setText(_translate("MainWindow", "&Find"))
        self.label_11.setText(
            _translate("MainWindow", " All Fields are mandatory"))
        self.shortDesc.setPlaceholderText(
            _translate("MainWindow",
                       "Enter short description of your project"))
        self.longDesc.setPlaceholderText(
            _translate(
                "MainWindow",
                "Enter short description file path or browse (only markdown files)"
            ))
        self.packages.setPlaceholderText(
            _translate("MainWindow",
                       "Enter packages to include or click Find button"))
        self.pyreq.setPlaceholderText(
            _translate("MainWindow", "Enter minimum python version required"))
        self.pyreq.setToolTip("Visit https://goo.gl/CKEpbN for help")
        self.browse_long_desc.setToolTip("Browse markdown files")
        self.find_packages.setToolTip("Find and list packages")
        self.keywords.setPlaceholderText(
            _translate("MainWindow", "Keywords for SEO"))
        self.shortDesc.setFocus()
        pass

    def pac(self):
        self.packages.setText(", ".join(find_packages()))
        pass

    def addAud(self):
        current = "Intended Audience :: " + self.audList.currentText()
        classifier = self.classifiers.toPlainText().split("\n")
        if current in classifier:
            return None
        classifier.append(current)
        self.classifiers.setPlainText("\n".join(classifier))
        pass

    def remAud(self):
        current = "Intended Audience :: " + self.audList.currentText()
        classifier = self.classifiers.toPlainText().split("\n")
        try:
            classifier.remove(current)
        except ValueError:
            pass
        self.classifiers.setPlainText("\n".join(classifier))
        pass

    def addLang(self):
        current = "Programming Language :: " + self.langList.currentText()
        classifier = self.classifiers.toPlainText().split("\n")
        if current in classifier:
            return None
        classifier.append(current)
        self.classifiers.setPlainText("\n".join(classifier))
        pass

    def remLang(self):
        current = "Programming Language :: " + self.langList.currentText()
        classifier = self.classifiers.toPlainText().split("\n")
        try:
            classifier.remove(current)
        except ValueError:
            pass
        self.classifiers.setPlainText("\n".join(classifier))
        pass

    def addEnv(self):
        current = "Environment :: " + self.envList.currentText()
        classifier = self.classifiers.toPlainText().split("\n")
        if current in classifier:
            return None
        classifier.append(current)
        self.classifiers.setPlainText("\n".join(classifier))
        pass

    def remEnv(self):
        current = "Environment :: " + self.envList.currentText()
        classifier = self.classifiers.toPlainText().split("\n")
        try:
            classifier.remove(current)
        except ValueError:
            pass
        self.classifiers.setPlainText("\n".join(classifier))
        pass

    def addLic(self):
        current = "License :: " + self.licList.currentText()
        classifier = self.classifiers.toPlainText().split("\n")
        if current in classifier:
            return None
        classifier.append(current)
        self.classifiers.setPlainText("\n".join(classifier))
        pass

    def remLic(self):
        current = "License :: " + self.licList.currentText()
        classifier = self.classifiers.toPlainText().split("\n")
        try:
            classifier.remove(current)
        except ValueError:
            pass
        self.classifiers.setPlainText("\n".join(classifier))
        pass

    def browse(self):
        file = str(
            QtWidgets.QFileDialog.getOpenFileName(
                self.obj, "Select File", self.data.dir,
                "Markdown files (*.MD *.md)")[0])
        self.longDesc.setText(file)
        pass

    def builder(self):
        # brainfuck validation

        # short desc
        shortDesc = self.shortDesc.text()
        if shortDesc == "":
            QtWidgets.QMessageBox.warning(self.obj, "Empty Field",
                                          "Short description is empty")
            self.shortDesc.setFocus()
            return None

        # long desc
        longDesc = self.longDesc.text()
        if longDesc == "":
            QtWidgets.QMessageBox.warning(self.obj, "Empty Fields",
                                          "Long description is empty")
            self.longDesc.setFocus()
            return None
        elif not os.path.exists(longDesc):
            QtWidgets.QMessageBox.warning(self.obj, "Not Exitsts",
                                          "Long description file not exists")
            self.longDesc.setFocus()
            return None

        # packages
        packages = self.packages.text()
        if packages == "":
            QtWidgets.QMessageBox.warning(self.obj, "Empty Fields",
                                          "Packages are empty")
            self.packages.setFocus()
            return None
        else:
            packages = [x.strip() for x in packages.split(",")]

        # keywords
        keywords = self.keywords.text()
        if keywords == "":
            QtWidgets.QMessageBox.warning(self.obj, "Empty Fields",
                                          "Keywords are empty")
            self.keywords.setFocus()
            return None

        # python version
        pyreq = self.pyreq.text()
        if pyreq == "":
            QtWidgets.QMessageBox.warning(self.obj, "Empty Fields",
                                          "Python version required is empty")
            self.pyreq.setFocus()
            return None

        classifiers = self.classifiers.toPlainText().split("\n")

        setup = FormatCode(
            template.format(
                name=self.data.name,
                packages=packages,
                version=self.data.version,
                auth_name=self.data.authorname,
                auth_email=self.data.authoremail,
                home_url=self.data.home_url,
                down_url=self.data.down_url,
                short_desc=shortDesc,
                long_desc=longDesc,
                license=self.data.license,
                keywords=keywords,
                classifiers=classifiers,
                python_required=pyreq),
            style_config="pep8")[0]
        with open(os.path.join(self.data.dir, "setup.py"), "w") as file:
            file.write(setup)
            file.close()

        QtWidgets.QMessageBox.information(
            self.obj, "Done", "Hurry ^_^\nSetup file has been created")
        pass

    def getdesc(self):
        d = "."
        try:
            d = self.data.dir
        except AttributeError:
            pass
        file = str(
            QtWidgets.QFileDialog.getOpenFileName(
                self.obj, "Select Readme", d, "Markdown Files (*.MD *.md")[0])
        self.longDesc.setText(file)
