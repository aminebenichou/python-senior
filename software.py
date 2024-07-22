from PyQt5 import QtWidgets
from functools import partial
from db import insertItem, edit_row, retrieve_items, delete_row

class MainWindow(QtWidgets.QWidget):
    def __init__ (self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Todo List Software")
        # first method to display a button
        self.button = QtWidgets.QPushButton("Add", self)
        self.button.clicked.connect(self.createTodoItem)
        # self.edit_btn.clicked.connect(self.editTodoItem)
        # to specify the dimensions other than the default
        # self.button.setGeometry(200, 200, 100, 100)
        # creating text field
        self.text_field = QtWidgets.QLineEdit()
        # second method to diplay a button
        self.main_layout = QtWidgets.QHBoxLayout(self)
        self.left_layout = QtWidgets.QVBoxLayout(self)
        self.right_layout = QtWidgets.QVBoxLayout(self)
        self.main_layout.addLayout(self.left_layout)
        self.main_layout.addLayout(self.right_layout)


        self.left_layout.addWidget(self.text_field)
        self.left_layout.addWidget(self.button)
        self.displayItems()

    def createTodoItem(self):
        print(self.text_field.text())
        insertItem(self.text_field.text())
        self.refresh()

    def refresh(self):
        for i in reversed(range(self.right_layout.count())): 
            self.right_layout.itemAt(i).widget().deleteLater()

        self.displayItems()

    def editTodoItem(self, item):
        
        edit_row(item, {"title": self.text_field.text()})        
        self.refresh()
    
    def deleteItem(self, item):
        delete_row(item)
        self.refresh()
    
    def displayItems(self):
        items = retrieve_items()
    
        for item in items :
            
            self.item_title = QtWidgets.QLabel(item[1])
            self.edit_btn = QtWidgets.QPushButton("Edit", self)
            self.delete_btn = QtWidgets.QPushButton("Delete", self)
            self.edit_btn.clicked.connect(partial(self.editTodoItem, item[0]))
            self.delete_btn.clicked.connect(partial(self.deleteItem, item[0]))
            self.right_layout.addWidget(self.item_title)
            self.right_layout.addWidget(self.edit_btn)
            self.right_layout.addWidget(self.delete_btn)


app = QtWidgets.QApplication([])

window = MainWindow()
window.resize(500,500)
window.move(100,100)
window.show()

app.exec_()