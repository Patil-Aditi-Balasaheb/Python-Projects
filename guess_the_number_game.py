from tkinter import *
from tkinter.ttk import *
import random

attempts = 10                    # initialize the attempts variable
answer = random.randint(1,100)   # generating a random number
running = True                   # initialize running variable as TRUE to execute the program again and again

while running==True:
    def check_answer():
        global attempts
        global text
        global running

        attempts -= 1            # decrementing the attempts variable

        guess = int(entry_window.get())              # user input to guess the number

        if answer == guess:
            text.set('YOU WIN! CONGRATS!')
            btn_check.destroy()                      # removing the Check button
            running=False                            # running variable is set FALSE to stop the program from executing again
            btn_restart.grid(row = 3, column = 1, padx = 50)                       # displaying the Play Again! button
        elif attempts == 0:
            text.set('Sorry, you are out of attempts. Better luck next time')
            btn_check.destroy()                      # removing the Check button
            running=False                            # running variable is set FALSE to stop the program from executing again
            btn_restart.grid(row = 3, column = 1, padx = 50)                       # displaying the Play Again! button
        elif guess < answer:
            text.set('Incorrect Guess! You have '+ str(attempts) +' attempts remaining. Go Higher!')
        elif guess > answer:
            text.set('Incorrect Guess! You have '+ str(attempts) +' attempts remaining. Go Lower!')
            
        return


    def play_again():
        root.destroy()                   # closing the window
        global attempts                  
        global running
        running=True                     # running variable is set TRUE to execute the program again
        attempts=10                      # attempts is again initialized to 10 for every game
    
    def quit():
        global running
        running=False                    # running variable is set FALSE to stop the program from executing again
        root.destroy()                   # closing the window
        
        
    root= Tk()
    root.title('Guess the number')        # title of the window
    root.geometry('800x300')              # size of the window
    root.configure(bg='white')            # background color of window
    root.protocol('WM_DELETE_WINDOW', quit)              # calling the quit() function on click of 'X' button

    style = Style()
    style.configure('TButton', font = ('calibri', 16, 'bold'), borderwidth = '4')
    style.configure('TLabel', font = ('calibri', 16, 'bold'), background = 'white')
   
    style.map('C.TButton', foreground = [('active', 'green')],background = [('active', 'black')])
    style.map('P.TButton', foreground = [('active', 'blue')],background = [('active', 'black')])
    style.map('Q.TButton', foreground = [('active', 'red')],background = [('active', 'black')])
    
    # label 1
    label = Label(root, text = 'GUESS THE NUMBER BETWEEN 1 TO 100')
    label.grid(row = 0, column = 1, pady = 10, padx = 50)
    
    # entry 1
    input_text = StringVar() 
    entry_window = Entry(root, textvariable = input_text, justify = CENTER, font = ('courier', 16, 'bold')) 
    entry_window.focus_force() 
    entry_window.grid(row = 1, column = 1)
    
    # button Check
    btn_check = Button(root, text = 'Check', style = 'C.TButton', command = check_answer)
    btn_check.grid(row = 1, column = 2)
    
    # Label 2
    text = StringVar()
    text.set('You have 10 attempts remaining. Good luck!')
    guess_attempts = Label(root, textvariable=text, font = ('calibri',14))
    guess_attempts.grid(row = 2, column = 1, pady = 10, padx = 50)
    
    # button Play Again!
    btn_restart = Button(root, text='Play Again!', style = 'P.TButton', command = play_again)
    
    # button Quit Game!
    btn_quit = Button(root, text = 'Quit Game!', style = 'Q.TButton', command = quit)
    btn_quit.grid(row = 4, column = 1, pady = 10, padx = 50)
    
    root.mainloop()
    