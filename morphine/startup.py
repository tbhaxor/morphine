from PyQt5 import QtCore, QtGui, QtWidgets
from webbrowser import open_new_tab
from morphine.minimal import Ui_minimal
from morphine.globals import MorphineDict
from morphine.minimal_deps import Ui_minimal_deps
from morphine.minimal_exec import Ui_minimal_exec
from morphine.minimal_exec_deps import Ui_minimal_exec_deps
import re
import os


class Ui_startup(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(851, 360)
        Dialog.setMinimumSize(QtCore.QSize(851, 360))
        Dialog.setMaximumSize(QtCore.QSize(851, 360))
        resolution = QtWidgets.QDesktopWidget().screenGeometry()
        Dialog.move(
            (resolution.width() / 2) - (Dialog.frameSize().width() / 2),
            (resolution.height() / 2) - (Dialog.frameSize().height() / 2),
        )

        self.next = QtWidgets.QPushButton(Dialog)
        self.next.setGeometry(QtCore.QRect(740, 310, 98, 29))
        self.next.setObjectName("next")
        self.exit = QtWidgets.QPushButton(Dialog)
        self.exit.setGeometry(QtCore.QRect(630, 310, 98, 29))
        self.exit.setObjectName("exit")
        self.lbl_link = QtWidgets.QLabel(Dialog)
        self.lbl_link.setGeometry(QtCore.QRect(10, 320, 201, 17))
        self.lbl_link.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lbl_link.setObjectName("lbl_link")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 150, 91, 30))
        self.label_2.setObjectName("label_2")
        self.authorname = QtWidgets.QLineEdit(Dialog)
        self.authorname.setGeometry(QtCore.QRect(130, 149, 271, 30))
        self.authorname.setObjectName("authorname")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(430, 150, 91, 30))
        self.label_3.setObjectName("label_3")
        self.authoremail = QtWidgets.QLineEdit(Dialog)
        self.authoremail.setGeometry(QtCore.QRect(550, 150, 291, 30))
        self.authoremail.setObjectName("authoremail")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 191, 91, 30))
        self.label_4.setObjectName("label_4")
        self.downurl = QtWidgets.QLineEdit(Dialog)
        self.downurl.setGeometry(QtCore.QRect(550, 191, 291, 30))
        self.downurl.setObjectName("downurl")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(430, 192, 101, 30))
        self.label_5.setObjectName("label_5")
        self.homeurl = QtWidgets.QLineEdit(Dialog)
        self.homeurl.setGeometry(QtCore.QRect(130, 190, 271, 30))
        self.homeurl.setObjectName("homeurl")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 19, 91, 30))
        self.label_6.setObjectName("label_6")
        self.major_v = QtWidgets.QLineEdit(Dialog)
        self.major_v.setGeometry(QtCore.QRect(550, 21, 90, 30))
        self.major_v.setObjectName("major_v")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(430, 22, 101, 30))
        self.label_7.setObjectName("label_7")
        self.projname = QtWidgets.QLineEdit(Dialog)
        self.projname.setGeometry(QtCore.QRect(130, 19, 271, 30))
        self.projname.setObjectName("projname")
        self.minor_v = QtWidgets.QLineEdit(Dialog)
        self.minor_v.setGeometry(QtCore.QRect(650, 20, 90, 30))
        self.minor_v.setObjectName("minor_v")
        self.patch_v = QtWidgets.QLineEdit(Dialog)
        self.patch_v.setGeometry(QtCore.QRect(750, 20, 90, 30))
        self.patch_v.setObjectName("patch_v")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(10, 61, 91, 30))
        self.label_8.setObjectName("label_8")
        self.devstat = QtWidgets.QComboBox(Dialog)
        self.devstat.setGeometry(QtCore.QRect(130, 60, 271, 30))
        self.devstat.setObjectName("devstat")
        self.devstat.addItem("")
        self.devstat.addItem("")
        self.devstat.addItem("")
        self.devstat.addItem("")
        self.devstat.addItem("")
        self.devstat.addItem("")
        self.devstat.addItem("")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(430, 60, 91, 30))
        self.label_9.setObjectName("label_9")
        self.license = QtWidgets.QLineEdit(Dialog)
        self.license.setGeometry(QtCore.QRect(550, 60, 291, 30))
        self.license.setObjectName("license")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(10, 101, 121, 30))
        self.label_10.setObjectName("label_10")
        self.projdir = QtWidgets.QLineEdit(Dialog)
        self.projdir.setGeometry(QtCore.QRect(130, 100, 651, 30))
        self.projdir.setObjectName("projdir")
        self.browse_projdir = QtWidgets.QPushButton(Dialog)
        self.browse_projdir.setGeometry(QtCore.QRect(800, 100, 41, 30))
        self.browse_projdir.setObjectName("browse_projdir")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(10, 230, 141, 30))
        self.label_11.setObjectName("label_11")
        self.setuptemplate = QtWidgets.QComboBox(Dialog)
        self.setuptemplate.setGeometry(QtCore.QRect(130, 230, 271, 30))
        self.setuptemplate.setObjectName("setuptemplate")
        self.setuptemplate.addItem("")
        self.setuptemplate.addItem("")
        self.setuptemplate.addItem("")
        self.setuptemplate.addItem("")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.lbl_link.mousePressEvent = self.openlnk
        self.exit.clicked.connect(self.quit_e)
        self.next.clicked.connect(self.validate)
        self.obj = Dialog
        self.browse_projdir.clicked.connect(self.browse)
        Dialog.setTabOrder(self.projname, self.major_v)
        Dialog.setTabOrder(self.major_v, self.minor_v)
        Dialog.setTabOrder(self.minor_v, self.patch_v)
        Dialog.setTabOrder(self.patch_v, self.devstat)
        Dialog.setTabOrder(self.devstat, self.license)
        Dialog.setTabOrder(self.license, self.projdir)
        Dialog.setTabOrder(self.projdir, self.browse_projdir)
        Dialog.setTabOrder(self.browse_projdir, self.authorname)
        Dialog.setTabOrder(self.authorname, self.authoremail)
        Dialog.setTabOrder(self.authoremail, self.homeurl)
        Dialog.setTabOrder(self.homeurl, self.downurl)
        Dialog.setTabOrder(self.downurl, self.setuptemplate)
        Dialog.setTabOrder(self.setuptemplate, self.exit)
        Dialog.setTabOrder(self.exit, self.next)
        pass

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Morphine :: Startup"))
        self.next.setText(_translate("Dialog", "&Next"))
        self.exit.setText(_translate("Dialog", "&Exit"))
        self.lbl_link.setText(
            _translate(
                "Dialog",
                '<html><head/><body><p><span style=" text-decoration: underline;color:blue;">https://tbhaxor.me/morphine</span></p></body></html>',
            ))
        self.label_2.setText(_translate("Dialog", "Author Name"))
        self.label_3.setText(_translate("Dialog", "Author Email"))
        self.label_4.setText(_translate("Dialog", "Home URL"))
        self.label_5.setText(_translate("Dialog", "Download URL"))
        self.label_6.setText(_translate("Dialog", "Project Name"))
        self.label_7.setText(_translate("Dialog", "Project version"))
        self.label_8.setText(_translate("Dialog", "Project Status"))
        self.devstat.setItemText(0, _translate("Dialog", "Planning"))
        self.devstat.setItemText(1, _translate("Dialog", "Pre-Alpha"))
        self.devstat.setItemText(2, _translate("Dialog", "Alpha"))
        self.devstat.setItemText(3, _translate("Dialog", "Beta"))
        self.devstat.setItemText(4, _translate("Dialog", "Production/Stable"))
        self.devstat.setItemText(5, _translate("Dialog", "Mature"))
        self.devstat.setItemText(6, _translate("Dialog", "Inactive"))
        self.label_9.setText(_translate("Dialog", "License"))
        self.label_10.setText(_translate("Dialog", "Project Directory"))
        self.browse_projdir.setText(_translate("Dialog", "..."))
        self.label_11.setText(_translate("Dialog", "Setup Template"))
        self.setuptemplate.setItemText(0, _translate("Dialog", "Minimal"))
        self.setuptemplate.setItemText(
            1, _translate("Dialog", "Minimal + Dependencies"))
        self.setuptemplate.setItemText(
            2, _translate("Dialog", "Minimal + Executable"))
        self.setuptemplate.setItemText(
            3, _translate("Dialog", "Minimal + Dependencies + Executable"))
        self.projname.setPlaceholderText(
            _translate("Dialog", "Unique project name (pip install [name])"))
        self.major_v.setPlaceholderText(_translate("Dialog", "Major Version"))
        self.minor_v.setPlaceholderText(_translate("Dialog", "Minor Version"))
        self.patch_v.setPlaceholderText(_translate("Dialog", "Patch Version"))
        self.license.setPlaceholderText(
            _translate("Dialog", "Project License (optional)"))
        self.projdir.setPlaceholderText(
            _translate("Dialog", "Enter project directory or browse it"))
        self.authoremail.setPlaceholderText(
            _translate("Dialog", "Enter author email"))
        self.authorname.setPlaceholderText(
            _translate("Dialog", "Enter author name"))
        self.homeurl.setPlaceholderText(
            _translate("Dialog", "Enter homepage url"))
        self.downurl.setPlaceholderText(
            _translate("Dialog", "Enter download url"))
        self.browse_projdir.setToolTip("Browses project directory")
        self.projname.setFocus()
        pass

    def openlnk(self, x):
        open_new_tab("https://tbhaxor.me/morphine")
        pass

    def quit_e(self, e=""):
        exit(0)
        pass

    def validate(self, e=""):
        params = MorphineDict()
        params.dir = "."
        # validating project name
        name = self.projname.text()
        if name == "":
            QtWidgets.QMessageBox.warning(self.obj, "Empty Fields",
                                          "Project name is mandatory")
            self.projname.setFocus()
            return None
        else:
            params.name = name

        # validating version
        v = self.major_v.text() + "." + self.minor_v.text(
        ) + "." + self.patch_v.text()
        if not re.match(r".+\..+\..+", v):
            QtWidgets.QMessageBox.warning(self.obj, "Invalid Input",
                                          "All version fields are mandatory")
            self.major_v.setFocus()
            return None
        else:
            params.version = v

        params.license = self.license.text()

        # validating author name
        aname = self.authorname.text()
        if aname == "":
            QtWidgets.QMessageBox.warning(self.obj, "Empty Field",
                                          "Author Name is empty")
            self.authorname.setFocus()
            return None

        else:
            params.authorname = aname

        # validating author email
        aemail = self.authoremail.text()
        if aemail == "":
            QtWidgets.QMessageBox.warning(self.obj, "Empty Field",
                                          "Author Email is empty")
            self.authoremail.setFocus()
            return None
        elif not re.match(r"^.+@.+\..+$", aemail):
            QtWidgets.QMessageBox.warning(self.obj, "Invalid Field",
                                          "Email will not be accepted")
            self.authoremail.setFocus()
            return None
        else:
            params.authoremail = aemail

        # validating project directory
        pdir = self.projdir.text()
        if pdir == "":
            QtWidgets.QMessageBox.warning(self.obj, "Empty Field",
                                          "Project Build Directory is empty")
            self.browse()
            return None
        elif not os.path.exists(pdir):
            QtWidgets.QMessageBox.warning(self.obj, "Directory Not Exists",
                                          "Project Build Directory doesn't")
            self.browse()
            return None
        else:
            params.dir = pdir

        # validating home url
        hurl = self.homeurl.text()
        if hurl == "":
            QtWidgets.QMessageBox.warning(self.obj, "Empty Field",
                                          "Home url is empty")
            self.homeurl.setFocus()
            return None
        else:
            params.home_url = hurl

        # validating download url
        durl = self.downurl.text()
        if durl == "":
            QtWidgets.QMessageBox.warning(self.obj, "Empty Field",
                                          "Home url is empty")
            self.downurl.setFocus()
            return None
        else:
            params.down_url = durl

        params.dev_status = ("Development Status :: {} - ".format(
            self.devstat.currentIndex() + 1) + self.devstat.currentText())

        # selecting template
        self.makerWindow = QtWidgets.QMainWindow()
        self.wi = None

        index = self.setuptemplate.currentIndex()
        if index == 0:
            self.wi = Ui_minimal(params)
            self.wi.setupUi(self.makerWindow)
        elif index == 1:
            self.wi = Ui_minimal_deps(params)
            self.wi.setupUi(self.makerWindow)
        elif index == 2:
            self.wi = Ui_minimal_exec(params)
            self.wi.setupUi(self.makerWindow)
        else:
            self.wi = Ui_minimal_exec_deps(params)
            self.wi.setupUi(self.makerWindow)

        self.obj.hide()
        self.makerWindow.show()
        pass

    def browse(self):
        file = str(
            QtWidgets.QFileDialog.getExistingDirectory(
                self.obj, "Select Project Directory"))
        self.projdir.setText(file)
        pass

    pass


def main():
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QMainWindow()
    ui = Ui_startup()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
