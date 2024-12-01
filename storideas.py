import tkinter, tkinter.ttk as ttk
from mod import en
from mod import es
from tkinter.font import Font

#CONSTANTS
TITLESIZE = 24

#GO TO LANGUAGE MENU
def gotolang(op,root):
    if(op == 1):
        en.guiMenu(root)
    if(op == 2):
        es.guiMenu(root)

#MAIN GUI MENU
#Create the main window
window = tkinter.Tk()
window.resizable(False, False)
window.title("MLT Storideas")

#Defining Title Font
titlefont = Font(size=TITLESIZE,
                 weight="normal")

#Main Frame
mainframe = ttk.Frame(window)
mainframe.grid(padx=10, pady=10)

#Title
title = ttk.Label(mainframe, text="MLT STORIDEAS", font=titlefont)
title.pack(padx=10,pady=10)

#Message
message = ttk.Label(mainframe, text="Select a language")
message.pack()

#Language Options
op = tkinter.IntVar()

#English
eng = ttk.Radiobutton(mainframe, text="English", variable=op, value=1)
eng.pack()

#Spanish
esp = ttk.Radiobutton(mainframe, text="Español", variable=op, value=2)
esp.pack()

#Button
button = ttk.Button(mainframe, text="Select", command=lambda: gotolang(op.get(),window))
button.pack()
    
#Infinte loop
window.mainloop()