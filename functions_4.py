# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
# необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных
# значений необходимо запускать скрипт с параметрами.


from sys import argv


def salary_1():
    name, hours, rate, bonus = argv
    return f'Your salary is {int(hours) * int(rate) + int(bonus)}'
print(salary_1())

# or

def salary():
    hours = int(input("Enter your working hours: "))
    rate = int(input("Enter your rate: "))
    bonus = int(input("Enter your bonus: "))
    return hours * rate + bonus


# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего
# элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].


def new_lst():
    lst_1 = (input('Enter numbers separated by a space: ')).split()
    new_lst = [int(lst_1[i]) for i in range(1, len(lst_1)) if int(lst_1[i - 1]) < int(lst_1[i])]
    return new_lst


# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.


def new_lst_1():
    lst_2 = [i for i in range(20, 240)]
    new_lst_1 = [el for el in lst_2 if el % 20 == 0 or el % 21 == 0]
    return new_lst_1


# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел,
# соответствующих требованию. Элементы вывести в порядке их следования в исходном списке. Для выполнения задания
# обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]


def new_lst_2():
    lst_3 = (input('Enter numbers separated by a space: ')).split()
    new_lst_2 = [int(i) for i in lst_3 if lst_3.count(i) <= 1]
    return new_lst_2

# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления
# произведения всех элементов списка.
# Подсказка: использовать функцию reduce().


def new_lst_3(el_1, el_2):
    return el_1 * el_2


# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен
# быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. Во втором
# также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.


def nums():

    a = int(input("Enter first num: "))
    lst = []
    for i in count(a):
        if i > 1000:
            break
        lst.append(i)
        print(i)

## or

def nums_2():

    a = int(input("Enter first num: "))
    for i in islice(count(a), 30):
        print(i)

def nums_1():

    a = int(input("Enter first num: "))
    lst = []
    for i in count(a):
        if i > 1000:
            break
        lst.append(i)
    n = len(lst)
    for i in cycle(lst):
        n -= 1
        if n == 0:
            break
        print(i)

## or

def nums_3(first, last, rep):
    try:
        first, last, rep = int(input("Enter first num: ")), int(input("Enter last num: ")), int(input("Enter repeat num: "))
        lst = [i for i in islice(count(), first, last + 1)]
        lst_1 = iter(i for i in cycle(lst))
        rep_lst = [next(lst_1) for _ in range(rep)]
        print(lst)
        return rep_lst
    except ValueError:
        return "ValueError"
    except TypeError:
        return "TypeError"


# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове
# функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная
# с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.


from math import factorial


def gen_():
    n = int(input("Введите число: "))
    for el in range(1, n + 1):
        yield factorial(el)
for i in gen_():
    print(i)

## or

def gen_1(num):
    fact_num = 1
    if fact_num == 0:
        yield f'{num}! = 1'
    for i in range(1, num + 1):
        fact_num *= 1
        yield f'{i}! = {fact_num}'

for el in fact(int(input("Enter number: "))):
    print(el)
