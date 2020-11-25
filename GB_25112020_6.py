# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
# (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный,
# желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.


# класс - это общий чертеж  и если атрибут есть в классе, то он для всех объектов, если атрибут у объекта - он
# для каждого элемента

from time import sleep

class TrafficLight:                # можно запускать без объекта с def

    def __init__(self, color):
        self.color = color


    def running(self, time):    # class method
        print(f"{self.color}")
        sleep({time})


color_1 = TrafficLight("красный")
color_2 = TrafficLight("желтый")
color_3 = TrafficLight("зеленый")
color_1.running()
sleep(7)
color_2.running()
sleep(2)
color_3.running()
sleep(4)
color_2.running()
sleep(2)
color_1.running()
sleep(7)

# or

from turtle import *

win = Screen()
win.setup(400, 600)

t = Turtle()


t.speed(0)
t.up()
t.goto(0, 87)
t.width(4)
t.color("black")
t.down()
t.circle(63)
t.up()
t.goto(0, -63)
t.width(4)
t.color("black")
t.down()
t.circle(63)
t.up()
t.goto(0, -213)
t.width(4)
t.color("black")
t.down()
t.circle(63)
t.up()

def traffic_lights(x, y, color):
    t.up()
    t.goto(x, y)
    t.color(color)
    t.down()
    t.begin_fill()
    t.circle(60)
    t.end_fill()
    t.up()


traffic_lights(0, 90, "red")
traffic_lights(0, 90, "white")
traffic_lights(0, -60, "yellow")
traffic_lights(0, -60, "white")
traffic_lights(0, -210, "green")
traffic_lights(0, -210, "white")
traffic_lights(0, -60, "yellow")
traffic_lights(0, -60, "white")
traffic_lights(0, 90, "red")
traffic_lights(0, 90, "white")



t.up()


win.listen()
win.mainloop()


# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width
# (ширина). Значения данных атрибутов должны передаваться при создании экземпляра
# класса. Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна. Использовать формулу:
# длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в
# 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т


class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        print(f"length = {length} m, width = {width} m")

    def mass(self):
        return f"{self._length} m * {self._width} * 25 kg * 5 sm = {self._length * self._width * 25 * 0.05} t"

r_1 = Road(34, 12)
r_2 = Road(80, 56)
print(r_1.mass())
print(r_2.mass())


# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name,
# surname, position (должность), income (доход). Последний атрибут должен быть
# защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
# дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов,
# вызвать методы экземпляров).


class Worker:
        def __init__(self, name, surname, position, wage, bonus):
            self.name = name
            self.surname = surname
            self.position = position
            self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return f"Full name: {self.name} {self.surname}"

    def get_total_income(self):
        return f"{self._income.get('wage') + self._income.get('bonus')}"


w_1 = Position("Sophy", "Turner", "Designer", 200, 500)
print(w_1.get_full_name())
print(w_1.get_total_income())


# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police
# (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс
# метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
# метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение
# о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


from random import choice

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        return f"{self.name} is started"
    def stop(self):
        return f"{self.name} is stopped"
    def turn(self):
        return f"{self.name} is turned {choice(['north', 'south', 'east', 'west', 'north-east', 'south-east', 'north-west', 'south-west'])}"
    def show_speed(self):
        print(f"Current {self.name} speed is {self.speed}")

class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Current {self.name} speed is {self.speed}")
        if self.speed > 60:
            return f'Speed of {self.name} is higher than allow for town car'
        else:
            return f'Speed of {self.name} is normal for town car'

class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Current {self.name} speed is {self.speed}")
        if self.speed > 40:
            return f'Speed of {self.name} is higher than allow for town car'
        else:
            return f'Speed of {self.name} is normal for town car'

class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


    def sport(self):
        if self.speed > 190:
            return f'{self.name} is sport car'
        else:
            return f'{self.name} is not sport car'

class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


    def police(self):
        if self.is_police:
            return f'{self.name} is police car'
        else:
            return f'{self.name} is not police car'

Chaika = SportCar(45, 'White', 'Chaika', False)
BMW = TownCar(160, 'Black', 'BMW x6', True)
Ferrari = WorkCar(2100, 'Red', 'FERRARI F8 SPIDER ', True)
Subaru = PoliceCar(110, 'Orange',  'Subaru', True)
print(Chaika.turn())
print(Ferrari.show_speed())
print(BMW.show_speed())
print(Subaru.police())



# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
# (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
# Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен
# выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def draw(self):
        print("Ручка")

class Pencil(Stationery):
    def draw(self):
        print("Карандаш")

class Handle(Stationery):
    def draw(self):
        print("Отрисовка")

pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
pen.draw()
pencil.draw()
handle.draw()