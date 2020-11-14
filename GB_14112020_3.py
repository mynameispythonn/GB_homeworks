# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
# пользователя, предусмотреть обработку ситуации деления на ноль.

num_1, num_2 = int(input("Enter first num: ")), int(input("Enter second num: "))
print(num_1 / num_2) if not ZeroDivisionError else print("ZeroDivisionError. Please try again")


# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод
# данных о пользователе одной строкой.

name, sname, datebirth, city, email, phone = input("Enter name: "), input("Enter sname: "), \
                                             input("Enter datebirth: "), input("Enter city: "), \
                                             input("Enter email: "), input("Enter phone: ")

print(f'{name} {sname} {datebirth} {city} {email} {phone}')
# or
print(name, sname, datebirth, city, email, phone, sep=" ")


# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших
# двух аргументов.


def my_func():
    lst_1 = []
    for i in range(3):
        obj = int(input("Enter number: "))
        lst_1.append(obj)
    return min(lst_1) + max(lst_1)

print(my_func())

or

def my_func(arg_1, arg_2, arg_3):
    lst_1 = [arg_1, arg_2, arg_3]
    return min(lst_1) + max(lst_1)

print(my_func(int(input("Enter arg_1: ")), int(input("Enter arg_2: ")), int(input("Enter arg_3: "))))


# 4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
# возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания
# необходимо обойтись без встроенной функции возведения числа в степень.


def my_func(x, y):
    m = x
    while y > 1:
        x *= m
        y -= 1
    return x

print(my_func(int(input("Enter x ")), int(input("Enter y "))))

or

def my_func(x, y):
    return x ** y

print(my_func(int(input("Enter x ")), int(input("Enter y "))))


# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма
# чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных
# чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение
# программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих
# чисел к полученной ранее сумме и после этого завершить программу.


n = 0
while True:
    for i in map(str, input().split()):
        if i.isdigit() == True:
            n += int(i)
        else:
            print(n)
            quit()
    print(n)


# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной
# первой буквой. Например, print(int_func(‘text’)) -> Text.

# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит
# из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной
# буквы. Необходимо использовать написанную ранее функцию int_func().


def int_func(txt):
    return txt[0].upper() + txt[1:]
print(int_func("text"))

def int_func(txt):
    txt = txt.split()
    txt_1 = []
    for i in txt:
        txt_1.append(i[0].upper() + i[1:])
    return ' '.join(txt_1)

print(int_func("text mext dext"))