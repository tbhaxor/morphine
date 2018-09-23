from PyQt5 import QtCore, QtGui, QtWidgets
from morphine.globals import __intended_audience__, __enviroments__, __license__, __programming_lang__, find_packages
from yapf.yapflib.yapf_api import FormatCode
import os
from morphine.template import __minimal_exec__ as template
import re


class Ui_minimal_exec_deps(object):
    place = """Set 'Console Script' Entry Points Line By Line
            [executable_name]=[module_name]:[function_name]
            [executable_name]=[module_name].[main module]
            [executable_name]=[module_name].[main module]:[function_name]
For Example:
            morphine-maker=morphine.__main__:executor"""

    def __init__(self, data):
        self.data = data
        pass

    def setupUi(self, minimal_exec_deps):
        minimal_exec_deps.setObjectName("minimal_exec_deps")
        minimal_exec_deps.resize(840, 515)
        minimal_exec_deps.setMinimumSize(QtCore.QSize(840, 515))
        minimal_exec_deps.setMaximumSize(QtCore.QSize(840, 515))
        self.obj = minimal_exec_deps
        resolution = QtWidgets.QDesktopWidget().screenGeometry()
        minimal_exec_deps.move(
            (resolution.width() / 2) -
            (minimal_exec_deps.frameSize().width() / 2),
            (resolution.height() / 2) -
            (minimal_exec_deps.frameSize().height() / 2),
        )
        self.centralwidget = QtWidgets.QWidget(minimal_exec_deps)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 111, 30))
        self.label.setMinimumSize(QtCore.QSize(0, 30))
        self.label.setObjectName("label")
        self.shortDesc = QtWidgets.QLineEdit(self.centralwidget)
        self.shortDesc.setGeometry(QtCore.QRect(120, 10, 711, 30))
        self.shortDesc.setMinimumSize(QtCore.QSize(0, 30))
        self.shortDesc.setObjectName("shortDesc")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 111, 30))
        self.label_2.setMinimumSize(QtCore.QSize(0, 30))
        self.label_2.setObjectName("label_2")
        self.longDesc = QtWidgets.QLineEdit(self.centralwidget)
        self.longDesc.setGeometry(QtCore.QRect(120, 50, 671, 30))
        self.longDesc.setMinimumSize(QtCore.QSize(0, 30))
        self.longDesc.setObjectName("longDesc")
        self.packages = QtWidgets.QLineEdit(self.centralwidget)
        self.packages.setGeometry(QtCore.QRect(530, 90, 251, 30))
        self.packages.setMinimumSize(QtCore.QSize(0, 30))
        self.packages.setObjectName("packages")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 111, 30))
        self.label_3.setMinimumSize(QtCore.QSize(0, 30))
        self.label_3.setObjectName("label_3")
        self.dependencies = QtWidgets.QLineEdit(self.centralwidget)
        self.dependencies.setGeometry(QtCore.QRect(120, 90, 321, 30))
        self.dependencies.setMinimumSize(QtCore.QSize(0, 30))
        self.dependencies.setObjectName("dependencies")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(460, 90, 71, 30))
        self.label_4.setMinimumSize(QtCore.QSize(0, 30))
        self.label_4.setObjectName("label_4")
        self.find_packages = QtWidgets.QPushButton(self.centralwidget)
        self.find_packages.setGeometry(QtCore.QRect(790, 90, 41, 30))
        self.find_packages.setMinimumSize(QtCore.QSize(0, 30))
        self.find_packages.setObjectName("find_packages")
        self.browse_long_desc = QtWidgets.QPushButton(self.centralwidget)
        self.browse_long_desc.setGeometry(QtCore.QRect(800, 50, 31, 30))
        self.browse_long_desc.setMinimumSize(QtCore.QSize(0, 30))
        self.browse_long_desc.setObjectName("browse_long_desc")
        self.entrypoints = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.entrypoints.setGeometry(QtCore.QRect(120, 130, 711, 101))
        self.entrypoints.setObjectName("entrypoints")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 130, 111, 30))
        self.label_5.setMinimumSize(QtCore.QSize(0, 30))
        self.label_5.setObjectName("label_5")
        self.envList = QtWidgets.QComboBox(self.centralwidget)
        self.envList.setGeometry(QtCore.QRect(120, 280, 221, 30))
        self.envList.setMinimumSize(QtCore.QSize(0, 30))
        self.envList.setObjectName("envList")
        self.envAdd = QtWidgets.QPushButton(self.centralwidget)
        self.envAdd.setGeometry(QtCore.QRect(350, 280, 31, 30))
        self.envAdd.setMinimumSize(QtCore.QSize(0, 30))
        self.envAdd.setObjectName("envAdd")
        self.envRem = QtWidgets.QPushButton(self.centralwidget)
        self.envRem.setGeometry(QtCore.QRect(390, 280, 31, 30))
        self.envRem.setMinimumSize(QtCore.QSize(0, 30))
        self.envRem.setObjectName("envRem")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 280, 111, 30))
        self.label_6.setMinimumSize(QtCore.QSize(0, 30))
        self.label_6.setObjectName("label_6")
        self.licRem = QtWidgets.QPushButton(self.centralwidget)
        self.licRem.setGeometry(QtCore.QRect(800, 280, 31, 30))
        self.licRem.setMinimumSize(QtCore.QSize(0, 30))
        self.licRem.setObjectName("licRem")
        self.licAdd = QtWidgets.QPushButton(self.centralwidget)
        self.licAdd.setGeometry(QtCore.QRect(760, 280, 31, 30))
        self.licAdd.setMinimumSize(QtCore.QSize(0, 30))
        self.licAdd.setObjectName("licAdd")
        self.licList = QtWidgets.QComboBox(self.centralwidget)
        self.licList.setGeometry(QtCore.QRect(530, 280, 221, 30))
        self.licList.setMinimumSize(QtCore.QSize(0, 30))
        self.licList.setObjectName("licList")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(440, 280, 71, 30))
        self.label_7.setMinimumSize(QtCore.QSize(0, 30))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(440, 320, 111, 30))
        self.label_8.setMinimumSize(QtCore.QSize(0, 30))
        self.label_8.setObjectName("label_8")
        self.audRem = QtWidgets.QPushButton(self.centralwidget)
        self.audRem.setGeometry(QtCore.QRect(390, 320, 31, 30))
        self.audRem.setMinimumSize(QtCore.QSize(0, 30))
        self.audRem.setObjectName("audRem")
        self.langAdd = QtWidgets.QPushButton(self.centralwidget)
        self.langAdd.setGeometry(QtCore.QRect(760, 320, 31, 30))
        self.langAdd.setMinimumSize(QtCore.QSize(0, 30))
        self.langAdd.setObjectName("langAdd")
        self.audAdd = QtWidgets.QPushButton(self.centralwidget)
        self.audAdd.setGeometry(QtCore.QRect(350, 320, 31, 30))
        self.audAdd.setMinimumSize(QtCore.QSize(0, 30))
        self.audAdd.setObjectName("audAdd")
        self.audList = QtWidgets.QComboBox(self.centralwidget)
        self.audList.setGeometry(QtCore.QRect(120, 320, 221, 30))
        self.audList.setMinimumSize(QtCore.QSize(0, 30))
        self.audList.setObjectName("audList")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 320, 111, 30))
        self.label_9.setMinimumSize(QtCore.QSize(0, 30))
        self.label_9.setObjectName("label_9")
        self.langList = QtWidgets.QComboBox(self.centralwidget)
        self.langList.setGeometry(QtCore.QRect(530, 320, 221, 30))
        self.langList.setMinimumSize(QtCore.QSize(0, 30))
        self.langList.setObjectName("langList")
        self.langRem = QtWidgets.QPushButton(self.centralwidget)
        self.langRem.setGeometry(QtCore.QRect(800, 320, 31, 30))
        self.langRem.setMinimumSize(QtCore.QSize(0, 30))
        self.langRem.setObjectName("langRem")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 360, 111, 30))
        self.label_10.setMinimumSize(QtCore.QSize(0, 30))
        self.label_10.setObjectName("label_10")
        self.classifiers = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.classifiers.setGeometry(QtCore.QRect(120, 360, 711, 101))
        self.classifiers.setReadOnly(True)
        self.classifiers.setObjectName("classifiers")
        self.build = QtWidgets.QPushButton(self.centralwidget)
        self.build.setGeometry(QtCore.QRect(750, 470, 81, 30))
        self.build.setMinimumSize(QtCore.QSize(0, 30))
        self.build.setObjectName("build")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(20, 470, 351, 30))
        self.label_11.setMinimumSize(QtCore.QSize(0, 30))
        self.label_11.setStyleSheet("color: red;\n"
                                    "text-decoration: underline;\n"
                                    "font-style: italic;")
        self.label_11.setObjectName("label_11")
        self.pyreq = QtWidgets.QLineEdit(self.centralwidget)
        self.pyreq.setGeometry(QtCore.QRect(120, 240, 321, 30))
        self.pyreq.setMinimumSize(QtCore.QSize(0, 30))
        self.pyreq.setObjectName("pyreq")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(460, 240, 71, 30))
        self.label_12.setMinimumSize(QtCore.QSize(0, 30))
        self.label_12.setObjectName("label_12")
        self.keywords = QtWidgets.QLineEdit(self.centralwidget)
        self.keywords.setGeometry(QtCore.QRect(530, 240, 301, 30))
        self.keywords.setMinimumSize(QtCore.QSize(0, 30))
        self.keywords.setObjectName("keywords")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(10, 240, 111, 30))
        self.label_13.setMinimumSize(QtCore.QSize(0, 30))
        self.label_13.setObjectName("label_13")
        minimal_exec_deps.setCentralWidget(self.centralwidget)
        self.entrypoints.setPlaceholderText(self.place)
        self.retranslateUi(minimal_exec_deps)
        QtCore.QMetaObject.connectSlotsByName(minimal_exec_deps)
        minimal_exec_deps.setTabOrder(self.shortDesc, self.longDesc)
        minimal_exec_deps.setTabOrder(self.longDesc, self.browse_long_desc)
        minimal_exec_deps.setTabOrder(self.browse_long_desc, self.dependencies)
        minimal_exec_deps.setTabOrder(self.dependencies, self.packages)
        minimal_exec_deps.setTabOrder(self.packages, self.find_packages)
        minimal_exec_deps.setTabOrder(self.find_packages, self.entrypoints)
        minimal_exec_deps.setTabOrder(self.entrypoints, self.pyreq)
        minimal_exec_deps.setTabOrder(self.pyreq, self.keywords)
        minimal_exec_deps.setTabOrder(self.keywords, self.envList)
        minimal_exec_deps.setTabOrder(self.envList, self.envAdd)
        minimal_exec_deps.setTabOrder(self.envAdd, self.envRem)
        minimal_exec_deps.setTabOrder(self.envRem, self.licList)
        minimal_exec_deps.setTabOrder(self.licList, self.licAdd)
        minimal_exec_deps.setTabOrder(self.licAdd, self.licRem)
        minimal_exec_deps.setTabOrder(self.licRem, self.audList)
        minimal_exec_deps.setTabOrder(self.audList, self.audAdd)
        minimal_exec_deps.setTabOrder(self.audAdd, self.audRem)
        minimal_exec_deps.setTabOrder(self.audRem, self.langList)
        minimal_exec_deps.setTabOrder(self.langList, self.langAdd)
        minimal_exec_deps.setTabOrder(self.langAdd, self.langRem)
        minimal_exec_deps.setTabOrder(self.langRem, self.classifiers)
        minimal_exec_deps.setTabOrder(self.classifiers, self.build)

        # bind data
        self.classifiers.appendPlainText(self.data.dev_status)
        self.audList.addItems(__intended_audience__)
        self.envList.addItems(__enviroments__)
        self.langList.addItems(__programming_lang__)
        self.licList.addItems(__license__)
        # bind buttons
        self.find_packages.clicked.connect(self.pac)
        self.audAdd.clicked.connect(self.addAud)
        self.audRem.clicked.connect(self.remAud)
        self.envAdd.clicked.connect(self.addEnv)
        self.envRem.clicked.connect(self.remEnv)
        self.langAdd.clicked.connect(self.addLang)
        self.langRem.clicked.connect(self.remLang)
        self.licAdd.clicked.connect(self.addLic)
        self.licRem.clicked.connect(self.remLic)
        self.browse_long_desc.clicked.connect(self.mark)
        self.build.clicked.connect(self.builder)
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

        deps = self.dependencies.text()
        if deps == "":
            QtWidgets.QMessageBox.warning(self.obj, "Empty Fields",
                                          "Python version required is empty")
            self.dependencies.setFocus()
            return None
        else:
            deps = [x.strip() for x in deps.split(",")]

        # python version
        pyreq = self.pyreq.text()
        if pyreq == "":
            QtWidgets.QMessageBox.warning(self.obj, "Empty Fields",
                                          "Python version required is empty")
            self.pyreq.setFocus()
            return None

        classifiers = self.classifiers.toPlainText().split("\n")
        execu = self.entrypoints.toPlainText().split("\n")
        if len(execu) == 0:
            QtWidgets.QMessageBox.warning(self.obj, "Empty Fields",
                                          "Entry point is empty")
            self.entrypoints.setFocus()
            return None
        elif not self.validateEntry():
            QtWidgets.QMessageBox.information(
                self.obj, "Invalid Input",
                "Entry points will not be accepted by pypi")
            self.entrypoints.setFocus()
        else:
            execu = {"console_scripts": execu}
            pass

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
                entry_points=execu,
                install_requires=deps),
            style_config="pep8")[0]
        with open(os.path.join(self.data.dir, "setup.py"), "w") as file:
            file.write(setup)
            file.close()

        QtWidgets.QMessageBox.information(
            self.obj, "Done", "Hurry ^_^\nSetup file has been created")
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

    def validateEntry(self):
        entrypoints = self.entrypoints.toPlainText().split("\n")
        for entrypoint in entrypoints:
            if re.match(r"^.+=.+\.?.+(:.+)?$", entrypoint) is None:
                return False
            pass
        return True

    def mark(self):
        file = str(
            QtWidgets.QFileDialog.getOpenFileName(
                self.obj, "Select Long Description", ".",
                "Markdown Files (*MD *md)")[0])
        self.longDesc.setText(file)
        pass

    def pac(self):
        self.packages.setText(", ".join(find_packages()))
        pass

    def retranslateUi(self, minimal_exec_deps):
        _translate = QtCore.QCoreApplication.translate
        minimal_exec_deps.setWindowTitle(
            _translate(
                "minimal_exec_deps",
                "Morphine :: Minimal + Executable + Dependencies :: Builder"))
        self.label.setText(
            _translate("minimal_exec_deps", "Short Description"))
        self.shortDesc.setPlaceholderText(
            _translate("minimal_exec_deps", "Enter short description"))
        self.label_2.setText(
            _translate("minimal_exec_deps", "Long Description"))
        self.longDesc.setPlaceholderText(
            _translate(
                "minimal_exec_deps",
                "Enter file containing long description or browse it (Markdown required)"
            ))
        self.packages.setPlaceholderText(
            _translate("minimal_exec_deps",
                       "Enter packages to include or click Find"))
        self.label_3.setText(_translate("minimal_exec_deps", "Dependencies"))
        self.dependencies.setPlaceholderText(
            _translate("minimal_exec_deps",
                       "Enter package dependencies (separate by comma)"))
        self.label_4.setText(_translate("minimal_exec_deps", "Packages"))
        self.find_packages.setText(_translate("minimal_exec_deps", "&Find"))
        self.browse_long_desc.setText(_translate("minimal_exec_deps", ".."))
        self.label_5.setText(_translate("minimal_exec_deps", "Entry Points"))
        self.envAdd.setText(_translate("minimal_exec_deps", "+"))
        self.envRem.setText(_translate("minimal_exec_deps", "-"))
        self.label_6.setText(_translate("minimal_exec_deps", "Enviroments"))
        self.licRem.setText(_translate("minimal_exec_deps", "-"))
        self.licAdd.setText(_translate("minimal_exec_deps", "+"))
        self.label_7.setText(_translate("minimal_exec_deps", "License"))
        self.label_8.setText(_translate("minimal_exec_deps", "Language"))
        self.audRem.setText(_translate("minimal_exec_deps", "-"))
        self.langAdd.setText(_translate("minimal_exec_deps", "+"))
        self.audAdd.setText(_translate("minimal_exec_deps", "+"))
        self.label_9.setText(_translate("minimal_exec_deps", "Audience"))
        self.langRem.setText(_translate("minimal_exec_deps", "-"))
        self.label_10.setText(_translate("minimal_exec_deps", "Classifiers"))
        self.build.setText(_translate("minimal_exec_deps", "&Build"))
        self.label_11.setText(
            _translate("minimal_exec_deps", "All fields are mandatory"))
        self.pyreq.setPlaceholderText(
            _translate("minimal_exec_deps",
                       "Enter python version required, (separate by commas)"))
        self.label_12.setText(_translate("minimal_exec_deps", "Keywords"))
        self.keywords.setPlaceholderText(
            _translate("minimal_exec_deps", "Enter keywords for SEO"))
        self.label_13.setText(
            _translate("minimal_exec_deps", "Python Required"))
        pass

    pass