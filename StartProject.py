#подключение модулей и виджетов
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QLabel, QLineEdit, QVBoxLayout
#объявление констант
win_width, win_height = 800, 300
win_x, win_y = 200, 200
txt_title = "Отправка текста"
txt_send = "Отправить"
txt_line = "Поле ввода"

class FirstWindow(QWidget):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        #вызов конструктора родительского класса
        super().__init__(parent=parent, flags=flags)

        # создаём и настраиваем графические элементы:
        self.initUI()

        #устанавливает связи между элементами
        self.connects()

        #устанавливает, как будет выглядеть окно (надпись, размер, место)
        self.set_appear()

        # старт:
        self.show()
    def initUI(self):
        ''' создает графические элементы '''
        self.desc = QLabel("Добро пожаловать в программу которая скажет, нужно ли вам худеть. Ниже введите ваши данные:")
        self.rost = QLineEdit("Рост")
        self.ves = QLineEdit("Вес")
        self.button = QPushButton("Проверить")
        self.result = QLabel() #Текст для результата 

        self.layout_line = QVBoxLayout()
        
        self.layout_line.addWidget(self.desc, alignment = Qt.AlignCenter) 
        self.layout_line.addWidget(self.rost, alignment = Qt.AlignCenter) 
        self.layout_line.addWidget(self.ves, alignment = Qt.AlignCenter) 
        self.layout_line.addWidget(self.button, alignment = Qt.AlignCenter) 
        self.layout_line.addWidget(self.result, alignment = Qt.AlignCenter) 

        self.setLayout(self.layout_line) 
    def next_click(self):
        rost = int( self.rost.text() )
        ves = int( self.ves.text() )
        if (rost - ves) > 100:
            self.result.setText("Всё хорошо!")
        else:
            self.result.setText("Вам бы сбросить " + str(100 - (rost - ves)))
    def connects(self):
        self.button.clicked.connect(self.next_click)
        
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

def main():
    app = QApplication([])
    mw = FirstWindow()
    app.exec_()

main()












