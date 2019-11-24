import design
import sys
from PyQt5 import QtWidgets

class ExampleApp(QtWidgets.QMainWindow, design.Ui_prob):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.action = QtWidgets.QAction("Открыть файл")
        self.menu.addAction(self.action)
        self.action.triggered.connect(self.file_open)
        self.action2 = QtWidgets.QAction("Сохранить файл")
        self.menu.addAction(self.action2)
        self.action2.triggered.connect(self.file_save)
        self.text = ""

    def file_open(self):
        file = QtWidgets.QFileDialog.getOpenFileName(self,"Выберите файл",filter="*.txt")
        if file:
            self.text = open(file[0],encoding="utf-8")
            self.textEdit.setPlainText(self.text.read())
            self.text.close()
    
    def file_save(self):
        a = self.textEdit.toPlainText()
        file = QtWidgets.QFileDialog.getOpenFileName(self,"Выберите файл",filter="*.txt")
        if file:
            self.text = open(file[0],"w",encoding="utf-8")
            a=self.textEdit.toPlainText()
            self.text.write(a)
            self.textEdit.textChanged()
                
def quit(window):
    print("123")

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.aboutToQuit.connect(quit(window))
    app.exec_()  # и запускаем приложение
main()