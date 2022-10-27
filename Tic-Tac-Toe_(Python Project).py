from tkinter import *
import tkinter.messagebox
from tkinter.font import Font

tk = Tk()
tk.resizable(False, False)
tk.title("Tic Tac Toe")

player_switch = True
flag = 0

my_font = Font(family = 'Ariel',size = 14,weight = 'bold')

def disableButton():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)

def btnClick(buttons):
    global player_switch, flag

    if buttons["text"] == " " and player_switch == True:
        buttons["text"] = "X"
        player_switch = False
        checkForWin()
        flag += 1


    elif buttons["text"] == " " and player_switch == False:
        buttons["text"] = "O"
        player_switch = True
        checkForWin()
        flag += 1
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Tile is Already Selected !!!")


def checkForWin():
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
        button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
        button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
        button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
        button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
        button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
        button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "X is Winner !!!")

    elif (flag == 8):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie !!!")

    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
          button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "O Winner !!!")


button1 = Button(tk, text=" ", font=my_font, bg='lightgray', fg='black', height=4, width=8,
                 command=lambda: btnClick(button1))
button1.grid(row=3, column=0)

button2 = Button(tk, text=' ', font=my_font, bg='lightgray', fg='black', height=4, width=8,
                 command=lambda: btnClick(button2))
button2.grid(row=3, column=1)

button3 = Button(tk, text=' ', font=my_font, bg='lightgray', fg='black', height=4, width=8,
                 command=lambda: btnClick(button3))
button3.grid(row=3, column=2)

button4 = Button(tk, text=' ', font=my_font, bg='lightgray', fg='black', height=4, width=8,
                 command=lambda: btnClick(button4))
button4.grid(row=4, column=0)

button5 = Button(tk, text=' ', font=my_font, bg='lightgray', fg='black', height=4, width=8,
                 command=lambda: btnClick(button5))
button5.grid(row=4, column=1)

button6 = Button(tk, text=' ', font=my_font, bg='lightgray', fg='black', height=4, width=8,
                 command=lambda: btnClick(button6))
button6.grid(row=4, column=2)

button7 = Button(tk, text=' ', font=my_font, bg='lightgray', fg='black', height=4, width=8,
                 command=lambda: btnClick(button7))
button7.grid(row=5, column=0)

button8 = Button(tk, text=' ', font=my_font, bg='lightgray', fg='black', height=4, width=8,
                 command=lambda: btnClick(button8))
button8.grid(row=5, column=1)

button9 = Button(tk, text=' ', font=my_font, bg='lightgray', fg='black', height=4, width=8,
                 command=lambda: btnClick(button9))
button9.grid(row=5, column=2)

tk.mainloop()