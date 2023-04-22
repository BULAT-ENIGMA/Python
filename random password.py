import random
from time import sleep
from string import *
d = digits
ll = ascii_lowercase
print(ll)
lu = ascii_uppercase
p = punctuation
ns = 'il1Lo0O'

chars = ''

n = int(input('Какое будет количество паролей? '))
le = int(input('Какая будет длинна одного пароля? '))
dot = input('включать ли цифры в пароль? д/н').lower()

if dot == 'д':
    chars += d

llot = input('включать ли маленькие буквы в пароль? д/н').lower()
if llot == 'д':
    chars += ll

luot = input('включать ли большие буквы в пароль? д/н').lower()
if luot == 'д':
    chars += lu

pot = input('включать ли нужные символы в пароль? д/н').lower()
if pot == 'д':
    chars += p

nsot = input('Исключать ли неоднозначные символы? д/н').lower()
if nsot == 'д':
    for i in range(len(ns)):
        chars = chars.replace(ns[i], '')





def generate_password(len, charse):
    y = []
    for i in range(n):
        e = random.sample(charse, len)
        e = ''.join(e)
        y.append(e)
    return y

g = generate_password(le, chars)

print(*g, sep='\n')
sleep(10)
