from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import math


def show_massage(): #Функция для выполнения вычислений
    name1 = int(count.get())
    name3 = (cont3.get())
    name2 = int(cont2.get())
    umn = name1 * name2
    umn1 = name1 // name2
    umn2 = name1 / name2
    summa = name1 + name2
    vichet = name1 - name2
    
    if name3 == "*": #логика вывода ответа
        messagebox.showinfo( "Твой ответ", f"{name1}  *  {name2}  =  {umn}")
    if name3 == "/" and name1 > name2:
        messagebox.showinfo( "Твой ответ", f"{name1}  /  {name2}  =  {umn1}")
    elif name3 == "/" and name1 < name2:
        messagebox.showinfo( "Твой ответ", f"{name1}  /  {name2}  =  {umn2}")
    if name3 == "+":
        messagebox.showinfo( "Твой ответ", f"{name1}  +  {name2}  =  {summa}")
    if name3 == "-":
        messagebox.showinfo( "Твой ответ", f"{name1}  -  {name2}  =  {vichet}")
    
        

root = Tk() #Основное окно приложения
root.title("Мой калькулятор")
root.geometry("350x300")

Label(root, text="Введи первое число:").pack(pady=10) #поля для получения числа и операции
count = Entry(root)
count.pack(pady=5)
Label(root, text="Введи операцию:").pack(pady=10)
cont3 = Entry(root)
cont3.pack(pady=3)
Label(root, text="Введи второе число:").pack(pady=10)
cont2 = Entry(root)
cont2.pack(pady=5)

    
Button(root, text="Ответ", command=show_massage).pack(pady=15) #кнопки в интерфейсе
Button(root, text="Закрыть", command=root.quit).pack(pady=5)

root.mainloop()
