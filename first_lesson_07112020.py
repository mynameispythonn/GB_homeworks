print('task_1')

name = 'simba'
print(type(name))
age = 12
print(type(age))
period = 1.33
print(type(period))
print(age + period)
print(age + period + 2)
print(age, name)
print(age, name, sep='_')
print(name, end=";")
print('kot')
age=int(input('How_old_are_you?:'))
period_1 = 20
print('After', period_1,'you will be', age+period_1)



print('task_2')

n = input('Введите число от 1 до 9: ')
nn = n + n
nnn = n + n + n
number = int(n) + int(nn) + int(nnn)
print(number)



print('task_3')

n = int(input('Введите желаемое время в секундах: '))
hour = n // 3600
minute = n//60 - hour * 60
second = n - hour * 3600 - n * 60
print('Заданное Вами время в формате чч:мм:сс : {hour}:{minute}:{second}')



print('task_4')

n = int(input('Введите  целое положительное число : '))
m = n % 10
n = n // 10
while n > 0:
    if n % 10 > m:
        m = n % 10
    n = n // 10
print(f'Наибольшая используемая в числе цифра: {m}')



print('task_5')

revenue = int(input('Какова выручка компании за последний месяц? : '))
cost = int(input('Каковы издержки компании за последний месяц? : '))
print(f'выручка составила: {revenue}')
print(f'издержки составили: {cost}')
if revenue > cost :
    ratio_rc = revenue // cost
    print(f'Доходы Вашей фирмы в этом месяце привысили расходы и рентабельность фирмы на данный момент составляет : {ratio_rc} ')
if revenue < cost :
    print('К сожалению, Ваша компания под грозой')
human_resource = int(input('Каково количество сотрудников в Вашей фирме на данный момент? : '))
ratio_rh = revenue // human_resource
print(f'Таким образом, прибыль на одного человека в Вашей фирме составляет: {ratio_rh}')



print('task_6')
number = 0
a = int(input('Сколько км в день пробегает спортсмен? : '))
b = int(input('Сколько спортсмену нужно пробежать км всего? : '))
while a <= b:
    a = a + (a * 0.1)
    number = number + 1
if a > b:
    print(f'На {number} день спортсмен пробежит больше {b} км')