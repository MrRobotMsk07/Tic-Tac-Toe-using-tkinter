from tkinter import *
import tkinter.messagebox
from tkinter.font import Font

tk = Tk()
tk.resizable(False, False)
tk.title("Tic Tac Toe")

player_switch=True
flag = 0

my_font = Font(family = 'Ariel',size = 14,weight = 'bold')

def disableButton():
    button1.configure(state=DISABLED, disabledforeground="black")
    button2.configure(state=DISABLED, disabledforeground="black")
    button3.configure(state=DISABLED, disabledforeground="black")
    button4.configure(state=DISABLED, disabledforeground="black")
    button5.configure(state=DISABLED, disabledforeground="black")
    button6.configure(state=DISABLED, disabledforeground="black")
    button7.configure(state=DISABLED, disabledforeground="black")
    button8.configure(state=DISABLED, disabledforeground="black")
    button9.configure(state=DISABLED, disabledforeground="black")

def enableButton():
    button1.configure(state=NORMAL)
    button2.configure(state=NORMAL)
    button3.configure(state=NORMAL)
    button4.configure(state=NORMAL)
    button5.configure(state=NORMAL)
    button6.configure(state=NORMAL)
    button7.configure(state=NORMAL)
    button8.configure(state=NORMAL)
    button9.configure(state=NORMAL)

def color_reset():
    button1['bg'] = 'SteelBlue1'
    button2['bg'] = 'SteelBlue1'
    button3['bg'] = 'SteelBlue1'
    button4['bg'] = 'SteelBlue1'
    button5['bg'] = 'SteelBlue1'
    button6['bg'] = 'SteelBlue1'
    button7['bg'] = 'SteelBlue1'
    button8['bg'] = 'SteelBlue1'
    button9['bg'] = 'SteelBlue1'

def reset_game():
    global player_switch , flag
    button1['text'] = ' '
    button2['text'] = ' '
    button3['text'] = ' '
    button4['text'] = ' '
    button5['text'] = ' '
    button6['text'] = ' '
    button7['text'] = ' '
    button8['text'] = ' '
    button9['text'] = ' '
    player_switch = True
    flag = 0
    enableButton()
    turn["text"] = "X's Turn"
    color_reset()

def btnClick(buttons):
    global player_switch , flag

    if buttons["text"] == " " and player_switch == True:
        buttons["text"] = "X"
        player_switch = False
        turn["text"] = "O's Turn"
        checkForWin()
        flag += 1

    elif buttons["text"] == " " and player_switch == False:
        buttons["text"] = "O"
        player_switch = True
        turn["text"] = "X's Turn"
        checkForWin()
        flag += 1

    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Tile is Already Selected !!!")

def color_result():
    if ((button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X') or
        (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O')):
        button1['bg'] = 'pink'
        button2['bg'] = 'pink'
        button3['bg'] = 'pink'

    elif ((button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X') or
        (button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O')):
        button4['bg'] = 'pink'
        button5['bg'] = 'pink'
        button6['bg'] = 'pink'

    elif ((button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X') or
        (button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O')):
        button7['bg'] = 'pink'
        button8['bg'] = 'pink'
        button9['bg'] = 'pink'

    elif ((button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X') or
        (button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O')):
        button1['bg'] = 'pink'
        button5['bg'] = 'pink'
        button9['bg'] = 'pink'

    elif ((button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X') or
        (button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O')):
        button3['bg'] = 'pink'
        button5['bg'] = 'pink'
        button7['bg'] = 'pink'

    elif ((button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X') or
        (button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O')):
        button1['bg'] = 'pink'
        button4['bg'] = 'pink'
        button7['bg'] = 'pink'

    elif ((button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X') or
        (button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O')):
        button2['bg'] = 'pink'
        button5['bg'] = 'pink'
        button8['bg'] = 'pink'


    elif ((button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X') or
          (button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O')):
        button3['bg'] = 'pink'
        button6['bg'] = 'pink'
        button9['bg'] = 'pink'

    else:
        button1['bg'] = 'pink'
        button2['bg'] = 'pink'
        button3['bg'] = 'pink'
        button4['bg'] = 'pink'
        button5['bg'] = 'pink'
        button6['bg'] = 'pink'
        button7['bg'] = 'pink'
        button8['bg'] = 'pink'
        button9['bg'] = 'pink'

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
        color_result()
        turn["text"] = "X is Winner"

    elif (flag == 8):
        turn["text"] = "It is a Tie !!!"
        disableButton()
        color_result()

    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
          button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):

        turn["text"] = "O is Winner"
        color_result()
        disableButton()

button1 = Button(tk, text=" ", font=my_font, bg='SteelBlue1', fg='black', height=4, width=9,
                 command=lambda: btnClick(button1))
button1.grid(row=1, column=1)

button2 = Button(tk, text=' ', font=my_font, bg='SteelBlue1', fg='black', height=4, width=9,
                 command=lambda: btnClick(button2))
button2.grid(row=1, column=2)

button3 = Button(tk, text=' ', font=my_font, bg='SteelBlue1', fg='black', height=4, width=9,
                 command=lambda: btnClick(button3))
button3.grid(row=1, column=3)

button4 = Button(tk, text=' ', font=my_font, bg='SteelBlue1', fg='black', height=4, width=9,
                 command=lambda: btnClick(button4))
button4.grid(row=2, column=1)

button5 = Button(tk, text=' ', font=my_font, bg='SteelBlue1', fg='black', height=4, width=9,
                 command=lambda: btnClick(button5))
button5.grid(row=2, column=2)

button6 = Button(tk, text=' ', font=my_font, bg='SteelBlue1', fg='black', height=4, width=9,
                 command=lambda: btnClick(button6))
button6.grid(row=2, column=3)

button7 = Button(tk, text=' ', font=my_font, bg='SteelBlue1', fg='black', height=4, width=9,
                 command=lambda: btnClick(button7))
button7.grid(row=3, column=1)

button8 = Button(tk, text=' ', font=my_font, bg='SteelBlue1', fg='black', height=4, width=9,
                 command=lambda: btnClick(button8))
button8.grid(row=3, column=2)

button9 = Button(tk, text=' ', font=my_font, bg='SteelBlue1', fg='black', height=4, width=9,
                 command=lambda: btnClick(button9))
button9.grid(row=3, column=3)

exit = Button(tk, text='Quit', font=my_font, bg='IndianRed1', fg='black', height=2, width=9,
                 command=tk.destroy)
exit.grid(row=4,column=1)

turn = Button(tk, text="X's Turn", font=my_font, bg='lightyellow3', fg='black', height=2, width=9,
                state=DISABLED , disabledforeground="black")
turn.grid(row=4,column=2)

reset = Button(tk, text='Reset', font=my_font, bg='lightgreen', fg='black', height=2, width=9,
                 command=lambda: reset_game())
reset.grid(row=4,column=3)

tk.mainloop()