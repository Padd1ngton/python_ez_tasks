from random import *
print('����� ���������� � �������� ��������')

def is_valid(s):
    return s.isdigit() and 1 <= int(s) <= game_limit

def start():
        global game_limit
        print('�� ������ ����� ����� ���������? ;)')
        x = input()
        if x.isdigit() and int(x) > 1:
            game_limit = int(x)
            print('�������� �������! �������!')
        else:
            print('�������� �����! �������� ����� (������ �����, ��-��!), ������ �������.')
            start()
            
def main_game():
    global n
    num = randint(1, game_limit)
    n = 0    
    flag = False
    while flag == False:
        s = input()
        if is_valid(s):
            if int(s) < num:
                n += 1
                print('���� ����� ������ �����������, ���������� ��� �����')
            elif int(s) > num:
                n += 1
                print('���� ����� ������ �����������, ���������� ��� �����')
            else:
                n += 1
                print('�� �������, �����������! ������� ������������:', n)
                print('�������, ��� ������ � �������� ��������.')
                flag = True
        else:
            print('� ����� ���� ���-���� ������ ����� ����� �� 1 �� 100?') 
            
            
def finish():
    print('������� ���? ��/���?')
    answer()
            
def answer():
    text = input()
    if text.lower() in ('�', '��', 'yes', 'y'):
        start()
        main_game()
        finish()
    elif text.lower() in ('n', '���', 'no', '�'):
        print("����� ���� :'(")  
    else:
        print("������ �� �����, �������, ����������)")
        answer()
    
        
start()
main_game()
finish()

    
    
    
