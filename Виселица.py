import random

def get_word():
    '''
    ?????????? ?????? ?????????? ???? ????? ? ??????:
    ????? - ????????? ???????? ????? ?? 1000 ????;
    ?????? - ??????? "_" ??????????? ?????? ????? ?????????? ?????. 
    '''
    words_list = ['???', '???????', '?????', '????', '?????', '????', '????', '??????', '?????', '?????', '??????', '????', '????', '??????', '????', '???????', '???', '??????', '???????', '??????', '???????', '???', '?????', '?????????', '?????', '?????', '???????', '????????', '?????', '???????', '??????', '??????', '?????', '???', '?????', '????', '???????', '????', '????', '?????', '???????????', '????????', '?????????', '?????', '???', '?????', '???????', '?????', '?????', '????????', '??????', '????', '???????', '???????', '?????', '????', '???', '??????', '???????', '??????', '???????????', '????', '????????', '?????', '???', '?????????', '?????', '????', '???????????', '????????', '????????', '??????', '????????', '????????', '????????????', '?????', '????', '??????', '????', '??????', '??????', '??????', '?????', '???????', '????', '?????????', '???', '??????', '?????', '?????', '?????', '?????????????', '?????', '???????????', '??????', '????', '?????', '????', '????', '?????', '?????????', '??????', '??????????', '?????', '????????', '????????????', '????????', '????', '????', '??????', '?????', '????', '????', '???????', '?????', '???', '??????', '?????????', '???????', '?????????', '???', '????', '??????????', '?????', '????', '?????', '?????', '????????', '???????', '???', '????', '??????', '????', '?????', '????', '??????', '?????', '????????', '??????', '???????', '????????', '????????', '??????', '?????', '?????', '????????', '??????', '????', '???????', '???????', '??????', '??????', '????', '????????', '????', '???', '?????', '????????', '?????', '????', '???????', '???????', '???????', '?????????', '??????????', '???????', '????????', '????????', '??????', '?????????', '???????', '??????', '???????????', '??????', '??????', '???', '????????????', '???????', '??????', '?????', '??????', '???', '?????', '????????', '?????', '????', '?????????????', '??????', '?????????????', '???', '????', '???????', '??????????', '????', '??????', '?????', '?????', '?????????', '????', '?????????', '?????', '???', '?????????', '???????????', '????????', '?????', '???????????', '???????', '?????', '???????', '???????', '?????????', '?????', '??????', '???????', '?????', '???????', '??????', '?????', '???????', '????', '?????????', '????', '????', '???????', '?????', '?????', '??????', '????', '??????', '??????????', '???', '???????', '????????????', '?????', '???', '??????', '??????', '??????', '????', '??????', '??????', '???????', '??????', '??????', '?????', '???????', '???????', '??????????', '????????', '?????', '??????', '?????????', '?????', '???????', '?????', '??????', '???????', '???????', '???????', '???????', '?????', '????????', '???????', '????', '??????', '???????', '??????????', '????????', '????', '?????????', '???????????', '??????', '??????????', '????????', '????????', '??????', '????', '????????????', '??????', '????????', '????', '??', '????', '????', '??????', '??????', '???????', '?????????????', '??????????', '????????????', '???', '????????', '??????', '???????', '??????', '?????', '?????', '?????', '??????', '???????', '????????????', '???????', '??????', '????', '???????????', '???????', '????', '?????', '?????', '???????', '????????', '??????', '?????????????', '???????', '???????', '????????', '????', '???????', '???????', '????????????', '????', '?????', '????', '?????????', '?????????', '???????', '???????', '??????????', '????????', '??????????', '?????', '????????', '??????', '?????', '?????????', '??????', '????', '????', '????', '?????', '?????', '???', '?????', '???', '??????????', '???????', '???', '??????????', '?????????????', '??????', '????', '??????', '??????', '???????', '??????', '????', '???', '???????', '???????', '????????', '???????', '???????', '??????????', '???', '?????', '????????', '????', '???????', '???????', '???????????', '?????', '???????????', '??????????????', '????????', '??????????', '????', '??????', '????', '??????????', '??????', '?????', '????', '????', '??????', '?????', '????????', '??????', '???????', '?????????', '???????????????', '??????', '????????', '?????', '???', '??????', '???????', '???????', '??????', '?????', '????????', '??????????', '????', '??????', '?????????', '???????????', '????', '???????', '?????', '???', '?????', '??????', '?????', '?????', '????????', '????', '?????????', '???????', '???????', '?????', '?????????', '????', '?????', '???????', '????', '???????????', '?????', '?????', '??????', '????????????', '??????', '????', '????????', '???????', '??????', '??', '?????', '?????????', '????', '???????', '???', '????', '????', '????????????', '?????', '????', '?????????', '????', '???????', '????', '?????', '??????', '?????', '???', '?????????', '????', '????????', '????????', '?????????????', '???????', '???????', '??????', '??????', '????', '??????', '?????', '????????', '?????????', '????????', '????????', '?????????', '???????', '??????', '?????', '?????', '?????????', '???????', '????', '???????????', '???????', '?????????', '??????????', '?????????', '?????????', '?????????', '??????????', '???????????', '????', '???????', '???????', '???????', '???????', '????????????', '?????????', '????', '?????????????', '???????', '??????', '???????????', '?????????', '?????', '????', '????????', '???????', '??????', '???', '????????', '????', '???????', '??????', '??????', '???????', '??????', '?????', '??????', '????????', '??????', '??????', '??????', '???????', '????', '???????', '????????', '????????', '????', '???????', '????????????????', '?????????????', '???????', '?????', '?????', '??????', '????????', '??????', '????????????', '???????????', '?????', '???????', '????????', '??????', '????????', '???????????', '????????', '????', '?????????', '?????', '??????', '????????', '??????', '??????', '?????', '??????', '?????????', '?????', '???????', '???????', '??????', '?????', '?????', '?????????', '???????', '????', '???????', '??????', '????', '???????', '???????', '??????', '????????', '?????', '????????', '?????????', '????', '??????', '???????', '????????????', '????', '??????', '?????', '????????', '?????', '??????????', '?????', '?????????', '?????', '???????', '????????????', '???????', '??????', '????', '????????', '??????????', '????????', '????????', '?????', '?????', '????', '??????', '?????', '?????', '?????????', '????', '??????????????', '?????', '?????', '?????????', '?????????', '???????', '?????????', '?????????', '?????', '????????', '???????', '????????', '???????????', '?????', '????????', '????', '?????', '??????', '???????????', '???????', '?????????????', '?????', '??????????', '???????', '??????????????', '???????????', '???', '?????', '?????????', '??????????', '???????', '?????', '??????', '????', '???', '????????', '??????', '??????????', '??????????', '?????', '??????????', '????', '??????????', '?????', '??????', '????', '????', '?????', '?????', '?????', '???????', '????????', '?????????', '??????', '???????????', '??????', '????????', '???????', '????', '???????', '??????', '????????', '????????', '????', '?????????', '??????????', '?????????', '???????????', '??????????', '??????', '????', '????????', '??????????', '????', '????????????', '??????????', '????', '???????????', '???', '????', '??????', '???????????', '????????', '??????????????', '?????', '????', '???', '??????????', '??????', '????????', '???????', '??????????', '???????', '?????????', '???????????', '????', '????????', '????', '????????', '??????????', '???????', '??????????', '??????', '??????????????', '??????', '?????', '???????', '????', '???????', '???????', '??????', '????????', '??????', '??????????', '??????', '????', '?????', '??????', '???????', '??????', '???????', '??????', '???????', '?????????', '?????', '?????', '????', '?????????', '??????????', '??????', '????????', '?????????', '????????', '???????????', '???????', '???????????', '?????', '???????', '????????????', '????????', '?????', '????', '???????', '????????', '?????', '??????', '????', '??????', '????????', '?????', '???????', '???', '???', '?????', '????????', '???', '????', '?????', '?????', '????????', '?????????', '??????', '?????????', '???????', '??????', '?????', '???????', '?????????', '??????', '??????????', '????????', '????????', '??????', '???????', '???????????', '?????????', '?????????', '???', '????????', '?????????', '?????', '?????', '??????', '?????????????', '????????', '???????', '???????????', '????????????', '????????', '?????', '?????????', '??????', '?????', '??????????????', '????', '?????????', '?????????', '???????', '????????', '??????????', '????', '??????', '??????', '????', '???????', '?????', '??????', '???', '????', '??????????', '????????', '???????', '?????', '???????????', '????????', '?????????', '??????????', '??????????', '???????????', '?????', '?????', '????????', '??????', '????', '?????', '????', '??????', '?????', '?????', '???????', '??????????', '?????????????', '??????', '????', '????', '??????', '????', '??????', '???????', '??????', '??????', '????', '????????', '??????', '?????????', '???????', '?????????', '???????????', '????', '????', '???????', '????????', '??????????', '?????', '?????', '??????', '??????', '????????', '??????', '?????', '???????????', '???????', '????', '?????', '????????', '?????', '????', '?????', '??????', '?????', '?????', '??????', '?????', '?????????', '???', '??????', '?????', '?????', '????????', '?????', '???', '?????????????', '???????', '????', '??????', '????', '?????', '?????', '??????', '??????', '?????????', '??????', '???????', '??????', '???', '?????', '???????', '???????', '??????????', '??????', '?????????????', '??????????', '?????', '???????????', '????', '??????', '?????????', '?????????', '??????', '????????', '????????', '????????', '????', '????????', '?????', '???????', '???????????', '?????', '????????????', '?????', '?????', '?????????', '??????', '???????', '???????????????', '?????????', '?????', '????????', '??????????', '????????', '????', '?????????', '????', '??????????', '?????', '???????????', '???????????', '??????', '??????', '???', '??????', '??????', '?????', '????????', '????????', '??????????', '???????', '???????', '???????????', '??????????', '?????', '?????', '???????', '???????', '???????', '?????', '??????', '?????????????', '?????', '?????????', '???????????', '????????', '???????????', '???????', '???', '????????', '????????????????', '???????', '?????????', '?????', '??????????', '??????????????', '??????????', '?????????????', '???????????', '???????', '??????', '??????', '???????', '????????', '???????', '??????', '???????', '????', '??????????', '?????????????', '????', '?????????', '???????', '????????', '?????????', '?????', '??????', '?????', '?????????', '????????????', '????', '??????????']
    word = random.choice(words_list).upper()
    return [word, ['_' for _, _ in enumerate(word)]]

def display_hangman(tries):
    stages = ['''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''', 
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''', 
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''', 
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''', 
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''', 
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''', 
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                ''', 
                '''
                   --------
                   |
                   |
                   |
                   |
                   |
                   -
                   ''', 
                '''
                   
                   |
                   |      
                   |    
                   |      
                   |     
                   -
                ''', 
                '''
                   
                   
                         
                       
                         
                        
                   -
                '''
    ]
    tries = tries if 0 <= tries <= 9 else 0 # ?????? ?? ??????
    print(stages[tries])

def statistics(word, tries):
    print()
    display_hangman(tries)
    print(*word[1])
    print(f'\n????? ????? {len(word[0])}, ?????????? ???? {sum([1 for i in word[1] if i.isalpha()])}.')
    print(f'???????: {tries}')

def input_answer(repiat_answer):
    while True:
        answer = input('??????? ???? ????? (????? ??? ?????):\n').strip().upper()
        if answer in repiat_answer:
            print('????? ?????? ??? ???. ?????????? ?????.')
        elif answer.isalpha():
            return answer

def check_answer(word, answer, tries, repiat_answer):
    if answer in word[0]:
        for char in answer:
            word[1] = [i if i == char else j for i, j in zip(word[0], word[1])]
        return (word, tries, repiat_answer)
    return (word, tries - 1, repiat_answer)

def get_answer(word, tries, repiat_answer):
    answer = input_answer(repiat_answer)
    repiat_answer.append(answer)
    return check_answer(word, answer, tries, repiat_answer)

def play(word):
    tries = 9
    repiat_answer = list()
    print('??????? ?????? ? ???????? ????!')
    while tries >= 0:
        statistics(word, tries)
        if not tries or not any([i == '_' for i in word[1]]): break
        word, tries, repiat_answer = get_answer(word, tries, repiat_answer)
    print('???. ??? ??????.' if tries else f'????? ??????? ?????.\n?????????? ????? {word[0]}.')
    print('??????? ????')
    answer()
        
def answer():
    text = input()
    if text.lower() in ('?', '??', 'yes', 'y'):
        play(get_word())
    elif text.lower() in ('n', '???', 'no', '?'):
        print("????? ???? :'(")  
    else:
        print("?????? ?? ?????, ???????, ??????????)")
        answer()

play(get_word())
        
        