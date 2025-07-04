# USD/RUB 
def usd_rub():
        usd = float(input('Введи число (USD): ')) # с usd в rub
        count_rub = usd * 78
        count_rub_rounded = round(count_rub, 2)  # Округляем до 2 знаков после точки
        print(count_rub_rounded, 'RUB') 
        

def rub_usd():
    rub = float(input('Введи число (RUB): ')) # c rub B usd
    count_usd = rub / 78
    count_usd_rounded = round(count_usd, 2)  # Округляем до 2 знаков после точки
    print(count_usd_rounded, 'USD')    


def choise_user_usd_rub(): # выбор пользователя в мейне 
    while True:
        choise = (input('Введи значение пары или "Вернуться назад": 1 - USD/RUB; 2 - RUB/USD; 3 - Назад: '))
        if choise == '1':
            usd_rub()
        elif choise == '2':
            rub_usd()
        else:
            main()


# USD/EUR
def usd_eur():
        usd = int(input('Введи число (USD): '))
        count_eur = usd * 0.85
        count_eur_rounded = round(count_eur, 2)  # Округляем до 2 знаков после точки
        print(count_eur_rounded, 'EUR') 
        

def eur_usd():
    eur = int(input('Введи число (EUR): '))
    count_usd = eur / 0.85
    count_usd_eur_rounded = round(count_usd, 2)  # Округляем до 2 знаков после точки
    print(count_usd_eur_rounded, 'USD')
    

def choise_user_usd_eur():  # выбор пользователя в мейне 
    while True:
        choise = (input('Введи значение пары или "Вернуться назад": 1 - USD/EUR; 2 - EUR/USD; 3 - Назад: '))
        if choise == '1':
            usd_eur()
        elif choise == '2':
            eur_usd()
        else:
            main()
        

# CNY_RUB
def cny_rub(): # с cny в rub
    cny = float(input('Введи число (CNY): '))
    count_rub = cny * 10.99
    count_rub_rounded = round(count_rub, 2)
    print(count_rub_rounded, 'RUB')
    
    
def rub_cny():
    rub = float(input('Введи число (RUB): ')) # с rub в cny
    count_cny = rub / 10.99
    count_cny_rounded = round(count_cny, 2)  # Округляем до 2 знаков после точки
    print(count_cny_rounded, 'CNY') 


def choise_user_cny_rub():  # выбор пользователя в мейне 
    while True:
        choise = (input('Введи значение пары или "Вернуться назад": 1 - CNY/RUB; 2 - RUB/CNY; 3 - Назад: '))
        if choise == '1':
            cny_rub()
        elif choise == '2':
            rub_cny()
        else:
            main()


def main(): # Основная функция программы
    print('Необходимо выбрать валюту или "Выйти":')
    chois_curr = (input('1 - RUB; 2 - USD; 3 - CNY; 4 - Выйти: '))
    print(chois_curr)
    
    if chois_curr == '1':
        return choise_user_usd_rub()
    elif chois_curr == '2':
        return choise_user_usd_eur()
    elif chois_curr == '3':
        return choise_user_cny_rub()
    else:
        exit()   
        
        
if __name__ == '__main__':
    main()