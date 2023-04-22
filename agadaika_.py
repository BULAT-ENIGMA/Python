import random
def is_valid(num):
    if num.isdigit() and 1 <= int(num) <= 100:
        return True
    else:
        return False
otv = 'да'
print('Добро пожаловать в угадайку. Вам нужно угадать число которое я загадал!)')
while otv == 'да':
    pr = int(input('Укажите максимальное значение числа, которое будем загадывать: '))
    count = 0
    r = random.randint(1, pr)

    while True:
        vd = input('Попробуйте угадать. Введите число: ')
        if is_valid(vd) == False:
            print('Введите нормально число')
            continue
        else:
            vd = int(vd)
            if vd < r:
                count += 1
                print('Число слишком маленькое')
            elif vd > r:
                count += 1
                print('Число слишком большое')
            elif vd == r:
                count += 1
                print('Поздравляю, это оно', 'число попыток равно', count)
                break

    otv = input('Хотите сыграть еще раз? да/нет')
    if otv == 'да':
        ovt = otv
    else:
        print('До скорой встречи!')



















