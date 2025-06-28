#в стиле акинатора да/нет 
import time 

def print_with_delay(text, delay = 0.1): #Функция при которой текст печатается с эффектом "печати по буквам"
    for char in text:
        print(char, end = '', flush = True)
        time.sleep(delay)
    print()

def guess_number():
    print('Хорошо, сейчас я угадаю....')

    chislo = input('Это число делится без остатка на 2? (Да/Нет):') 
    if chislo == 'Да':
        print('Я уже почти догадался!...')
        guess_mee_chet= ['2','4','6','8','10'] #логика поиска по списку четных чисел 
        (print_with_delay('Это число меньше 6? (Да/Нет):', delay = 0.2))
        chislo1 = input()
        if chislo1 == 'Да':
            del guess_mee_chet [-1] #Убрал ненужные варианты
            del guess_mee_chet [-1]
            del guess_mee_chet [-1]
            (print_with_delay('Это число в квадрате будет ровно 16? (Да/Нет):', delay = 0.2))
            chislo11 = input()
            if chislo11 == 'Нет':
                del guess_mee_chet[-1]
                print('Твое число:', ','.join(guess_mee_chet)) # число - 2
            elif chislo11 == 'Да':
              del guess_mee_chet[0]
              print('Твое число:', ','.join(guess_mee_chet)) #число 4
        elif chislo1 == 'Нет':
            del guess_mee_chet [0]
            del guess_mee_chet [0]
            (print_with_delay('Это число в квадрате будет ровно 100? (Да/Нет):', delay = 0.2))
            chislo12 = input()
            if chislo12 == 'Да':
                del guess_mee_chet[0]
                del guess_mee_chet[0]
                print('Твое число:', ','.join(guess_mee_chet)) # Число - 10
            if chislo12 == 'Нет':
                (print_with_delay('Это число в квадрате будет ровно 64? (Да/Нет):', delay = 0.2))
                chislo122 = input()
                if chislo122 == 'Да':
                    del guess_mee_chet [-1]
                    del guess_mee_chet [0]
                    print('Твое число:', ','.join(guess_mee_chet))# Число - 8 
                if chislo122 == 'Нет':
                    del guess_mee_chet [-1]
                    del guess_mee_chet [-1]
                    print('Твое число:', ','.join(guess_mee_chet))# Число - 6
    if chislo == 'Нет': #Если нечетное 
        print('Я уже почти догадался!...')
        guess_mee_nechet = ['1','3','5','7','9']
        (print_with_delay('Это число меньше 5? (Да/Нет):', delay = 0.2))
        necht = input()
        if necht == 'Да':
            del guess_mee_nechet [-1] #Убрал ненужные варианты
            del guess_mee_nechet [-1]
            del guess_mee_nechet [-1]
            (print_with_delay('Это число в квадрате будет ровно 9? (Да/Нет):', delay = 0.2))
            necht1 = input()
            if necht1 == 'Нет':
                del guess_mee_nechet[-1]
                print('Твое число:', ','.join(guess_mee_nechet)) # число - 1
            elif necht1 == 'Да':
              del guess_mee_nechet[0]
              print('Твое число:', ','.join(guess_mee_nechet)) #число 3
        elif necht == 'Нет':
            del guess_mee_nechet [0]
            del guess_mee_nechet [0] 
            (print_with_delay('Это число в квадрате будет ровно 81? (Да/Нет):', delay = 0.2))
            necht2 = input()
            if necht2 == 'Да':
                del guess_mee_nechet[0]
                del guess_mee_nechet[0]
                print('Твое число:', ','.join(guess_mee_nechet)) # Число - 9
            if necht2 == 'Нет':
                (print_with_delay('Это число в квадрате будет ровно 49? (Да/Нет):', delay = 0.2))
                necht3 = input()
                if necht3 == 'Да':
                    del guess_mee_nechet [-1]
                    del guess_mee_nechet [0]
                    print('Твое число:', ','.join(guess_mee_nechet))# Число - 7
                if necht3 == 'Нет':
                    del guess_mee_nechet [-1]
                    del guess_mee_nechet [-1]
                    print('Твое число:', ','.join(guess_mee_nechet))# Число - 5

print('Привет! хочешь я угадаю твое число?')
itog = (input('Напиши (Да/Нет):'))
print(itog)

if itog == 'Да':
    print('Отлично! Тогда, загадай число от 1 до 10')    
elif itog == 'Нет':
    print('До скорой встречи, как будет желание поиграть, просто скажи мне!')
    exit()
    
    
(print_with_delay('Загадал? (Да/Нет):', delay = 0.2))
contin = input()

if contin == 'Да':
    guess_number()
elif contin == 'Нет':
    print('Как будешь готов, напиши "Готов":')
    contin = input()
    if contin == 'Готов':
        guess_number()