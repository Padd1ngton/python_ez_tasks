from random import *
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

def is_valid_int():
    flag = False
    while flag == False:   
        x = input()
        if x.isdigit() and int(x) > 0:
            flag = True
            return int(x)
        else:
            print('Значение должно быть числом (именно числом) и больше нуля! Попробуйте ещё.')
        
def is_valid_answer():
    flag = False
    while flag == False:   
        x = input()
        if x.lower() in ('д', 'да', 'yes', 'y', 'n', 'нет', 'no', 'н'):
            flag = True
            return x
        else:
            print('Некорректное значение. Да или нет? yes or no?')
            
def generate_password(length, chars):
    password = ''
    for _ in range(length):
        password += choice(chars)
    print('Держите свой пароль:', password, sep = '\n')
    

print('Сколько паролей необходимо для генерации?')
num = is_valid_int()

print('Какой длины должны быть пароли?')
length = is_valid_int()

print('Включать ли цифры 0123456789?')
if is_valid_answer().lower() in ('д', 'да', 'yes', 'y'):
    chars += digits

print('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?')
if is_valid_answer().lower() in ('д', 'да', 'yes', 'y'):
    chars += uppercase_letters

print('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?')
if is_valid_answer().lower() in ('д', 'да', 'yes', 'y'):
    chars += lowercase_letters
    
print('Включать ли символы !#$%&*+-=?@^_?')
if is_valid_answer().lower() in ('д', 'да', 'yes', 'y'):
    chars += punctuation
    
print('Исключать ли неоднозначные символы il1Lo0O?')
if is_valid_answer().lower() in ('д', 'да', 'yes', 'y'):
    for i in 'il1Lo0O':
        chars = chars.replace(i, '')

for j in range(num):
    generate_password(length, chars)
