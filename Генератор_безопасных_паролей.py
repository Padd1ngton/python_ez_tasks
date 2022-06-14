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
            print('�������� ������ ���� ������ (������ ������) � ������ ����! ���������� ���.')
        
def is_valid_answer():
    flag = False
    while flag == False:   
        x = input()
        if x.lower() in ('�', '��', 'yes', 'y', 'n', '���', 'no', '�'):
            flag = True
            return x
        else:
            print('������������ ��������. �� ��� ���? yes or no?')
            
def generate_password(length, chars):
    password = ''
    for _ in range(length):
        password += choice(chars)
    print('������� ���� ������:', password, sep = '\n')
    

print('������� ������� ���������� ��� ���������?')
num = is_valid_int()

print('����� ����� ������ ���� ������?')
length = is_valid_int()

print('�������� �� ����� 0123456789?')
if is_valid_answer().lower() in ('�', '��', 'yes', 'y'):
    chars += digits

print('�������� �� ��������� ����� ABCDEFGHIJKLMNOPQRSTUVWXYZ?')
if is_valid_answer().lower() in ('�', '��', 'yes', 'y'):
    chars += uppercase_letters

print('�������� �� �������� ����� abcdefghijklmnopqrstuvwxyz?')
if is_valid_answer().lower() in ('�', '��', 'yes', 'y'):
    chars += lowercase_letters
    
print('�������� �� ������� !#$%&*+-=?@^_?')
if is_valid_answer().lower() in ('�', '��', 'yes', 'y'):
    chars += punctuation
    
print('��������� �� ������������� ������� il1Lo0O?')
if is_valid_answer().lower() in ('�', '��', 'yes', 'y'):
    for i in 'il1Lo0O':
        chars = chars.replace(i, '')

for j in range(num):
    generate_password(length, chars)
