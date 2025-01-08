from tkinter import*

root = Tk()
root.geometry("392x410")
root.title("Tic Tac Toe")

frame=Frame(root,bg="#2b2727")
frame.pack()

titlelable=Label(frame,text="Tic Tac Toe      ",font=('Arial',25),bg='#fceb26',width=60)
titlelable.pack(padx=5,pady=5)

frame1 = Frame(root,bg="#929394")
frame1.pack()
turn="X"

end=False

bestmove = 1

board={1:" ",2:" ",3:" ",
       4:" ",5:" ",6:" ",
       7:" ",8:" ",9:" "}

def update():
    for key in board.keys():
        buttons[key-1]["text"]=board[key]

def restart():
    global end
    end=False
    for button in buttons:
        button["text"]=" "
    for i in board.keys():
        board[i]=" " 
    Drowlable=Label(frame1,text='                         ',font=('Arial',20),bg="#929394")
    Drowlable.grid(row=3,column=0,columnspan=3)

def Win(Player):
    if board[1]==board[2]and board[2]==board[3]and board[3]==Player:
        return True
    elif board[4]==board[5]and board[5]==board[6]and board[6]==Player:
        return True
    elif board[7]==board[8]and board[8]==board[9]and board[9]==Player:
        return True
    elif board[1]==board[4]and board[4]==board[7]and board[7]==Player:
        return True
    elif board[2]==board[5]and board[5]==board[8]and board[8]==Player:
        return True
    elif board[3]==board[6]and board[6]==board[9]and board[9]==Player:
        return True
    elif board[1]==board[5]and board[5]==board[9]and board[9]==Player:
        return True
    elif board[3]==board[5]and board[5]==board[7]and board[7]==Player:
        return True
    
    return False


def drow():
    
    for i in board.keys():
        if board[i]==" ":
            return False      
    return True

def gameover():
    winninglable=Label(frame1,text=f'{turn} Win the game',font=('Arial',20),bg="#929394")
    winninglable.grid(row=3,column=0,columnspan=3)

def minmax(board,ismaxamizing):
    if Win("O"):
        return 1
    if Win("X"):
        return -1
    if drow():
        return 0
    
    if ismaxamizing:
        bestscore = -100

        for key in board.keys():    
            if board[key]==" ":
                board[key]="O"
                score = minmax(board,False)
                board[key]=" "
                if score>bestscore:
                    bestscore=score
        return bestscore          
                
    else:
        bestscore = 100
        
        for key in board.keys():
            if board[key]==" ":
                board[key]="X"
                score = minmax(board,True)
                board[key]=" "
                if score<bestscore:
                    bestscore=score
        return bestscore             

def Computer():
    global bestmove 
    bestscore = -100

    for key in board.keys():
        if board[key]==" ":
            board[key]="O"
            score = minmax(board,False)
            board[key]=" "
            if score>bestscore:
                bestscore=score
                bestmove=key
         
    board[bestmove]="O"
    
def XorO(event):
    global turn,end

    if end==True:
        return
    
    button = event.widget
    Input=str(button)
    Input=Input[-1]
     

    if Input=='n':
        Input=1
    else:
        Input=int(Input)

    
    if button["text"]==" ":

        if turn=="X":
            
            board[Input]="X"
            if Win(turn):
                gameover()
                end=True
            turn="O"

            Computer()
            if Win(turn):
                gameover()
                end=True
            turn="X"
            update()
           
    if drow():
        Drowlable=Label(frame1,text= '    Game is Drow    ',font=('Arial',20),bg="#929394")
        Drowlable.grid(row=3,column=0,columnspan=3)

# First row
button1 = Button(frame1,text=" ",height=1,width=3,font=("Arial",40),bg="#f59b5f",borderwidth=3,relief=RAISED)
button1.grid(row = 0,column=0)
button1.bind("<Button-1>",XorO)

button2 = Button(frame1,text=" ",height=1,width=3,font=("Arial",40),bg="#f59b5f",borderwidth=3,relief=RAISED)
button2.grid(row = 0,column=1)
button2.bind("<Button-1>",XorO)

button3 = Button(frame1,text=" ",height=1,width=3,font=("Arial",40),bg="#f59b5f",borderwidth=3,relief=RAISED)
button3.grid(row = 0,column=2)
button3.bind("<Button-1>",XorO)

# Second Row
button4 = Button(frame1,text=" ",height=1,width=3,font=("Arial",40),bg="#f59b5f",borderwidth=3,relief=RAISED)
button4.grid(row = 1,column=0)
button4.bind("<Button-1>",XorO)

button5 = Button(frame1,text=" ",height=1,width=3,font=("Arial",40),bg="#f59b5f",borderwidth=3,relief=RAISED)
button5.grid(row = 1,column=1)
button5.bind("<Button-1>",XorO)

button6 = Button(frame1,text=" ",height=1,width=3,font=("Arial",40),bg="#f59b5f",borderwidth=3,relief=RAISED)
button6.grid(row = 1,column=2)
button6.bind("<Button-1>",XorO)

# Third row
button7 = Button(frame1,text=" ",height=1,width=3,font=("Arial",40),bg="#f59b5f",borderwidth=3,relief=RAISED)
button7.grid(row = 2,column=0)
button7.bind("<Button-1>",XorO)

button8 = Button(frame1,text=" ",height=1,width=3,font=("Arial",40),bg="#f59b5f",borderwidth=3,relief=RAISED)
button8.grid(row = 2,column=1)
button8.bind("<Button-1>",XorO)

button9 = Button(frame1,text=" ",height=1,width=3,font=("Arial",40),bg="#f59b5f",borderwidth=3,relief=RAISED)
button9.grid(row = 2,column=2)
button9.bind("<Button-1>",XorO)

restart=Button(frame1,text="Restart",height=1,width=6,font=("Arial",15),bg="#6bb3fa",borderwidth=3,relief=RAISED,command=restart)
restart.grid(row=0,column=5)

buttons=[button1,button2,button3,button4,button5,button6,button7,button8,button9]


root.mainloop()
