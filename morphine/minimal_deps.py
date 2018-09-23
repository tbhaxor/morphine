from PyQt5 import QtCore, QtGui, QtWidgets
from morphine.globals import __enviroments__, __intended_audience__, __programming_lang__, __license__, find_packages
import os
from yapf.yapflib.yapf_api import FormatCode
from morphine.template import __minimal_deps__ as template


class Ui_minimal_deps(object):
    def __init__(self, data):
        self.data = data
        pass

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(840, 490)
        MainWindow.setMinimumSize(QtCore.QSize(840, 490))
        MainWindow.setMaximumSize(QtCore.QSize(840, 490))
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
        self.shortDesc.setGeometry(QtCore.QRect(130, 10, 701, 30))
        self.shortDesc.setObjectName("shortDesc")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 111, 30))
        self.label_2.setObjectName("label_2")
        self.longDesc = QtWidgets.QLineEdit(self.centralwidget)
        self.longDesc.setGeometry(QtCore.QRect(130, 50, 661, 30))
        self.longDesc.setObjectName("longDesc")
        self.dependencies = QtWidgets.QLineEdit(self.centralwidget)
        self.dependencies.setGeometry(QtCore.QRect(130, 90, 301, 30))
        self.dependencies.setObjectName("dependencies")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 111, 30))
        self.label_3.setObjectName("label_3")
        self.packages = QtWidgets.QLineEdit(self.centralwidget)
        self.packages.setGeometry(QtCore.QRect(530, 90, 241, 30))
        self.packages.setObjectName("packages")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(450, 90, 71, 30))
        self.label_4.setObjectName("label_4")
        self.keywords = QtWidgets.QLineEdit(self.centralwidget)
        self.keywords.setGeometry(QtCore.QRect(530, 130, 300, 30))
        self.keywords.setObjectName("keywords")
        self.pyrec = QtWidgets.QLineEdit(self.centralwidget)
        self.pyrec.setGeometry(QtCore.QRect(130, 130, 301, 30))
        self.pyrec.setObjectName("pyrec")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(450, 130, 71, 30))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 130, 111, 30))
        self.label_6.setObjectName("label_6")
        self.envList = QtWidgets.QComboBox(self.centralwidget)
        self.envList.setGeometry(QtCore.QRect(130, 170, 220, 30))
        self.envList.setObjectName("envList")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 170, 111, 30))
        self.label_7.setObjectName("label_7")
        self.licList = QtWidgets.QComboBox(self.centralwidget)
        self.licList.setGeometry(QtCore.QRect(530, 170, 221, 30))
        self.licList.setObjectName("licList")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(450, 170, 71, 30))
        self.label_8.setObjectName("label_8")
        self.audList = QtWidgets.QComboBox(self.centralwidget)
        self.audList.setGeometry(QtCore.QRect(530, 210, 221, 30))
        self.audList.setObjectName("audList")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(450, 210, 71, 30))
        self.label_9.setObjectName("label_9")
        self.langList = QtWidgets.QComboBox(self.centralwidget)
        self.langList.setGeometry(QtCore.QRect(130, 210, 221, 30))
        self.langList.setObjectName("langList")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 210, 111, 30))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(10, 260, 81, 30))
        self.label_11.setObjectName("label_11")
        self.classifiers = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.classifiers.setGeometry(QtCore.QRect(130, 260, 701, 181))
        self.classifiers.setReadOnly(True)
        self.classifiers.setObjectName("classifiers")
        self.browse_long_desc = QtWidgets.QPushButton(self.centralwidget)
        self.browse_long_desc.setGeometry(QtCore.QRect(800, 50, 31, 30))
        self.browse_long_desc.setObjectName("browse_long_desc")
        self.find_pack = QtWidgets.QPushButton(self.centralwidget)
        self.find_pack.setGeometry(QtCore.QRect(780, 90, 51, 30))
        self.find_pack.setObjectName("find_pack")
        self.licAdd = QtWidgets.QPushButton(self.centralwidget)
        self.licAdd.setGeometry(QtCore.QRect(760, 170, 31, 30))
        self.licAdd.setObjectName("licAdd")
        self.licRem = QtWidgets.QPushButton(self.centralwidget)
        self.licRem.setGeometry(QtCore.QRect(800, 170, 31, 30))
        self.licRem.setObjectName("licRem")
        self.langRem = QtWidgets.QPushButton(self.centralwidget)
        self.langRem.setGeometry(QtCore.QRect(400, 210, 31, 30))
        self.langRem.setObjectName("langRem")
        self.langAdd = QtWidgets.QPushButton(self.centralwidget)
        self.langAdd.setGeometry(QtCore.QRect(360, 210, 31, 30))
        self.langAdd.setObjectName("langAdd")
        self.build = QtWidgets.QPushButton(self.centralwidget)
        self.build.setGeometry(QtCore.QRect(740, 450, 91, 30))
        self.build.setObjectName("build")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(30, 450, 151, 30))
        self.label_12.setStyleSheet("color: rgb(255, 0, 0);\n"
                                    "font-style: italic;\n"
                                    "text-decoration: underline;\n"
                                    "font-size: 13px")
        self.label_12.setObjectName("label_12")
        self.audRem = QtWidgets.QPushButton(self.centralwidget)
        self.audRem.setGeometry(QtCore.QRect(800, 210, 31, 30))
        self.audRem.setObjectName("audRem")
        self.audAdd = QtWidgets.QPushButton(self.centralwidget)
        self.audAdd.setGeometry(QtCore.QRect(760, 210, 31, 30))
        self.audAdd.setObjectName("audAdd")
        self.envRem = QtWidgets.QPushButton(self.centralwidget)
        self.envRem.setGeometry(QtCore.QRect(400, 170, 31, 30))
        self.envRem.setObjectName("envRem")
        self.envAdd = QtWidgets.QPushButton(self.centralwidget)
        self.envAdd.setGeometry(QtCore.QRect(360, 170, 31, 30))
        self.envAdd.setObjectName("envAdd")
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionsss = QtWidgets.QAction(MainWindow)
        self.actionsss.setObjectName("actionsss")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.shortDesc, self.longDesc)
        MainWindow.setTabOrder(self.longDesc, self.browse_long_desc)
        MainWindow.setTabOrder(self.browse_long_desc, self.dependencies)
        MainWindow.setTabOrder(self.dependencies, self.packages)
        MainWindow.setTabOrder(self.packages, self.find_pack)
        MainWindow.setTabOrder(self.find_pack, self.pyrec)
        MainWindow.setTabOrder(self.pyrec, self.keywords)
        MainWindow.setTabOrder(self.keywords, self.envList)
        MainWindow.setTabOrder(self.envList, self.envAdd)
        MainWindow.setTabOrder(self.envAdd, self.envRem)
        MainWindow.setTabOrder(self.envRem, self.licList)
        MainWindow.setTabOrder(self.licList, self.licAdd)
        MainWindow.setTabOrder(self.licAdd, self.licRem)
        MainWindow.setTabOrder(self.licRem, self.langList)
        MainWindow.setTabOrder(self.langList, self.langAdd)
        MainWindow.setTabOrder(self.langAdd, self.langRem)
        MainWindow.setTabOrder(self.langRem, self.audList)
        MainWindow.setTabOrder(self.audList, self.audAdd)
        MainWindow.setTabOrder(self.audAdd, self.audRem)
        MainWindow.setTabOrder(self.audRem, self.classifiers)
        MainWindow.setTabOrder(self.classifiers, self.build)

        # making combo and initial
        self.envList.addItems(__enviroments__)
        self.audList.addItems(__intended_audience__)
        self.licList.addItems(__license__)
        self.langList.addItems(__programming_lang__)
        self.classifiers.appendPlainText(self.data.dev_status)
        # binding buttons
        self.build.clicked.connect(self.builder)
        self.find_pack.clicked.connect(self.findall)
        self.browse_long_desc.clicked.connect(self.browse)
        self.audAdd.clicked.connect(self.addAud)
        self.audRem.clicked.connect(self.remAud)
        self.envAdd.clicked.connect(self.addEnv)
        self.envRem.clicked.connect(self.remEnv)
        self.langAdd.clicked.connect(self.addLang)
        self.langRem.clicked.connect(self.remLang)
        self.licAdd.clicked.connect(self.addLic)
        self.licRem.clicked.connect(self.remLic)
        self.shortDesc.setPlaceholderText("Enter short description")
        self.longDesc.setPlaceholderText(
            "Enter long description file path or browse. (Markdown file required)"
        )
        self.keywords.setPlaceholderText("Enter keywords for SEO")
        self.dependencies.setPlaceholderText(
            "Enter dependencies (separate by comma)")
        self.pyrec.setPlaceholderText("Enter python version requirements")
        self.packages.setPlaceholderText(
            "Enter python packages to be included or click Find button")

        pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(
            _translate("MainWindow",
                       "Morphine :: Minimal + Dependencies :: Maker"))
        self.label.setText(_translate("MainWindow", "Short Description"))
        self.label_2.setText(_translate("MainWindow", "Long Description"))
        self.label_3.setText(_translate("MainWindow", "Dependecies"))
        self.label_4.setText(_translate("MainWindow", "Packages"))
        self.label_5.setText(_translate("MainWindow", "Keywords"))
        self.label_6.setText(_translate("MainWindow", "Python Required"))
        self.label_7.setText(_translate("MainWindow", "Enviroment"))
        self.label_8.setText(_translate("MainWindow", "License"))
        self.label_9.setText(_translate("MainWindow", "Audience"))
        self.label_10.setText(_translate("MainWindow", "Prog. Language"))
        self.label_11.setText(_translate("MainWindow", "Classifiers"))
        self.browse_long_desc.setText(_translate("MainWindow", "..."))
        self.find_pack.setText(_translate("MainWindow", "Find"))
        self.licAdd.setText(_translate("MainWindow", "+"))
        self.licRem.setText(_translate("MainWindow", "-"))
        self.langRem.setText(_translate("MainWindow", "-"))
        self.langAdd.setText(_translate("MainWindow", "+"))
        self.build.setText(_translate("MainWindow", "&Build"))
        self.label_12.setText(
            _translate("MainWindow", "All fields are mandatory"))
        self.audRem.setText(_translate("MainWindow", "-"))
        self.audAdd.setText(_translate("MainWindow", "+"))
        self.envRem.setText(_translate("MainWindow", "-"))
        self.envAdd.setText(_translate("MainWindow", "+"))
        self.shortDesc.setFocus()
        pass

    def browse(self):
        file = str(
            QtWidgets.QFileDialog.getOpenFileName(
                self.obj, "Select Long Description", ".",
                "Markdown Files (*MD *md)")[0])
        self.longDesc.setText(file)
        pass

    def findall(self):
        self.packages.setText(", ".join(find_packages()))

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

    def builder(self):
        shortDesc = self.shortDesc.text()
        if shortDesc == "":
            QtWidgets.QMessageBox.warning(self.obj, "Empty Field",
                                          "Short description is empty")
            self.shortDesc.setFocus()
            return None

        longDesc = self.longDesc.text()
        if longDesc == "":
            QtWidgets.QMessageBox.warning(self.obj, "Empty Fields",
                                          "Long description is empty")
            self.shortDesc.setFocus()
            return None
        elif not os.path.exists(longDesc):
            QtWidgets.QMessageBox.warning(self.obj, "Not Exitsts",
                                          "Long description file not exists")
            self.longDesc.setFocus()
            return None

        packages = self.packages.text()
        if packages == "":
            QtWidgets.QMessageBox.warning(self.obj, "Empty Fields",
                                          "Packages are empty")
            self.packages.setFocus()
            return None
        else:
            packages = [x.strip() for x in packages.split(",")]

        keywords = self.keywords.text()
        if keywords == "":
            QtWidgets.QMessageBox.warning(self.obj, "Empty Fields",
                                          "Keywords are empty")
            self.keywords.setFocus()
            return None

        pyreq = self.pyrec.text()
        if pyreq == "":
            QtWidgets.QMessageBox.warning(self.obj, "Empty Fields",
                                          "Python version required is empty")
            self.pyrec.setFocus()
            return None

        deps = self.dependencies.text()
        if deps == "":
            QtWidgets.QMessageBox.warning(self.obj, "Empty Fields",
                                          "Python version required is empty")
            self.dependencies.setFocus()
            return None
        else:
            deps = [x.strip() for x in deps.split(",")]

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
                python_required=pyreq,
                install_requires=deps),
            style_config="pep8")[0]
        with open(os.path.join(self.data.dir, "setup.py"), "w") as file:
            file.write(setup)
            file.close()

        QtWidgets.QMessageBox.information(
            self.obj, "Done", "Hurry ^_^\nSetup file has been created")
        pass
