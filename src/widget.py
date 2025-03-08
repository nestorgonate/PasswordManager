# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QMessageBox

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget
from passwordgenerate import generatePassword
from accountsfile import verify_accountfile
import json
class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.GenerarPasswordButton.clicked.connect(self.showPassword)
        self.ui.ShowPassword.setReadOnly(True)
        self.ui.AddAccount.clicked.connect(self.addAccount)
    def showPassword(self):
        password = generatePassword()
        self.ui.ShowPassword.setPlainText(password)
    def addAccount(self):
        if verify_accountfile():
            try:
                site_name = self.ui.SiteAccount.toPlainText().strip()
                email_account = self.ui.EmailAccount.toPlainText().strip()
                password_account = self.ui.PasswordAccount.toPlainText().strip()
                if not site_name and not email_account and not password_account:
                    self.show_message("Advertencia", "No se han ingresado datos")
                    return
                try:
                    with open("accounts.json", "r") as accountsfile:
                        file = json.load(accountsfile)
                        if not isinstance(file, list):
                            file = []
                        account_json = {"site": site_name,
                        "email": email_account,
                        "password": password_account
                        }
                        file.append(account_json)
                        with open("accounts.json", "w") as accountsfile:
                            json.dump(file, accountsfile, indent=4)
                    self.ui.SiteAccount.clear()
                    self.ui.EmailAccount.clear()
                    self.ui.PasswordAccount.clear()
                    self.show_message("Correcto", "Se ha agregado la cuenta al archivo accounts.json")
                except Exception as jsone:
                    pass
            except Exception as jsone:
                pass
    def show_message(self, titulo, mensaje):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(titulo)
        msg_box.setText(mensaje)
        msg_box.setIcon(QMessageBox.Information)
        msg_box.exec()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
