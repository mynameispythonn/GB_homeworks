


# ПРИМЕЧАНИЯ К РАБОТЕ:
# практически во всех заданиях я решаю без проверок (try\except)


# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.


import os


ex_1 = open("txt_1.txt", "w", encoding="utf-8")
while True:
    line = input()
    break if len(line) <= 1 else ex_1.write(f"{line}\n")
ex_1.close()
os.remove("txt_1.txt")

# or

with open("txt_1.txt", "w+", encoding="utf-8") as ex_1:
    while True:
        line = input()
        break if len(line) <= 1 else print(f"{line}", file=ex_1)
    ex_1.seek(0)
    print(ex_1.read())
os.remove("txt_1.txt")


# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

ex_2 = open("txt_2.txt", "r", encoding="utf_8")
n = 0
for i in ex_2:
    n += 1
    m = 0
    for j in i:
        m += 1
    print(f"{n} line has {m} characters")
print(f"This file has {n} strings")
ex_2.close()

# or

ex_2 = open("txt_2.txt", "r", encoding="utf_8")
print("\n".join([f"{index} line has {len(value.split())} words" for index, value in enumerate(ex_2.readlines(), 1)]))
ex_2.close()


# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет
# средней величины дохода сотрудников.


try:
    ex_3 = open("txt_3.txt", "r", encoding="utf-8")
    lst_s = []
    lst_z = []
    for i in ex_3:
        line = i.split(" ")
        lst_z.append(float(line[1]))
        if float(line[1]) < 20000.0:
            lst_s.append(line[0])
    print("\n".join(lst_s), sum(lst_z) / len(lst_z), sep="\n")
    ex_3.close()

except IOError:
    print("IOError!", "Try again", sep="\n")

# or

ex_3 = open("txt_3.txt", "r", encoding="utf-8")
lst_s = [value.split(" ")[0] for value in ex_3 if float(value.split(" ")[1]) < 20000.0] # здесь я не смогла понять, как
# за один присест и [0] и [1] сразу раскидать на два списка сразу
print("\n".join(lst_s))
ex_3.close()

# or

ex_3 = open("txt_3.txt", "r", encoding="utf-8")
workers = {}
for value in ex_3:
    workers[value.split()[0]] = float(value.split()[1])
print("\n".join(worker for worker, salary in workers.items() if salary < 20000.0),
      sum(workers.values()) / len(workers), sep="\n")
ex_3.close()

# здесь тоже хотела сократить, но не поняла как еще это сделать


# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться
# в новый текстовый файл.


try:
    with open("txt_4.txt", "r", encoding="utf-8") as ex_4:
        dict_nums = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре", "Five": "Пять",
                     "Six": "Шесть", "Seven": "Семь", "Eight": "Восемь", "Nine": "Девять", "Ten": "Десять"}
        with open("txt_41.txt", "w", encoding="utf-8") as ex_41:
            for i in ex_4:
                i = i.split(" ")
                if i[0] in dict_nums:
                    ex_41.write(f"{dict_nums[i[0]]} {i[1]} {i[2]}\n")
        with open("txt_41.txt", "r", encoding="utf-8") as ex_41:
            print(ex_41.read())
except KeyError:
    print("KeyError!", "Try again", sep="\n")
except IOError:
    print("IOError!", "Try again", sep="\n")


# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


try:
    with open("txt_5.txt", "x", encoding="utf-8") as ex_5:
        nums = ex_5.write(" ".join((str(i) for i in range(35))))
    print(sum(i for i in range(67)))
except FileExistsError:
    print("FileExistsError!", "Try again", sep="\n")
except IOError:
    print("IOError!", "Try again", sep="\n")
os.remove("txt_5.txt")


# # or

from random import randint

try:
    with open("txt_51.txt", "w+", encoding="utf-8") as ex_51:
        m = " ".join([str(randint(1, 567890)) for _ in range(7)])
        print(f"{m}\n", file=ex_51)
        ex_51.seek(0)
        print(sum(map(int, ex_51.readline().split())))
except TypeError:
    print("TypeError!", "Try again", sep="\n")
os.remove("txt_51.txt")

# здесь я не поняла, почему при использовании join список со строчными значениями переводит их в число - перепробовала
# кучу вариантов, но подходит только этот


## 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета
# не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий
# по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —

# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}


import re

with open("txt_6.txt", "r", encoding="utf-8") as ex_6:
    dct_6 = {"".join(re.findall(r'^\w+', i)): sum(int(j) for j in re.findall(r'\w+', i) if j.isdigit()) for i in ex_6}
    print(dct_6)


# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
# форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
# убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

# Подсказка: использовать менеджеры контекста.


with open("txt_7.txt", "r", encoding="utf-8") as ex_7:
    dct_71 = {i.split()[0]: (int(i.split()[3]) - int(i.split()[1])) for i in ex_7}
with open("txt_7.txt", "r", encoding="utf-8") as ex_7:
    for i in ex_7:
        dct_72 = {"average_profit": (sum(int(i.split()[3]) for i in ex_7) / len(i.split()))}
    lst_7 = [dct_71, dct_72]
    print(lst_7)