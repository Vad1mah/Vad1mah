from tkinter import *
from tkinter import ttk
import os

def check():
    global i
    global score
    s = f'{var1.get()}' + f'{var2.get()}' + f'{var3.get()}' + f'{var4.get()}'
    if s == answer[i][4]:
        score += 1
    if i != len(answer) - 1:
        i += 1
        var1.set(0)
        var2.set(0)
        var3.set(0)
        var4.set(0)
        label1.config(text=question[i])
        button1_text.set(value=answer[i][0])
        button2_text.set(value=answer[i][1])
        button3_text.set(value=answer[i][2])
        button4_text.set(value=answer[i][3])
    else:
        button1.destroy()
        button2.destroy()
        button3.destroy()
        button4.destroy()
        check_button.destroy()
        if score == 0:
            label1.config(text='Количество правильных ответов ' + str(score) + ' из ' + str(len(answer)) + ' (' + ' 0% ' + ')')
        else:
            label1.config(text='Количество правильных ответов ' + str(score) + ' из ' + str(len(answer)) + ' ( ' + str(int(score/len(answer) * 100)) + '% )')
        
answer = [
    ["(1) Воды +","(2) Еды","(3) Деревьев","(4) Насекомых", "1000"],
    ["(1) Обэма","(2) Путин +","(3) Путлер","(4) Билли Херингтон", "0100"],
    ["(1) 2","(2) 3","(3) 4","(4) 5 +", "0001"],
    ["(1) 8","(2) 9","(3) 10","(4) 11 +", "0001"],
    ["(1) Деревья +","(2) Водоросли +","(3) Грибы","(4) Мох", "1100"]
]

root = Tk()
root.geometry("500x500")
frm = ttk.Frame(root, padding=10)
frm.grid(sticky=(N,S,E,W))

script_dir = os.path.dirname(__file__)
rel_path = "Questions.txt"
abs_file_path = os.path.join(script_dir, rel_path)

score = 0
i = 0
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
button1_text = StringVar(value=answer[i][0])
button2_text = StringVar(value=answer[i][1])
button3_text = StringVar(value=answer[i][2])
button4_text = StringVar(value=answer[i][3])
label2 = StringVar()

question = open(abs_file_path, encoding = 'utf-8', mode = 'r').readlines()
label1 = ttk.Label(frm, text=question[i])
label1.grid(row=0, column=0, sticky="W")
label2 = ttk.Label(frm, text='Имя файла: ' + rel_path + '\n(выбор файла добавим позже)')
label2.grid(row=0, column=0, padx=315)
button1 = ttk.Checkbutton(frm, textvariable=button1_text, variable=var1, onvalue=1, offvalue=0)
button1.grid(row=1, column=0, sticky="W")
button2 = ttk.Checkbutton(frm, textvariable=button2_text, variable=var2, onvalue=1, offvalue=0)
button2.grid(row=2, column=0, sticky="W")
button3 = ttk.Checkbutton(frm, textvariable=button3_text, variable=var3, onvalue=1, offvalue=0)
button3.grid(row=3, column=0, sticky="W")
button4 = ttk.Checkbutton(frm, textvariable=button4_text, variable=var4, onvalue=1, offvalue=0)
button4.grid(row=4, column=0, sticky="W")
check_button = ttk.Button(frm, text="Ответить", command=check)
check_button.grid(row=5, column=0, sticky="W")

root.mainloop()