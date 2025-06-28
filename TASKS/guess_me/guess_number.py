#в стиле акинатора да/нет 
import time 

def print_with_delay(text, delay = 0.1): #Функция при которой текст печатается с эффектом "печати по буквам"
    for char in text:
        print(char, end = '', flush = True)
        time.sleep(delay)
    print()


def ask_question(question, delay = 0.2): # Задает вопрос пользователю и возвращает ответ
    print_with_delay(question, delay)
    return input().strip().capitalize()
    

def process_even_numbers(): #Обрабатывает логику для четных чисел 
    numbers = ['2', '4', '6', '8', '10']
    
    answer = ask_question('Это число меньше 6? (Да/Нет):')
    
    if answer == 'Да':
        numbers = numbers[:2] # Оставляем только 2 и 4 
        answer = ask_question ('Это число в квадрает будет ровно 16? (Да/Нет):')
        
        if answer == 'Нет':
            return numbers[0] # 2
        else:
            return numbers[1] # 4
    else:
        numbers = numbers[2:] # Оставляем 6,8,10
        answer = ask_question('Это число в квадрате будет ровно 100? (Да/Нет):')
        
        if answer == 'Да':
            return numbers[2] # 10
        else:
            answer = ask_question('Это число в квадрате будет ровно 64? (Да/Нет):')
            
            if answer == 'Да':
                return numbers[1] # 8
            else:
                return numbers[0] # 6
            
            
def process_odd_numbers(): # Обрабатывает логику для нечетных чисел 
    numbers = ['1', '3', '5', '7','9']
    
    answer = ask_question('Это число меньше 5? (Да/Нет):')
    
    if answer == 'Да':
        numbers = numbers[:2] # Оставляем только 1 и 3 
        answer = ask_question('Это число в квадрате будет ровно 9? (Да/Нет):')
        
        if answer == 'Нет':
            return numbers[0] # 1
        else:
            return numbers[1] # 3 
    else:
        numbers = numbers[2:] # Оставляем 5, 7, 9
        answer = ask_question('Это число в квадрате будет ровно 81? (Да/Нет):')
        
        if answer == 'Да':
            return numbers[2] # 9
        else:
            answer = ask_question('Это число в квадрате будет ровно 49? (Да/Нет):')
            
            if answer == 'Да':
                return numbers[1] # 7
            else:
                return numbers [0] # 5
            
                
def guess_number(): # Основная функция угадывания числа
    print('Хорошо, сейчас угадаю...')
    
    answer = ask_question('Это число делится без остатка на 2? (Да/Нет):')
    
    if answer == 'Да':
        result = process_even_numbers()
    else:
        result = process_odd_numbers()
        
    print(f'Твое число: {result}')
    
    
def main(): # Основная функция программы
    print_with_delay('Привет! Хочешь, я угадаю твое число?')
    answer = input('Напиши (Да/Нет): ').strip().capitalize()
    
    if answer == 'Нет':
        print('До скорой встречи! Как будет желание поиграть, просто скажи мне!')
        return
    
    print('Отлично! Тогда загадай число от 1 до 10')
    
    while True:
        answer = ask_question('Загадал (Да/Нет): ')
        
        if answer == 'Да':
            guess_number()
            break
        else:
            print('Как будешь готов, напиши "Готов":') 
            answer = input().strip().capitalize()
            if answer == 'Готов':
                guess_number()
                break
            
            
if __name__ == '__main__':
    main()