from random import *
questions = ['������ ��������� ������������', '�������� ���� ��� �������� ������', '���������', '�������� ������ ��������� ����� �����������', '��� ������������ �� ������� ���������']
answers = ['����������', '��������', '��������', '����������', '����������']

def question():
    probe = []
    n = 5
    num = randint(0, len(questions) - 1)
    word = answers[num]
    len_word = len(answers[num])
    print('����, ������:', questions[num])
    view_word = ['_' for i in range(len_word)]
    print(*view_word)
    print('���������� ���� � �����:', len_word)
    print('��� �����!')
    while n > 0: 
        x = input().lower()
        if x == word:
            print(word)
            print('� ��� ���������� �����!')
            break
        elif x in probe:
            print('�� ��� ��� ���������, ����� ������ �������.')
        elif x.isalpha() and (len(x) == 1 or len(x) == len_word):
            probe.append(x)
            if len(x) == 1:
                if x in word:
                    print('����� ����� ���� � �����!')
                    for i in range(len_word):
                        if word[i] == x:
                            view_word[i] = x
                    if '_' in view_word:
                        print(*view_word)
                    else:
                        print(*view_word)
                        print('�� ������� �� �����!')
                        break
                else:
                    n -= 1
                    print('����� ����� ��� � �����\n�������� ������.\n������� ��������:', n)
                    print(*view_word)
            else:
                n -= 1
                print('��� ������������ �����\n�������� ������ ����� ��� �����!\n������� ��������:', n)
                print(*view_word)
        else:
            print('��� ��� �����? �������� ����� ��� ����� �������')
            print(*view_word)
            
    if n == 0:
        print('������� �����������... ���������� ����� - ', word)
        print('�� ����� ����������� ������ � ��������� ���!\n������� ���?')
        play_or_not()
    else:
        print('������� ���?')
        play_or_not()
        
def play_or_not():
    text = input()
    if text.lower() in ('�', '��', 'yes', 'y'):
        question()
    elif text.lower() in ('n', '���', 'no', '�'):
        print("����� ���� :'(")  
    else:
        print("������ �� �����, �������, ����������)")
        play_or_not()        

print('����� ���������� �� �������-��� "���� �����!"')
print('�� ������ ��������� ����� 5 ��� �� �����.\n�� ������ ������� ��� �����, ��� � ����� �������.\n�������!')
question()

