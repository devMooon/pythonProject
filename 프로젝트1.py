from tkinter import *
import tkinter.font as tkFont
import math

#함수
def percent_sign() :
    result = float(txt.get("0.0", END))
    result /= 100
    txt.delete("0.0", END)
    txt.insert("0.0", result)

def delete_sign() :
    result = float(txt.get("0.0", END))
    result = 0
    txt.delete("0.0", END)
    txt.insert("0.0", result)

def back_sign() :
    result = txt.get("0.0", END)
    if len(result) == 2:
        txt.delete("0.0", END)
        txt.insert("0.0", "0")
    else:
        txt.delete("0.0", END)
        txt.insert("0.0", result[:-2])

def change_sign(n):
    try:
        result = int(txt.get("0.0", END))
    except:
        result = txt.get("0.0", END)
        result = float(result[:-1])

    if n == 1:
        result /= (result*result)
    elif n == 2:
        result *= result
    else :
        result = math.sqrt(result)

    txt.delete("0.0", END)
    txt.insert("0.0", result)

def plus_sign(n):
    result = txt.get("0.0", END)
    result = result[:-1] + n
    txt.delete("0.0", END)
    txt.insert("0.0", result)

def equal_sign():
    #try:
    result = txt.get("0.0", END)
    result = eval(result)
    #except SyntaxErrory:
    txt.delete("0.0", END)
    txt.insert("0.0", result)

#숫자
def change_number(n):
    result = txt.get("0.0", END)
    if result[0] == "0":
        result = result[:-1]

    result = result[:-1] + n

    txt.delete("0.0", END)
    txt.insert("0.0", result)

#윈도우 기본 설정
main = Tk()
main.attributes('-alpha', 0.95)
main.title("계산기")
main.geometry("320x475")
main.resizable(False, False)

#숫자 입력창
label = Label(text = "   표준", width = 26, height = 2, bg = "gray90", anchor = "w")
fontexample = tkFont.Font(family="나눔고딕", size = 15, weight = "bold")
label.configure(font=fontexample)

txt = Text(width = 21, height = 3, bg = "gray90", bd = 0)
fontexample = tkFont.Font(family="Arial", size = 20, weight = "bold")
txt.configure(font=fontexample)
txt.insert(1.0, "0")

#버튼 추가
signBtn1 = Button(text = "%", width = "10", height="3", bg = "gray92", relief = "groove", bd = 1, command = percent_sign)
signBtn2 = Button(text = "CE", width = "10", height="3", bg = "gray92", relief = "groove", bd = 1, command = delete_sign)
signBtn3 = Button(text = "C", width = "10", height="3", bg = "gray92", relief = "groove", bd = 1, command = delete_sign)
signBtn4 = Button(text = "<-", width = "10", height="3", bg = "gray92", relief = "groove", bd = 1, command = back_sign) #이미지 삽입?

signBtn5 = Button(text = "1/x", width = "10", height="3", bg = "gray92", relief = "groove", bd = 1, command = lambda: change_sign(1))
signBtn6 = Button(text = "x^2", width = "10", height="3", bg = "gray92", relief = "groove", bd = 1, command = lambda: change_sign(2))
signBtn7 = Button(text = "√x", width = "10", height="3", bg = "gray92", relief = "groove", bd = 1, command = lambda: change_sign(3))
signBtn8 = Button(text = "÷", width = "10", height="3", bg = "gray92", relief = "groove", bd = 1, command = lambda: plus_sign('/'))

numBtn7 = Button(text = "7", width = "10", height="3", bg = "gray100", relief = "groove", bd = 1, command = lambda: change_number('7'))
numBtn8 = Button(text = "8", width = "10", height="3", bg = "gray100", relief = "groove", bd = 1, command = lambda: change_number('8'))
numBtn9 = Button(text = "9", width = "10", height="3", bg = "gray100", relief = "groove", bd = 1, command = lambda: change_number('9'))
signBtn9 = Button(text = "×", width = "10", height="3", bg = "gray92", relief = "groove", bd = 1, command = lambda: plus_sign('*'))

numBtn4 = Button(text = "4", width = "10", height="3", bg = "gray100", relief = "groove", bd = 1, command = lambda: change_number('4'))
numBtn5 = Button(text = "5", width = "10", height="3", bg = "gray100", relief = "groove", bd = 1, command = lambda: change_number('5'))
numBtn6 = Button(text = "6", width = "10", height="3", bg = "gray100", relief = "groove", bd = 1, command = lambda: change_number('6'))
signBtn10 = Button(text = "-", width = "10", height="3", bg = "gray92", relief = "groove", bd = 1, command = lambda: plus_sign('-'))

numBtn1 = Button(text = "1", width = "10", height="3", bg = "gray100", relief = "groove", bd = 1, command = lambda: change_number('1'))
numBtn2 = Button(text = "2", width = "10", height="3", bg = "gray100", relief = "groove", bd = 1, command = lambda: change_number('2'))
numBtn3 = Button(text = "3", width = "10", height="3", bg = "gray100", relief = "groove", bd = 1, command = lambda: change_number('3'))
signBtn11 = Button(text = "+", width = "10", height="3", bg = "gray92", relief = "groove", bd = 1, command = lambda: plus_sign('+'))

signBtn12 = Button(text = "±", width = "10", height="3", bg = "gray100", relief = "groove", bd = 1)
numBtn0 = Button(text = "0", width = "10", height="3", bg = "gray100", relief = "groove", bd = 1, command = lambda: change_number('0'))
signBtn13 = Button(text = ".", width = "10", height="3", bg = "gray100", relief = "groove", bd = 1, command = lambda: plus_sign('.'))
signBtn14 = Button(text = "=", width = "10", height="3", bg = "skyblue", relief = "groove", bd = 1, command = equal_sign)

#숫자 입력창 윈도우에 삽입
label.grid(row=0, column=0, columnspan = 4)
txt.grid(row=1, column=0, rowspan = 2, columnspan = 4)

#버튼 윈도우에 삽입

#grid 첫번째 셀 기준
signBtn1.grid(row=3, column=0)
signBtn2.grid(row=3, column=1)
signBtn3.grid(row=3, column=2)
signBtn4.grid(row=3, column=3)

signBtn5.grid(row=4, column=0)
signBtn6.grid(row=4, column=1)
signBtn7.grid(row=4, column=2)
signBtn8.grid(row=4, column=3)

numBtn7.grid(row=5, column=0)
numBtn8.grid(row=5, column=1)
numBtn9.grid(row=5, column=2)
signBtn9.grid(row=5, column=3)

numBtn4.grid(row=6, column=0)
numBtn5.grid(row=6, column=1)
numBtn6.grid(row=6, column=2)
signBtn10.grid(row=6, column=3)

numBtn1.grid(row=7, column=0)
numBtn2.grid(row=7, column=1)
numBtn3.grid(row=7, column=2)
signBtn11.grid(row=7, column=3)

signBtn12.grid(row=8, column=0)
numBtn0.grid(row=8, column=1)
signBtn13.grid(row=8, column=2)
signBtn14.grid(row=8, column=3)

main.mainloop()