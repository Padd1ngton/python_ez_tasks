eng_lower_alphabet = [chr(i) for i in range(97, 123)]
eng_upper_alphabet = [chr(i) for i in range(65, 91)]
rus_lower_alphabet = [chr(i) for i in range(1072, 1104)]
rus_upper_alphabet = [chr(i) for i in range(1040, 1072)]


def shifr():
    print('Введите текст для работы...')
    s = input()
    print('Введите шаг сдвига')
    step = is_valid_digit()
    final = ''
    for i in range(len(s)): 
        if s[i] in eng_lower_alphabet:
            if (ord(s[i]) + step) < 123:
                final += chr(ord(s[i]) + step)
            else:
                final += chr(96 + ((ord(s[i]) + step) - 122))        
        elif s[i] in eng_upper_alphabet:
            if (ord(s[i]) + step) < 91:
                final += chr(ord(s[i]) + step)
            else:
                final +=chr(64 + ((ord(s[i]) + step) - 90))            
        elif s[i] in rus_lower_alphabet:
            if (ord(s[i]) + step) < 1104:
                final += chr(ord(s[i]) + step)
            else:
                final += chr(1071 + ((ord(s[i]) + step) - 1103))              
        elif s[i] in rus_upper_alphabet:
            if (ord(s[i]) + step) < 1072:
                final += chr(ord(s[i]) + step)
            else:
                final += chr(1040 + ((ord(s[i]) + step) - 1071))                
        else:
             final += s[i]  
    print('Держи готовый вариант следующей строкой', final, sep = '\n')
    
def deshifr():
    print('Введите текст для работы...')
    s = input()
    print('Введите шаг сдвига')
    step = is_valid_digit()
    final = ''
    for i in range(len(s)): 
        if s[i] in eng_lower_alphabet:
            if (ord(s[i]) - step) >= 97:
                final += chr(ord(s[i]) - step)
            else:
                final += chr(123 - (97 - (ord(s[i]) - step)))             
        elif s[i] in eng_upper_alphabet:
            if (ord(s[i]) - step) >= 65:
                final += chr(ord(s[i]) - step)
            else:
                final += chr(91 - (65 - (ord(s[i]) - step)))            
        elif s[i] in rus_lower_alphabet:
            if (ord(s[i]) - step) >= 1072:
                final += chr(ord(s[i]) - step)
            else:
                final += chr(1104 - (1072 - (ord(s[i]) - step)))              
        elif s[i] in rus_upper_alphabet:
            if (ord(s[i]) - step) >= 1040:
                final += chr(ord(s[i]) - step)
            else:
                final += chr(1072 - (1040 - (ord(s[i]) - step)))               
        else:
             final += s[i]  
    print('Держи готовый вариант следующей строкой', final, sep = '\n')   
    

def is_valid_digit():
    flag = False
    while flag == False:   
        x = input()
        if x.isdigit() and int(x) > 0:
            flag = True
            return int(x)
        else:
            print('Значение должно быть числом (именно число) и больше нуля! Попробуйте ещё.')
    
def is_valid():
    x = int(input())
    if x == 1:
        shifr()
    elif x == 2:
        deshifr()
    else:
        print('А ты у мамы одарённый. 1 - для шифрования, 2 - для дешифрования. Выбери из этих двух вариантов.')
        is_valid()

print('Приветствую, на связи Цезарь! Будем шифровать или дешифровывать? Просто выберите между 1 и 2 соответственно ;)')
is_valid()