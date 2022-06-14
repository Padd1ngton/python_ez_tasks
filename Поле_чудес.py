from random import *
questions = ['Боязнь открытого пространства', 'Защитная речь или защитное письмо', 'Отшельник', 'Немецкий наёмный пехотинец эпохи Возрождения', 'Меч ландскнехтов на двойном жаловании']
answers = ['агорафобия', 'апология', 'анахорет', 'ландскнехт', 'цвайхандер']

def question():
    probe = []
    n = 5
    num = randint(0, len(questions) - 1)
    word = answers[num]
    len_word = len(answers[num])
    print('Итак, вопрос:', questions[num])
    view_word = ['_' for i in range(len_word)]
    print(*view_word)
    print('Количество букв в слове:', len_word)
    print('Вам слово!')
    while n > 0: 
        x = input().lower()
        if x == word:
            print(word)
            print('И это правильный ответ!')
            break
        elif x in probe:
            print('Вы это уже пробовали, нужен другой вариант.')
        elif x.isalpha() and (len(x) == 1 or len(x) == len_word):
            probe.append(x)
            if len(x) == 1:
                if x in word:
                    print('Такая буква есть в слове!')
                    for i in range(len_word):
                        if word[i] == x:
                            view_word[i] = x
                    if '_' in view_word:
                        print(*view_word)
                    else:
                        print(*view_word)
                        print('Вы угадали всё слово!')
                        break
                else:
                    n -= 1
                    print('Такой буквы нет в слове\nНазовите другую.\nПопыток осталось:', n)
                    print(*view_word)
            else:
                n -= 1
                print('Это неправильное слово\nНазовите другое слово или букву!\nПопыток осталось:', n)
                print(*view_word)
        else:
            print('Что это такое? Назовите букву или слово целиком')
            print(*view_word)
            
    if n == 0:
        print('Попытки закончились... Правильный ответ - ', word)
        print('Не стоит отчаиваться Повезёт в следующий раз!\nСыграем ещё?')
        play_or_not()
    else:
        print('Сыграем ещё?')
        play_or_not()
        
def play_or_not():
    text = input()
    if text.lower() in ('д', 'да', 'yes', 'y'):
        question()
    elif text.lower() in ('n', 'нет', 'no', 'н'):
        print("Очень жаль :'(")  
    else:
        print("Ничего не понял, повтори, пожалуйста)")
        play_or_not()        

print('Добро пожаловать на капитОН-шоу "Поле Чудес!"')
print('Вы можете ошибиться всего 5 раз за раунд.\nВы можете назвать как букву, так и слово целиком.\nПоехали!')
question()

