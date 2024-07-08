from PyQt5 import QtWidgets

class MainWindow(QtWidgets.QWidget):
    def __init__ (self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Todo List Software")
        # first method to display a button
        self.button = QtWidgets.QPushButton("Print message", self)
        # to specify the dimensions other than the default
        # self.button.setGeometry(200, 200, 100, 100)

        # creating text field
        self.text_field = QtWidgets.QLineEdit()
        # second method to diplay a button
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.main_layout.addWidget(self.text_field)
        self.main_layout.addWidget(self.button)
        


app = QtWidgets.QApplication([])

window = MainWindow()
window.resize(500,500)
window.move(100,100)
window.show()

app.exec_()