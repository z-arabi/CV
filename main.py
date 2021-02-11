import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow , QGroupBox

Form = uic.loadUiType(os.path.join(os.getcwd(),"Form.ui"))[0]

class IntroWindow(QMainWindow, Form):
    def __init__(self):
        super(IntroWindow,self).__init__()
        self.setupUi(self)
        # self.basicInformation.name.nameEdit.textEdited.connect(self.setName)
        self.name = self.testMain.text()
    def setName(self,name):
        self.name = name

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = IntroWindow()
    w.show()
    sys.exit(app.exec_()) 