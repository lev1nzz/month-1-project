# from tkinter import *
# from tkinter import ttk

# root = Tk()
# root.title('Конверт Валют')
# root.geometry('400x500+500+200')

# label = Label(text = 'ВЫБЕРИ ВАЛЮТУ', font=("Arial", 14))
# icon = PhotoImage(file = "icon.png")
# root.iconphoto(False, icon)
# label.pack()

# languages = ["USD/RUB", "", "", ""]
# combobox = ttk.Combobox(values=languages)
# combobox.pack(anchor=NW, padx=6, pady=6)

# root.mainloop()


# USD/RUB 
def usd_rub():
        usd = float(input('Введи число (USD): '))
        count_rub = usd * 78
        print(count_rub, 'RUB') 
        

def rub_usd():
    rub = float(input('Введи число (RUB): '))
    count_usd = rub / 78
    print(count_usd, 'USD')    


def choise_user_usd_rub():
    choise = (input('Введи значение пары: 1 - USD/RUB; 2 - RUB/USD:'))
    if choise == '1':
        usd_rub()
    elif choise == '2':
        rub_usd()


# USD/EUR
def usd_eur():
        usd = float(input('Введи число (USD): '))
        count_rub = usd * 0.85
        print(count_rub, 'EUR') 
        

def eur_usd():
    eur = float(input('Введи число (EUR): '))
    count_usd = eur / 0.85
    print(count_usd, 'USD')
    

def choise_user_usd_eur():
    choise = (input('Введи значение пары: 1 - USD/EUR; 2 - EUR/USD:'))
    if choise == '1':
        usd_eur()
    elif choise == '2':
        eur_usd()
        

def main():
    print('Необходимо выбрать валюту:')
    chois_curr = (input('1 - RUB; 2 - USD: '))
    print(chois_curr)
    
    if chois_curr == '1':
        return choise_user_usd_rub()
    elif chois_curr == '2':
        return choise_user_usd_eur()
        
        
        
if __name__ == '__main__':
    main()