def convert_currency(amount: float, rate: float, from_curr: str, to_curr: str) -> float: #Общая функция для конвертации валюты
    converted_amount = amount * rate
    return round(converted_amount, 2)

def get_currency_input(currency_name: str) -> float: # Получение ввода суммы от пользователя
    while True:
        try:
            amount = float(input(f'Введите сумму в {currency_name}: '))
            if amount >= 0:
                return amount
            print("Сумма должна быть положительной. Попробуйте снова.")
        except ValueError:
            print("Ошибка: введите числовое значение.")

def currency_pair_handler(pair_name: str, direct_rate: float, reverse_rate: float, curr1: str, curr2: str): #Обработчик для пары валют
    while True:
        choice = input(f'Выберите направление конвертации ({pair_name}):\n'
                      f'1 - {curr1} → {curr2}\n'
                      f'2 - {curr2} → {curr1}\n'
                      f'3 - Назад\n'
                      'Ваш выбор: ')
        
        if choice == '1':
            amount = get_currency_input(curr1)
            result = convert_currency(amount, direct_rate, curr1, curr2)
            print(f'{result} {curr2}')
        elif choice == '2':
            amount = get_currency_input(curr2)
            result = convert_currency(amount, reverse_rate, curr2, curr1)
            print(f'{result} {curr1}')
        elif choice == '3':
            return
        else:
            print("Неверный ввод. Попробуйте снова.")

def usd_rub_handler(): # Обработчик пары USD/RUB
    currency_pair_handler("USD/RUB", 78, 1/78, "USD", "RUB")

def usd_eur_handler(): #Обработчик пары USD/EUR
    currency_pair_handler("USD/EUR", 0.85, 1/0.85, "USD", "EUR")

def cny_rub_handler(): #Обработчик пары CNY/RUB
    currency_pair_handler("CNY/RUB", 10.99, 1/10.99, "CNY", "RUB")

def main(): #Основная функция программы
    while True:
        print('\nВыберите валютную пару или выход:')
        choice = input('1 - USD/RUB\n'
                      '2 - USD/EUR\n'
                      '3 - CNY/RUB\n'
                      '4 - Выйти\n'
                      'Ваш выбор: ')
        
        if choice == '1':
            usd_rub_handler()
        elif choice == '2':
            usd_eur_handler()
        elif choice == '3':
            cny_rub_handler()
        elif choice == '4':
            print("До свидания!")
            break
        else:
            print("Неверный ввод. Попробуйте снова.")

if __name__ == '__main__':
    main()