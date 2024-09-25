"""
6. Написать GUI приложение, которое представляет собой
библиотеку с поиском книг по автору и наименованию, добав-
лению новых книг и чтению книг в форматах epub, fb2 и pdf
"""

# т.к использование бд не обязательно, реализацию сделаю без нее
"""
т.к использование бд не обязательно, реализацию сделаю без нее
Так же обращаю внимание, что может работать не супер быстро,
но все работает, я загрузил большие книжки с картинками,
из-за чего могут быть зависания
"""
import sys
from PyQt6 import *
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import *
from ebooklib import epub, ITEM_DOCUMENT
import shutil
from bs4 import BeautifulSoup
from os import listdir
import PyPDF2
from lxml import etree

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Книжки")
        self.setFixedSize(QSize(800, 600))
        
        self.centralWidget = QWidget()
        

        self.combo_box_label = QLabel('найденные книги -', self.centralWidget)
        self.combo_box_label.setGeometry(420, 7, 100, 25)

        self.combo_box = QComboBox(self.centralWidget)
        self.combo_box.setGeometry(520, 10, 200, 25)
        
        self.openBookButton = QPushButton("Открыть", self.centralWidget)
        self.openBookButton.move(580, 50)
        self.openBookButton.clicked.connect(self.openBook)

        self.qtext = QTextEdit(self.centralWidget)
        self.qtext.setReadOnly(True)
        self.qtext.resize(600, 450)
        self.qtext.move(100, 100)

        self.uploadBookButton = QPushButton("Загрузить книгу", self.centralWidget)
        self.uploadBookButton.move(10, 10)
        self.uploadBookButton.clicked.connect(self.uploadBook)


        self.findBookByAuthorbutton = QPushButton("Найти книгу по автору", self.centralWidget)
        self.findBookByAuthorbutton.move(120, 10)
        self.findBookByAuthorbutton.clicked.connect(self.findBookByAuthor)

        self.findBookByNamebutton = QPushButton("Найти книгу по названию", self.centralWidget)
        self.findBookByNamebutton.move(265, 10)
        self.findBookByNamebutton.clicked.connect(self.findBookByName)

        self.setCentralWidget(self.centralWidget)
        
        
    def openBook(self):
        cur_book = self.combo_box.currentText()
        if '.epub' in cur_book:
            self.readEpub(cur_book)
        elif '.fb2' in cur_book:
            self.readfb2(cur_book)
        elif '.pdf' in cur_book:
            self.readPdf(cur_book)

    def findBookByAuthor(self):
        finded_books = []
        author, ok = QInputDialog.getText(self, 'Введите автора', 'Автор:')
        if ok and author:
            onlyfiles = listdir('9/books/')
            for i in onlyfiles:
                if author in i[0:i.index('-%%-')]:
                    finded_books.append(i)
        self.combo_box.clear()
        self.combo_box.addItems(finded_books)
        self.combo_box.setEditable(True)

    def findBookByName(self):
        finded_books = []
        bookName, ok = QInputDialog.getText(self, 'Введите название', 'название:')
        if ok and bookName:
            onlyfiles = listdir('9/books/')
            for i in onlyfiles:
                name = i[i.index('-%%-')+4:]
                name = name[0:name.index('.')]
                if bookName in name:
                    finded_books.append(i)
        self.combo_box.clear()
        self.combo_box.addItems(finded_books)
        self.combo_box.setEditable(True)

    def uploadBook(self):
        author, ok = QInputDialog.getText(self, 'Введите автора', 'Автор:')
        if ok and author:
            bookName, ok = QInputDialog.getText(self, 'Введите название', 'название:')
            if ok and bookName:
                fname = QFileDialog.getOpenFileName(self, 'Найти книгу', filter="*.epub *.fb2 *.pdf")[0]
                if fname:
                    try:
                        with open(f'9/books/{author}-%%-{bookName}.{fname.split('.')[-1]}', 'a', encoding='utf-8') as file:
                            pass
                        shutil.copyfile(fname, f'9/books/{author}-%%-{bookName}.{fname.split('.')[-1]}')
                    except Exception as e:
                        print(e)
                        return
                else:
                    return self.errorAlert()

    def errorAlert(self):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Ошибка")
        dlg.setText('ошибка загрузки файла, файл не передан или расширение не "epub, fb2 и pdf"')
        button = dlg.exec()

    def readfb2(self, file_path):
        with open('9/books/' + file_path, 'rb') as f:
            tree = etree.parse(f)
            
        root = tree.getroot()
        namespaces = {'fb2': 'http://www.gribuser.ru/xml/fictionbook/2.0'}
        body = root.xpath('//fb2:body', namespaces=namespaces)
        
        full_text = ""
        
        # Проходим по всем параграфам в <body> и извлекаем текст
        for section in body:
            paragraphs = section.xpath('.//fb2:p', namespaces=namespaces)
            for paragraph in paragraphs:
                full_text += paragraph.text or "" + "\n"
        
        self.qtext.setHtml(full_text)

    def readPdf(self, file_path):
        with open('9/books/' + file_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            full_text = ""
            
            # Проходим по всем страницам и извлекаем текст
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                full_text += page.extract_text() or ""
        
            # Устанавливаем текст в QTextEdit
            self.qtext.setHtml(full_text)

    def readEpub(self, file_path):
        book = epub.read_epub('9/books/' + file_path)
        
        # Инициализация переменной для хранения текста
        full_text = ""
        
        # Проход по всем документам в книге
        for item in book.get_items():
            if item.get_type() == ITEM_DOCUMENT:
                # Используем BeautifulSoup для извлечения текста из HTML
                soup = BeautifulSoup(item.content, 'html.parser')
                full_text += soup.get_text()

        # Устанавливаем текст в QTextEdit
        self.qtext.setHtml(full_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()