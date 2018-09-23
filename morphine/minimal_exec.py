from PyQt5 import QtCore, QtGui, QtWidgets
from morphine.globals import __intended_audience__, __enviroments__, __license__, __programming_lang__, find_packages
from yapf.yapflib.yapf_api import FormatCode
import os
from morphine.template import __minimal_exec__ as template
import re


class Ui_minimal_exec(object):

    place = """Set 'Console Script' Entry Points Line By Line
            [executable_name]=[module_name]:[function_name]
            [executable_name]=[module_name].[main module]
            [executable_name]=[module_name].[main module]:[function_name]
For Example:
            morphine-maker=morphine.__main__:executor"""

    def __init__(self, data):
        self.data = data
        try:
            self.data.dir
        except KeyError:
            self.data.dir = "."

        pass

    def setupUi(self, minimal_exec):
        minimal_exec.setObjectName("minimal_exec")
        minimal_exec.resize(866, 488)
        minimal_exec.setMinimumSize(QtCore.QSize(866, 488))
        minimal_exec.setMaximumSize(QtCore.QSize(866, 488))
        resolution = QtWidgets.QDesktopWidget().screenGeometry()
        minimal_exec.move(
            (resolution.width() / 2) - (minimal_exec.frameSize().width() / 2),
            (resolution.height() / 2) -
            (minimal_exec.frameSize().height() / 2),
        )
        self.centralwidget = QtWidgets.QWidget(minimal_exec)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 111, 30))
        self.label.setObjectName("label")
        self.shortDesc = QtWidgets.QLineEdit(self.centralwidget)
        self.shortDesc.setGeometry(QtCore.QRect(120, 10, 731, 30))
        self.shortDesc.setObjectName("shortDesc")
        self.longDesc = QtWidgets.QLineEdit(self.centralwidget)
        self.longDesc.setGeometry(QtCore.QRect(120, 50, 690, 30))
        self.longDesc.setText("")
        self.longDesc.setObjectName("longDesc")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 101, 30))
        self.label_2.setObjectName("label_2")
        self.browse_long_desc = QtWidgets.QPushButton(self.centralwidget)
        self.browse_long_desc.setGeometry(QtCore.QRect(820, 50, 31, 30))
        self.browse_long_desc.setObjectName("browse_long_desc")
        self.packages = QtWidgets.QLineEdit(self.centralwidget)
        self.packages.setGeometry(QtCore.QRect(120, 90, 651, 30))
        self.packages.setText("")
        self.packages.setObjectName("packages")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 101, 30))
        self.label_3.setObjectName("label_3")
        self.find_packages = QtWidgets.QPushButton(self.centralwidget)
        self.find_packages.setGeometry(QtCore.QRect(780, 90, 71, 30))
        self.find_packages.setObjectName("find_packages")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 130, 101, 30))
        self.label_4.setObjectName("label_4")
        self.entrypoints = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.entrypoints.setGeometry(QtCore.QRect(120, 130, 731, 91))
        self.entrypoints.setReadOnly(False)
        self.entrypoints.setObjectName("entrypoints")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 230, 101, 30))
        self.label_5.setObjectName("label_5")
        self.keywords = QtWidgets.QLineEdit(self.centralwidget)
        self.keywords.setGeometry(QtCore.QRect(120, 230, 320, 30))
        self.keywords.setObjectName("keywords")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(450, 230, 81, 30))
        self.label_6.setObjectName("label_6")
        self.pyreq = QtWidgets.QLineEdit(self.centralwidget)
        self.pyreq.setGeometry(QtCore.QRect(530, 230, 320, 30))
        self.pyreq.setObjectName("pyreq")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 270, 101, 30))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(450, 270, 81, 30))
        self.label_8.setObjectName("label_8")
        self.envList = QtWidgets.QComboBox(self.centralwidget)
        self.envList.setGeometry(QtCore.QRect(120, 270, 241, 30))
        self.envList.setObjectName("envList")
        self.envRem = QtWidgets.QPushButton(self.centralwidget)
        self.envRem.setGeometry(QtCore.QRect(410, 270, 31, 30))
        self.envRem.setObjectName("envRem")
        self.envAdd = QtWidgets.QPushButton(self.centralwidget)
        self.envAdd.setGeometry(QtCore.QRect(370, 270, 31, 30))
        self.envAdd.setObjectName("envAdd")
        self.audList = QtWidgets.QComboBox(self.centralwidget)
        self.audList.setGeometry(QtCore.QRect(530, 270, 241, 30))
        self.audList.setObjectName("audList")
        self.audAdd = QtWidgets.QPushButton(self.centralwidget)
        self.audAdd.setGeometry(QtCore.QRect(780, 270, 31, 30))
        self.audAdd.setObjectName("audAdd")
        self.audRem = QtWidgets.QPushButton(self.centralwidget)
        self.audRem.setGeometry(QtCore.QRect(820, 270, 31, 30))
        self.audRem.setObjectName("audRem")
        self.licList = QtWidgets.QComboBox(self.centralwidget)
        self.licList.setGeometry(QtCore.QRect(530, 310, 241, 30))
        self.licList.setObjectName("licList")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(450, 310, 81, 30))
        self.label_9.setObjectName("label_9")
        self.langList = QtWidgets.QComboBox(self.centralwidget)
        self.langList.setGeometry(QtCore.QRect(120, 310, 241, 30))
        self.langList.setObjectName("langList")
        self.langAdd = QtWidgets.QPushButton(self.centralwidget)
        self.langAdd.setGeometry(QtCore.QRect(370, 310, 31, 30))
        self.langAdd.setObjectName("langAdd")
        self.licRem = QtWidgets.QPushButton(self.centralwidget)
        self.licRem.setGeometry(QtCore.QRect(820, 310, 31, 30))
        self.licRem.setObjectName("licRem")
        self.langRem = QtWidgets.QPushButton(self.centralwidget)
        self.langRem.setGeometry(QtCore.QRect(410, 310, 31, 30))
        self.langRem.setObjectName("langRem")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 310, 101, 30))
        self.label_10.setObjectName("label_10")
        self.licAdd = QtWidgets.QPushButton(self.centralwidget)
        self.licAdd.setGeometry(QtCore.QRect(780, 310, 31, 30))
        self.licAdd.setObjectName("licAdd")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(10, 350, 101, 30))
        self.label_11.setObjectName("label_11")
        self.classifiers = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.classifiers.setGeometry(QtCore.QRect(120, 350, 731, 91))
        self.classifiers.setReadOnly(True)
        self.classifiers.setObjectName("classifiers")
        self.build = QtWidgets.QPushButton(self.centralwidget)
        self.build.setGeometry(QtCore.QRect(770, 450, 81, 30))
        self.build.setObjectName("build")
        minimal_exec.setCentralWidget(self.centralwidget)

        self.retranslateUi(minimal_exec)
        QtCore.QMetaObject.connectSlotsByName(minimal_exec)
        minimal_exec.setTabOrder(self.shortDesc, self.longDesc)
        minimal_exec.setTabOrder(self.longDesc, self.browse_long_desc)
        minimal_exec.setTabOrder(self.browse_long_desc, self.packages)
        minimal_exec.setTabOrder(self.packages, self.find_packages)
        minimal_exec.setTabOrder(self.find_packages, self.entrypoints)
        minimal_exec.setTabOrder(self.entrypoints, self.keywords)
        minimal_exec.setTabOrder(self.keywords, self.pyreq)
        minimal_exec.setTabOrder(self.pyreq, self.envList)
        minimal_exec.setTabOrder(self.envList, self.envAdd)
        minimal_exec.setTabOrder(self.envAdd, self.envRem)
        minimal_exec.setTabOrder(self.envRem, self.audList)
        minimal_exec.setTabOrder(self.audList, self.audAdd)
        minimal_exec.setTabOrder(self.audAdd, self.audRem)
        minimal_exec.setTabOrder(self.audRem, self.langList)
        minimal_exec.setTabOrder(self.langList, self.langAdd)
        minimal_exec.setTabOrder(self.langAdd, self.langRem)
        minimal_exec.setTabOrder(self.langRem, self.licList)
        minimal_exec.setTabOrder(self.licList, self.licAdd)
        minimal_exec.setTabOrder(self.licAdd, self.licRem)
        minimal_exec.setTabOrder(self.licRem, self.classifiers)
        minimal_exec.setTabOrder(self.classifiers, self.build)
        self.entrypoints.setPlaceholderText(self.place)
        self.obj = minimal_exec
        # adding data
        self.audList.addItems(__intended_audience__)
        self.envList.addItems(__enviroments__)
        self.langList.addItems(__programming_lang__)
        self.licList.addItems(__license__)
        # binds
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
                entry_points=execu),
            style_config="pep8")[0]
        with open(os.path.join(self.data.dir, "setup.py"), "w") as file:
            file.write(setup)
            file.close()

        QtWidgets.QMessageBox.information(
            self.obj, "Done", "Hurry ^_^\nSetup file has been created")
        pass

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

    def retranslateUi(self, minimal_exec):
        _translate = QtCore.QCoreApplication.translate
        minimal_exec.setWindowTitle(
            _translate("minimal_exec",
                       "Morphine :: Minimal + Executable :: Builder"))
        self.label.setText(_translate("minimal_exec", "Short Description"))
        self.shortDesc.setPlaceholderText(
            _translate("minimal_exec", "Enter short description", "sss"))
        self.longDesc.setPlaceholderText(
            _translate(
                "minimal_exec",
                "Enter long description file path or browse. (Markdown file required)"
            ))
        self.label_2.setText(_translate("minimal_exec", "Long Description"))
        self.browse_long_desc.setText(_translate("minimal_exec", "..."))
        self.packages.setPlaceholderText(
            _translate("minimal_exec", "Enter packges to include or find it"))
        self.label_3.setText(_translate("minimal_exec", "Packages"))
        self.find_packages.setText(_translate("minimal_exec", "&Find"))
        self.label_4.setText(_translate("minimal_exec", "Entry Points"))
        self.label_5.setText(_translate("minimal_exec", "Keywords"))
        self.keywords.setPlaceholderText(
            _translate("minimal_exec", "Enter keywords for SEO"))
        self.label_6.setText(_translate("minimal_exec", "Python Req."))
        self.pyreq.setPlaceholderText(
            _translate("minimal_exec", "Enter python version(s) required"))
        self.label_7.setText(_translate("minimal_exec", "Enviroment"))
        self.label_8.setText(_translate("minimal_exec", "Audience"))
        self.envRem.setText(_translate("minimal_exec", "-"))
        self.envAdd.setText(_translate("minimal_exec", "+"))
        self.audAdd.setText(_translate("minimal_exec", "+"))
        self.audRem.setText(_translate("minimal_exec", "-"))
        self.label_9.setText(_translate("minimal_exec", "Audience"))
        self.langAdd.setText(_translate("minimal_exec", "+"))
        self.licRem.setText(_translate("minimal_exec", "-"))
        self.langRem.setText(_translate("minimal_exec", "-"))
        self.label_10.setText(_translate("minimal_exec", "Enviroment"))
        self.licAdd.setText(_translate("minimal_exec", "+"))
        self.label_11.setText(_translate("minimal_exec", "Entry Points"))
        self.build.setText(_translate("minimal_exec", "&Build"))
        self.classifiers.appendPlainText(
            _translate("minimal_exec", self.data.dev_status))
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
