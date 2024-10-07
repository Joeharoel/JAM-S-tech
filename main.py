from PySide6.QtWidgets import QApplication
from frontPage import MyUserform
import sys

app = QApplication(sys.argv)

window = MyUserform()

window.show()
app.exec()