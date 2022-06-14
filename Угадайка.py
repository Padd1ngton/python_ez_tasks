from random import *
print('Добро пожаловать в числовую угадайку')

def is_valid(s):
    return s.isdigit() and 1 <= int(s) <= game_limit

def start():
        global game_limit
        print('До какого числа будем угадывать? ;)')
        x = input()
        if x.isdigit() and int(x) > 1:
            game_limit = int(x)
            print('Значение принято! Поехали!')
        else:
            print('Ошибочка вышла! Назовите число (именно число, да-да!), больше единицы.')
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
                print('Ваше число меньше загаданного, попробуйте еще разок')
            elif int(s) > num:
                n += 1
                print('Ваше число больше загаданного, попробуйте еще разок')
            else:
                n += 1
                print('Вы угадали, поздравляем! Попыток понадобилось:', n)
                print('Спасибо, что играли в числовую угадайку.')
                flag = True
        else:
            print('А может быть все-таки введем целое число от 1 до 100?') 
            
            
def finish():
    print('Сыграем ещё? Да/нет?')
    answer()
            
def answer():
    text = input()
    if text.lower() in ('д', 'да', 'yes', 'y'):
        start()
        main_game()
        finish()
    elif text.lower() in ('n', 'нет', 'no', 'н'):
        print("Очень жаль :'(")  
    else:
        print("Ничего не понял, повтори, пожалуйста)")
        answer()
    
        
start()
main_game()
finish()

    
    
    
