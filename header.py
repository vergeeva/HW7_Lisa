# Задание 1.
# 1. Опишите класс «Длина» для измерения расстояний.
# Данные класса: число километров и метров, натуральные числа.
# Конструктор класса: конструктор произвольной длины, умолчания = 0.
# 2. Определите метод приведения, если данные заданы некорректно,
# и методы ввода и вычисления длины в метрах.
# 3. Для вывода полной информации об объекте перегрузите __str__.
# 4. Напишите property для доступа к атрибутам объекта.
# 5. Объявите несколько объектов, найдите длину в метрах для каждого объекта.
class length:
    # def __check(self):
    #     return self.__km > 0 and 0 < self.__m < 1001

    def __check(self):
        if self.__km > 0 and self.__m > 1000:
            self.__km += self.__m // 1000
            self.__m -= self.__m // 1000 * 1000
            return 1
        else:
            return self.__km > 0 and 0 < self.__m < 1001

    def __init__(self, km=0, m=0):
        self.__km = km
        self.__m = m
        if self.__check() == 0:
            self.__km = 0
            self.__m = 0

    def input_class(self):
        self.__km = int(input("Введите количество километров: "))
        self.__m = int(input("Введите количество километров: "))
        if self.__check():
            self.__km = 0
            self.__m = 0

    def __str__(self):
        return f'расстояние: {self.__km} км {self.__m} м'

    def convert(self):
        return self.__km * 1000 + self.__m

    @property
    def km(self):
        return self.__km

    @km.setter
    def km(self, km):
        self.__km = km

    @property
    def m(self):
        return self.__m

    @m.setter
    def m(self, m):
        self.__m = m


# Задание 2.
# 1. Опишите класс «Расстояние», производный от длины,
# который позволит выводить расстояние, заданное длиной,
# в различных единицах измерения, например, в милях, в лигах, ярдах,
# футах и так далее. Данные класса, это признак, который определяет правило перевода.
# 2. Определите конструктор расстояния на основе конструктора суперкласса.
# 3. Для вывода полной информации об объекте перегрузите __str__.
# 4. Определите метод вычисления расстояния в указанной единице измерения.
# Определите метод вывода таблицы расстояний в различных единицах измерения.
# 5. Объявите несколько расстояний, выведите на экран значение
# расстояния в разных единицах
class distance(length):
    def __check(self):
        return self.__type == 0 or self.__type == 1 or self.__type == 2 or self.__type == 3

    def __convert(self):
        if self.__type == 0:
            return self.convert() * 0.000621
        elif self.__type == 1:
            return self.convert() * 39.3701
        elif self.__type == 2:
            return self.convert() * 1.09361
        elif self.__type == 3:
            return self.convert() * 3.28084

    def __init__(self, type=0, km=0, m=0):
        super().__init__(km, m)
        self.__type = type  # 0-миля; 1-дюйм; 2-ярд; 3-фут

    def __str__(self):
        return f'данные: правило перевода:{self.__type} {super().__str__()}'

    def make_table(self):
        print("_________________________________")
        print(f'|{self}\t|')
        print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")
        print(self)
        for i in range(0, 4):
            self.__type = i
            # print(f'|значение в метрах = {super().convert()}\t|')
            print(f'|тип правила = {i}\t\t\t\t|')
            print(f'Значение по правилу: {round(self.__convert(), 2)}\t|')
        print("|_______________________________|")
