#!/user/bin/python3.12
# -*- coding: utf-8 -*-
# Создание GUI приложения Python Tkinter. Виджет Button

import tkinter as tk


def say_hello():
    print("hello!!!")


def add_label():
    label = tk.Label(win, text="new", background="red")
    label.pack()


def counter():
    global count  # используем глобальную функцию
    count += 1
    btn4['text'] = f"Счетчик: {count}"  # изменяем атрибут text на наше значение


count = 0
win = tk.Tk()
win.geometry("300x400+100+200")
win.title("Мое первое графическое приложение!!!")

btn1 = tk.Button(win,
                 text="Hello",
                 command=say_hello,
                 )  # У модуля tk, вызываем класс Button тем самым создаем виджет Button
# в качестве параметров классу Button передаем где будем его размещать (на нашем окне win)
# еще передаем текст, который будет на нашей кнопке размещен,
# еще передаем название функции обработчика нажатия кнопки, причем без ее вызова.

# Что-бы увидеть этот виджет на окне, его еще нужно расположить на окне,
# есть специальные методы которые это делают. У btn_1 вызовем такой метод pack()
btn2 = tk.Button(win, text="Add new label",  # Вторая кнопка, которая создает Label с текстом new
                 command=add_label,
                 )
btn3 = tk.Button(win, text="lambda: add label",
                 command=lambda: tk.Label(win, text="new lambda", background="blue").pack(),  # Третья кнопка где будем
                 )  # работать с Lambda функцией. Применим метод pack() к самой функции чтобы изменения отображались.
# Ниже, тоже применим метод pack(), как раньше, что бы сама кнопка тоже отображалась.
btn4 = tk.Button(win,
                 text=f"Счетчик: {count}",
                 command=counter,  # Четвертая кнопка где будем
                 bg='yellow',  # цвет фона кнопки
                 )  # делать счетчик в котором отображается количество нажатий на эту кнопку
btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()
win.mainloop()
