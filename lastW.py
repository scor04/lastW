# напиши здесь код третьего экрана приложения
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

class ThirdW(QWidget):
    def __init__(self, info):
        super().__init__()
        self.info = info
        self.setWindowTitle("Результат")
        self.resize(900, 700)

        self.index = (4*(self.info.P1 + self.info.P2 + self.info.P3) - 200) / 10

        self.text = 'Индекс Руфьё: ' + str(self.index)
        self.label1 = QLabel(self.text)

        self.f1 = "Работоспособность сердца: " + self.interpretation()
        self.label2 = QLabel(self.f1)


        self.v_line = QVBoxLayout()
        self.v_line.addWidget(self.label1,alignment = Qt.AlignCenter)
        self.v_line.addWidget(self.label2,alignment = Qt.AlignCenter)
        self.setLayout(self.v_line)

        self.show()
    
    def interpretation(self):
        if self.info.age >= 15:
            if self.index >= 15:
                return "Низкий"
            elif self.index >= 11 and self.index <= 14.9:
                return "Удовлетворительный"
            elif self.index >= 6 and self.index <= 10.9:
                return "Средний"
            elif self.index >= 0.5 and self.index <= 5.9:
                return "Выше среднего"
            elif self.index >= 0.4:
                return "Высокий"

        elif self.info.age >= 13 and self.info.age <= 14:
            if self.index >= 16.5:
                return 'Низкий'
            elif self.index >= 12.5 and self.index <= 16.4:
                return "Удовлетворительный"
            elif self.index >= 7.5 and self.index <= 12.4:
                return "Средний"
            elif self.index >= 2 and self.index <= 7.4:
                return "Выше среднего"
            elif self.index >= 1.9:
                return "Высокий"

        elif self.info.age >= 11 and self.info.age <= 12:
            if self.index >= 18:
                return 'Низкий'
            elif self.index >= 14 and self.index <= 17.9:
                return "Удовлетворительный"
            elif self.index >= 9 and self.index <= 13.9:
                return "Средний"
            elif self.index >= 3.5 and self.index <= 8.9:
                return "Выше среднего"
            elif self.index >= 3.4:
                return "Высокий"

        elif self.info.age >= 9 and self.info.age <= 10:
            if self.index >= 19.5:
                return 'Низкий'
            elif self.index >= 15.5 and self.index <= 19.4:
                return "Удовлетворительный"
            elif self.index >= 10.5 and self.index <= 15.4:
                return "Средний"
            elif self.index >= 5 and self.index <= 10.4:
                return "Выше среднего"
            elif self.index >= 4.9:
                return "Высокий"

        elif self.info.age >= 7 and self.info.age <= 8:
            if self.index >= 21:
                return 'Низкий'
            elif self.index >= 17 and self.index <= 20.9:
                return "Удовлетворительный"
            elif self.index >= 12 and self.index <= 16.9:
                return "Средний"
            elif self.index >= 6.5 and self.index <= 11.9:
                return "Выше среднего"
            elif self.index >= 6.4:
                return "Высокий"


class ppp():
    def __init__(self, name, age, P1, P2, P3):
        self.name = name
        self.age = age
        self.P1 = P1
        self.P2 = P2
        self.P3 = P3
