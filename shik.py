import design
import sys
from PyQt5 import QtWidgets
class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
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
        self.pushButton.clicked.connect(self.shifr)
        self.pushButton_2.clicked.connect(self.deshifr)
        self.pushButton_3.clicked.connect(self.speshl)
        self.pushButton_4.clicked.connect(self.despeshl)
    def 
    def despeshl(self):
        a=self.textEdit.toPlainText()
        c="абвгдеёжзийклмнопрстуфхцчшщыъьэюя"
        n="abcdefghijklnopqrstuvwxyz12345678"
        d=""
        for i in a:
            if i in c:
                i=n[c.index(i)]
                d+=i
            elif i in n:
                i=c[n.index(i)]
                d+=i
        self.textEdit.setPlainText(d)
    def speshl(self):
        a=self.textEdit.toPlainText()
        c="абвгдеёжзийклмнопрстуфхцчшщыъьэюя"
        n="abcdefghijklnopqrstuvwxyz12345678"
        d=""
        for i in a:
            if i in c:
                i=n[c.index(i)]
                d+=i
            elif i in n:
                i=c[n.index(i)]
                d+=i
        self.textEdit.setPlainText(d)
    def deshifr(self):
        a=self.textEdit.toPlainText() 
        c="абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        n="abcdefghijklnopqrstuvwxyz"
        b = self.spinBox.value() % 33
        d=""
        for i in a:
            if i in c:
                i=c[c.index(i)-b]
                d+=i
            if i in n:
                i=n[n.index(i)-b]
                d+=i
        self.textEdit.setPlainText(d)
    def shifr(self):
        a=self.textEdit.toPlainText()
        c="абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        n="abcdefghijklnopqrstuvwxyz"
        b = self.spinBox.value() % 33
        d=""
        for i in a:
            if i in c:
                i=c[c.index(i)+b]
                d+=i
            elif i in n:
                i=n[n.index(i)+b]
                d+=i
        self.textEdit.setPlainText(d)
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
            self.text.close()
def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    #app.aboutToQuit.connect(quit(window))
    app.exec_()  # и запускаем приложение
main()