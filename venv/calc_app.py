import sys
import math
import random
import threading
import time
import re
import sqlite3
import csv
import tkinter

from tkinter import *
from tkinter import ttk

window =TK()

class Calculator:
    calc_value = 0.0
    div_trigger = False
    mult_trigger = False
    add_trigger = False
    sub_trigger = False

    def button_press(self, value):
        entry_val = self.number_entry.get()
        entry_val += value
        self.number_entry.delete(0, 'end')
        self.number_entry.insert(0, entry_val)

    def is_float(self, str_val):
        try:
            float(str_val)
            return True
        except ValueError:
            return False

    def math_button_press(self, value):
        if self.is_float(str.number_entry.get()):
            self.add_trigger = False
            self.sub_trigger = False
            self.mult_trigger = False
            self.div_trigger = False
            self.calc_value = float(self.entry_value.get())
            if value =="/":
                print("/ pressed")
                self.div_trigger = True
            elif value == "*":
                print(" * pressed")
                self.mult_trigger = True
            elif value == "+":
                print(" + pressed")
                self.add_trigger = True
            else:
                print(" - pressed")
                self.add_trigger = True


            self.number_entry.delete(0, "end")

    def equal_button_press(self):
        if self.add_trigger or self.sub_trigger or self.mult_trigger or self.div_trigger:
            if self.add_trigger:
                solution = self.calc_value + float(self.entry_value.get())
            elif self.sub_trigger:
                solution = self.calc_value - float(self.entry_value.get())
            elif self.mult_trigger:
                solution = self.calc_value * float(self.entry_value.get())
            else:
                solution = self.calc_value / float(self.entry_value.get())

        print(self.calc_value, " ", float(self.entry).get(), " ", solution)
        self.number_entry.delete(0, "end")
        self.number_entry.insert(0, solution)

    def _init_(self,window):
        self.entry_value = StringVar(window, value="")
        window.title("Calculator")
        window.geometry("500x250")
        window.resizable(width=False, height=False)
        style = ttk.Style()
        style.configure("TButton",
                        font="serif 15",
                        padding=10)
        style.configure("TEntry",
                        font="serif 18",
                        padding=10)
        self.number_entry = ttk.Entry(window,
                                      textvariable=self.entry_value, width=50, )
        self.number_entry.grid(row=0, columsapn=4)
        # -------------1st Row-----------------
        self.button7 = tkinter.Button(window, text="7", command=lambda: self.button_press('7')).grid(row=1, column=0)
        self.button8 = tkinter.Button(window, text="8", command=lambda: self.button_press('8')).grid(row=1, column=1)
        self.button9 = tkinter.Button(window, text="9", command=lambda: self.button_press('9')).grid(row=1, column=2)
        self.button_div = ttk.Button(window, text="/", command=lambda: self.math_button_press('/')).grid(row=1, column=3)
        # ------------2nd Row-------------------
        self.button4 = ttk.Button(window, text="4", command=lambda: self.button_press('4')).grid(row=2, column=0)
        self.button5 = ttk.Button(window, text="5", command=lambda: self.button_press('5')).grid(row=2, column=1)
        self.button6 = ttk.Button(window, text="6", command=lambda: self.button_press('6')).grid(row=2, column=2)
        self.button_mult = ttk.Button(window, text="*", command=lambda: self.math_button_press('*')).grid(row=2, column=3)
        # -------------3rd Row------------------
        self.button1 = ttk.Button(window, text="1", command=lambda: self.button_press('1')).grid(row=3, column=0)
        self.button2 = ttk.Button(window, text="2", command=lambda: self.button_press('2')).grid(row=3, column=1)
        self.button3 = ttk.Button(window, text="3", command=lambda: self.button_press('3')).grid(row=3, column=2)
        self.button_add = ttk.Button(window, text="+", command=lambda: self.math_button_press('+')).grid(row=3, column=3)
        # ------------4th Row------------------------------------
        self.button_clear = ttk.Button(window, text="AC", command=lambda: self.math_button_press('AC')).grid(row=4,
                                                                                                           column=0)
        self.button0 = ttk.Button(window, text="0", command=lambda: self.button_press('0')).grid(row=4, column=1)
        self.button_equal = ttk.Button(window, text="=", command=lambda: self.math_button_press('=')).grid(row=4,
                                                                                                         column=2)
        self.button_sub = ttk.Button(window, text="-", command=lambda: self.math_button_press('-')).grid(row=4, column=3)


        window = tk()
        calc = Calculator(window)
        window.mainloop()







