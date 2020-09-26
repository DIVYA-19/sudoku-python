from tkinter import *
import tkinter.font as tkFont
from sudokusol import *
import random

global player


def fillPuzzle(size,btn):
    global grid
    grid = []
    player = []
    start_player = []
    for i in range(size):
        player.append([0]*size)
        start_player.append([0]*size)        
    for i in range(size):
        grid.append([0]*size)
    x,y = random.randint(0,size),random.randint(0,size)
    sudoku(grid,x,y,size)
    print(grid)
    for i in range(size):
        for j in range(size):
            if random.random() > 0.7:
                player[i][j] = grid[i][j]
                start_player[i][j] = grid[i][j]
                btn[i][j].configure(text=grid[i][j],state=DISABLED ,font=font)
    return player,start_player

def action(x,y,size):
    orig_color = btn[x][y].cget("bg")
    def enter(size):
        value = i.get()
        value = int(value)
        if isValid(player,x,y,value,size):
            btn[x][y].configure(bg=orig_color)
            player[x][y] = value
            btn[x][y].configure(text=value ,font=font)
            value_window.destroy()
            for item in player:
                if 0 in item:
                    break
            else:
                win = Tk()
                win_f = tkFont.Font(family="helvetica", size=25)
                win_label = Label(win,text="Solved!!!",font=font)
                win_label.pack()
        else:
            btn[x][y].configure(bg=orig_color)
            value_window.destroy()
            notValid = Tk()
            notValid.geometry("100x20")
            l = Label(notValid,text="Not Possible")
            l.pack()
    
    print(x,y)
    btn[x][y].configure(bg="red")
    value_window = Tk()
    value_window.geometry("220x50")
    b = Button(value_window,text="SUBMIT", command= lambda size=size: enter(size))
    b.pack(side=BOTTOM)
    w = Label(value_window, text="Value to enter:",font=font)
    w.pack(side=LEFT)
    i = Entry(value_window,width=5,font=font)
    i.pack(side=LEFT)    

    value_window.mainloop()

#example values
def builtGrid(size):
    global root
    root = Tk()
    root.title("sudoku")
    global font
    font = tkFont.Font(family="helvetica", size=12)
    root.geometry("500x500")
    frame = Frame(root)
    Grid.rowconfigure(root, 0, weight=1)
    Grid.columnconfigure(root, 0, weight=1)
    frame.grid(row=0, column=0, sticky=N+S+E+W)
    grid=Frame(frame)
    global btn
    btn = []
    for i in range(size+1):
        temp = []
        for j in range(size):
            bt = None
            temp.append(bt)
        btn.append(temp)
    x_axis = []
    count = 1
    for i in range(1,size):
        if i%sizes[size][0] == 0:
            x_axis.append(count*(sizes[size][0]) -1)
            count += 1
    print(x_axis)
    y_axis = []
    count = 1
    for i in range(1,size):
        if i%sizes[size][1] == 0:
            y_axis.append(count*(sizes[size][1]) - 1)
            count += 1
    for x in range(size):
        for y in range(size):
            btn[x][y] = Button(frame, command= lambda x=x,y=y,size=size: action(x,y,size))
            if y in y_axis:
                btn[x][y].grid(column=y, row=x,padx=(0,5), sticky="nsew")
            if x in x_axis:
                btn[x][y].grid(column=y, row=x,pady=(0,5), sticky="nsew")
            else:
                btn[x][y].grid(column=y, row=x, sticky="nsew")

    for x in range(size):
      Grid.columnconfigure(frame, x, weight=1)

    for y in range(size+1):
      Grid.rowconfigure(frame, y, weight=1)
    global player
    player,start_player = fillPuzzle(size,btn)

    stop = Button(frame,text=" quit ",width=6,height=2,bg='red',command=stop_play)
    stop.grid(row=size+1,columnspan=size//4,pady=7)
    main_menu = Button(frame,text=" menu ",width=6,height=2,command=menu)
    main_menu.grid(row=size+1,column=size//4,pady=7,padx=5)
    reset_b = Button(frame,text=" reset ",width=6,height=2,command=lambda start_player=start_player: reset(start_player))
    reset_b.grid(row=size+1,column=(size//4)*2,pady=7)
    restart_b = Button(frame,text=" restart ",width=6,height=2,command= restart)
    restart_b.grid(row=size+1,column=(size//4)*3,pady=7)

def stop_play():
    root.destroy()

def start_action(n):
    builtGrid(n)
    global size
    size = n
    start_frame.destroy()

def restart():
    root.destroy()
    builtGrid(size)

def menu():
    root.destroy()
    options()

def reset(start_player):
    print(start_player)
    for i in range(size):
        for j in range(size):
            if start_player[i][j]!=0:
                print(start_player[i][j])
                player[i][j] = start_player[i][j]
                btn[i][j].configure(text=start_player[i][j],state=DISABLED ,font=font)
            else:
                player[i][j] = 0
                btn[i][j].configure(text='',font=font)

def options():
    global start_frame
    start_frame = Tk()
    start_frame.geometry("300x300")

    bt1 = Button(start_frame,text=6,width=10,height=5, command= lambda size=6: start_action(6))
    bt1.pack(side=BOTTOM)
    #bt1.place(x=50,y=50)
    bt2  =Button(start_frame,text=9,width=10,height=5, command= lambda size=9: start_action(9))
    bt2.pack(side=BOTTOM)
    bt3 = Button(start_frame,text=15,width=10,height=5, command= lambda size=15: start_action(15))
    bt3.pack(side=BOTTOM)
    start_frame.mainloop()
options()
root.mainloop()
