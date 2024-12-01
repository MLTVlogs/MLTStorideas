import io
import tkinter
import tkinter.ttk as ttk
from tkinter.font import Font

TITLESIZE = 24
SUBTITLESIZE = 18

#######################################
#FUNCTIONS
#######################################
#4-Element Story Save English
def four_elementSave(chr,goal,obst,reso,window):
    #Open the file
    try:
        story = io.open("story.txt","w")
    except FileNotFoundError:
        return

    #write the elements in the file
    story.write(f"CHARACTER: {chr}")
    story.write(f"GOAL: {goal}")
    story.write(f"OBSTACLE: {obst}")
    story.write(f"RESOLUTION: {reso}")

    #Close the file
    story.close()

    #Close the window
    guiMenu(window)

#4-Element Story GUI English
def four_elementGui(mainmenu):
    #Close the main menu
    mainmenu.destroy()

    #Main Window 
    window = tkinter.Tk()
    window.title("MLT Storideas")
    window.resizable(False,False)

    #Set Icon
    icon = tkinter.PhotoImage(file="artwork/storideas_icon.png")
    window.iconphoto(False,icon)

    #Title Font
    subtitlefont = Font(size=SUBTITLESIZE,
                    weight="normal")

    #MainFrame
    mainframe = ttk.Frame(window)
    mainframe.grid(padx=10,pady=10)

    #Frames
    frame1 = ttk.Frame(mainframe)
    frame1.grid(row=0)

    frame2 = ttk.Frame(mainframe)
    frame2.grid(row=1)

    frame3 = ttk.Frame(mainframe)
    frame3.grid(row=2)

    #Title
    title = ttk.Label(frame1,text="4-ELEMENT STORY", font=subtitlefont)
    title.grid(row=0,column=0,padx=3,pady=3)

    #Character
    labelchr = ttk.Label(frame2,text="CHARACTER",font=("Arial",10))
    labelchr.grid(row=1,column=0,sticky="w")
    textchr = tkinter.Text(frame2,width=80,height=2,font=("Arial",10))
    textchr.grid(row=2,column=0,padx=3,pady=3,sticky="w")
    scrvchr = ttk.Scrollbar(frame2,command=textchr.yview)
    scrvchr.grid(row=2,column=1,sticky="nsew")
    textchr.config(yscrollcommand=scrvchr.set)

    #Goal
    labelgoal = ttk.Label(frame2,text="GOAL", font=("Arial",10))
    labelgoal.grid(row=3,column=0,sticky="w")
    textgoal = tkinter.Text(frame2,width=80,height=3,font=("Arial",10))
    textgoal.grid(row=4,column=0,padx=3,pady=3,sticky="w")
    scrvgoal = ttk.Scrollbar(frame2,command=textgoal.yview)
    scrvgoal.grid(row=4,column=1,sticky="nsew")
    textgoal.config(yscrollcommand=scrvgoal.set)

    #Obstacle
    labelobst = ttk.Label(frame2,text="OBSTACLE", font=("Arial",10))
    labelobst.grid(row=5,column=0,sticky="w")
    textobst = tkinter.Text(frame2,width=80,height=3,font=("Arial",10))
    textobst.grid(row=6,column=0,padx=3,pady=3,sticky="w")
    scrvobst = ttk.Scrollbar(frame2,command=textobst.yview)
    scrvobst.grid(row=6,column=1,sticky="nsew")
    textobst.config(yscrollcommand=scrvobst.set)

    #Resolution
    labelreso = ttk.Label(frame2,text="RESOLUTION", font=("Arial",10))
    labelreso.grid(row=7,column=0,sticky="w")
    textreso = tkinter.Text(frame2,width=80,height=3,font=("Arial",10))
    textreso.grid(row=8,column=0,padx=3,pady=3,sticky="w")
    scrvreso = ttk.Scrollbar(frame2,command=textreso.yview)
    scrvreso.grid(row=8,column=1,sticky="nsew")
    textreso.config(yscrollcommand=scrvreso.set)

    #Buttons
    savebutton = ttk.Button(frame3,text="Save",command=lambda:four_elementSave(textchr.get("1.0",tkinter.END),
                                                                                     textgoal.get("1.0",tkinter.END),
                                                                                     textobst.get("1.0",tkinter.END),
                                                                                     textreso.get("1.0",tkinter.END),
                                                                                     window))
    savebutton.grid(row=0,column=0,padx=3,pady=3)

    cancelbutton = ttk.Button(frame3,text="Cancel",command=lambda:guiMenu(window))
    cancelbutton.grid(row=0,column=1,padx=3,pady=3)

    #Main Loop
    window.mainloop()

#######################################
#3-Act Story Save English
def three_actSave(set,conf,reso,window):
    #Open the file
    try:
        story = io.open("story.txt","w")
    except FileNotFoundError:
        return

    #write the acts in the file
    story.write(f"SETUP: {set}")
    story.write(f"CONFRONTATION: {conf}")
    story.write(f"RESOLUTION: {reso}")

    #Close the file
    story.close()

    #Close the window
    guiMenu(window)

#3-Act Story GUI English
def three_actGui(mainmenu):
    #Close the main menu
    mainmenu.destroy()

    #Main Window 
    window = tkinter.Tk()
    window.title("MLT Storideas")
    window.resizable(False,False)

    #Set Icon
    icon = tkinter.PhotoImage(file="artwork/storideas_icon.png")
    window.iconphoto(False,icon)

    #Title Font
    subtitlefont = Font(size=SUBTITLESIZE,
                    weight="normal")
    
    #MainFrame
    mainframe = ttk.Frame(window)
    mainframe.grid(padx=10,pady=10)

    #Frames
    frame1 = ttk.Frame(mainframe)
    frame1.grid(row=0)

    frame2 = ttk.Frame(mainframe)
    frame2.grid(row=1)

    frame3 = ttk.Frame(mainframe)
    frame3.grid(row=2)

    #Title
    title = ttk.Label(frame1,text="3-ACT STORY", font=subtitlefont)
    title.grid(row=0,column=0,padx=3,pady=3)

    #Setup
    labelset = ttk.Label(frame2,text="SETUP", font=("Arial",10))
    labelset.grid(row=1,column=0,sticky="w")
    textset = tkinter.Text(frame2,width=80,height=5,font=("Arial",10))
    textset.grid(row=2,column=0,padx=3,pady=3,sticky="w")
    scrvset = ttk.Scrollbar(frame2,command=textset.yview)
    scrvset.grid(row=2,column=1,sticky="nsew")
    textset.config(yscrollcommand=scrvset.set)

    #Confrontation
    labelconf = ttk.Label(frame2,text="CONFRONTATION", font=("Arial",10))
    labelconf.grid(row=3,column=0,sticky="w")
    textconf = tkinter.Text(frame2,width=80,height=5,font=("Arial",10))
    textconf.grid(row=4,column=0,padx=3,pady=3,sticky="w")
    scrvconf = ttk.Scrollbar(frame2,command=textconf.yview)
    scrvconf.grid(row=4,column=1,sticky="nsew")
    textconf.config(yscrollcommand=scrvconf.set)

    #Resolution
    labelreso = ttk.Label(frame2,text="RESOLUTION", font=("Arial",10))
    labelreso.grid(row=5,column=0,sticky="w")
    textreso = tkinter.Text(frame2,width=80,height=5,font=("Arial",10))
    textreso.grid(row=6,column=0,padx=3,pady=3,sticky="w")
    scrvreso = ttk.Scrollbar(frame2,command=textreso.yview)
    scrvreso.grid(row=6,column=1,sticky="nsew")
    textreso.config(yscrollcommand=scrvreso.set)

    #Buttons
    savebutton = ttk.Button(frame3,text="Save",command=lambda:three_actSave(textset.get("1.0",tkinter.END),
                                                                                  textconf.get("1.0",tkinter.END),
                                                                                  textreso.get("1.0",tkinter.END),
                                                                                  window))
    savebutton.grid(row=0,column=0,padx=3,pady=3)

    cancelbutton = ttk.Button(frame3,text="Cancel",command=lambda:guiMenu(window))
    cancelbutton.grid(row=0,column=1,padx=3,pady=3)

    #Main Loop
    window.mainloop()

#######################################
#4-Act Story Save English
def four_actSave(set,inct,clmx,reso,window):
    #Open the file
    try:
        story = io.open("story.txt","w")
    except FileNotFoundError:
        return

    #write the acts in the file
    story.write(f"SETUP: {set}")
    story.write(f"INCITING INCIDENT: {inct}")
    story.write(f"CLIMAX: {clmx}")
    story.write(f"RESOLUTION: {reso}")

    #Close the file
    story.close()

    #Close the window
    guiMenu(window)

#4-Act Story GUI English
def four_actGui(mainmenu):
    #Close the main menu
    mainmenu.destroy()
    
    #Main Window 
    window = tkinter.Tk()
    window.title("MLT Storideas")
    window.resizable(False,False)

    #Set Icon
    icon = tkinter.PhotoImage(file="artwork/storideas_icon.png")
    window.iconphoto(False,icon)

    #Title Font
    subtitlefont = Font(size=SUBTITLESIZE,
                    weight="normal")

    #MainFrame
    mainframe = ttk.Frame(window)
    mainframe.grid(padx=10,pady=10)

    #Frames
    frame1 = ttk.Frame(mainframe)
    frame1.grid(row=0)

    frame2 = ttk.Frame(mainframe)
    frame2.grid(row=1)

    frame3 = ttk.Frame(mainframe)
    frame3.grid(row=2)

    #Title
    title = ttk.Label(frame1,text="4-ACT STORY", font=subtitlefont)
    title.grid(row=0,column=0,padx=3,pady=3)

    #Setup
    labelset = ttk.Label(frame2,text="SETUP", font=("Arial",10))
    labelset.grid(row=1,column=0,sticky="w")
    textset = tkinter.Text(frame2,width=80,height=5,font=("Arial",10))
    textset.grid(row=2,column=0,padx=3,pady=3,sticky="w")
    scrvset = ttk.Scrollbar(frame2,command=textset.yview)
    scrvset.grid(row=2,column=1,sticky="nsew")
    textset.config(yscrollcommand=scrvset.set)

    #Confrontation
    labelinct = ttk.Label(frame2,text="INCITING INCIDENT", font=("Arial",10))
    labelinct.grid(row=3,column=0,sticky="w")
    textinct = tkinter.Text(frame2,width=80,height=5,font=("Arial",10))
    textinct.grid(row=4,column=0,padx=3,pady=3,sticky="w")
    scrvinct = ttk.Scrollbar(frame2,command=textinct.yview)
    scrvinct.grid(row=4,column=1,sticky="nsew")
    textinct.config(yscrollcommand=scrvinct.set)

    #Climax
    labelclmx = ttk.Label(frame2,text="CLIMAX", font=("Arial",10))
    labelclmx.grid(row=5,column=0,sticky="w")
    textclmx = tkinter.Text(frame2,width=80,height=5,font=("Arial",10))
    textclmx.grid(row=6,column=0,padx=3,pady=3,sticky="w")
    scrvclmx = ttk.Scrollbar(frame2,command=textclmx.yview)
    scrvclmx.grid(row=6,column=1,sticky="nsew")
    textclmx.config(yscrollcommand=scrvclmx.set)

    #Resolution
    labelreso = ttk.Label(frame2,text="RESOLUTION", font=("Arial",10))
    labelreso.grid(row=7,column=0,sticky="w")
    textreso = tkinter.Text(frame2,width=80,height=5,font=("Arial",10))
    textreso.grid(row=8,column=0,padx=3,pady=3,sticky="w")
    scrvreso = ttk.Scrollbar(frame2,command=textreso.yview)
    scrvreso.grid(row=8,column=1,sticky="nsew")
    textreso.config(yscrollcommand=scrvreso.set)

    #Buttons
    savebutton = ttk.Button(frame3,text="Save",command=lambda:four_actSave(textset.get("1.0",tkinter.END),
                                                                                 textinct.get("1.0",tkinter.END),
                                                                                 textclmx.get("1.0",tkinter.END),
                                                                                 textreso.get("1.0",tkinter.END),
                                                                                 window))
    savebutton.grid(row=0,column=0,padx=3,pady=3)

    cancelbutton = ttk.Button(frame3,text="Cancel",command=lambda:guiMenu(window))
    cancelbutton.grid(row=0,column=1,padx=3,pady=3)

    #Main Loop
    window.mainloop()

#######################################
#7-Act Story Save English
def seven_actSave(acts, window):
    actsnames = ("SETUP","1st PLOT POINT","1st PINCH","MIDPOINT","2nd PINCH","2nd PLOT POINT","RESOLUTION")

    #Open the file
    try:
        story = io.open("story.txt","w")
    except FileNotFoundError:
        return

    #write the acts in the file
    for i in acts:
        story.write(f"{actsnames[acts.index(i)]}: {acts[acts.index(i)].get('1.0',tkinter.END)}")

    #Close the file
    story.close()

    #Close the window
    guiMenu(window)

#7-Act Story GUI English
def seven_actGui(mainmenu):
    #Define the lists and tuples
    actsnames = ("SETUP","1st PLOT POINT","1st PINCH","MIDPOINT","2nd PINCH","2nd PLOT POINT","RESOLUTION")
    labels = []
    texts = []
    scrvs = []

    #Close the main menu
    mainmenu.destroy()

    #Main Window 
    window = tkinter.Tk()
    window.title("MLT Storideas")
    window.resizable(False,False)

    #Set Icon
    icon = tkinter.PhotoImage(file="artwork/storideas_icon.png")
    window.iconphoto(False,icon)

    #Title Font
    subtitlefont = Font(size=SUBTITLESIZE,
                    weight="normal")
    
    #MainFrame
    mainframe = ttk.Frame(window)
    mainframe.grid(padx=10,pady=10)

    #Frames
    frame1 = ttk.Frame(mainframe)
    frame1.grid(row=0)

    frame2 = ttk.Frame(mainframe)
    frame2.grid(row=1)

    frame3 = ttk.Frame(mainframe)
    frame3.grid(row=2)

    #Title
    title = ttk.Label(frame1,text="7-ACT STORY", font=subtitlefont)
    title.grid(row=0,column=0,padx=3,pady=3)

    #7 ACTS
    for i in range(7):
        labels.append(ttk.Label(frame2,text=actsnames[i], font=("Arial",10)))
        labels[i].grid(row=i*2,column=0,sticky="w")
        texts.append(tkinter.Text(frame2,width=80,height=4,font=("Arial",10)))
        texts[i].grid(row=(i*2)+1,column=0,padx=3,pady=3,sticky="w")
        scrvs.append(ttk.Scrollbar(frame2,command=texts[i].yview))
        scrvs[i].grid(row=(i*2)+1,column=1,sticky="nsew")
        texts[i].config(yscrollcommand=scrvs[i].set)


    #Buttons
    savebutton = ttk.Button(frame3,text="Save",command=lambda:seven_actSave(texts, window))
    savebutton.grid(row=0,column=0,padx=3,pady=3)

    cancelbutton = ttk.Button(frame3,text="Cancel",command=lambda:guiMenu(window))
    cancelbutton.grid(row=0,column=1,padx=3,pady=3)

    #Main Loop
    window.mainloop()

#######################################
#N-Act Story Create English
def n_actCreate(parent, num, labels, texts, scrvs):
    #Destroy the previous widgets
    for i in range(len(labels)):
        labels[i].destroy()
    for i in range(len(texts)):
        texts[i].destroy()
    for i in range(len(scrvs)):
        scrvs[i].destroy()

    #Clear the lists
    labels.clear()
    texts.clear()
    scrvs.clear()
    
    #Create the new widgets
    for i in range(num):
        labels.append(ttk.Label(parent,text=f"ACT {i+1}", font=("Arial",10)))
        labels[i].grid(row=(i//2)*2,column=(i%2)*2,padx=0,pady=0)
        texts.append(tkinter.Text(parent,width=80,height=3,font=("Arial",10)))
        texts[i].grid(row=((i//2)*2)+1,column=(i%2)*2,padx=0,pady=0,sticky="w")
        scrvs.append(ttk.Scrollbar(parent,command=texts[i].yview))
        scrvs[i].grid(row=((i//2)*2)+1,column=((i%2)*2)+1,sticky="nsew")
        texts[i].config(yscrollcommand=scrvs[i].set)

#N-Act Story Save English
def n_actSave(acts, size, window):
    #Open the file
    try:
        story = io.open("story.txt","w")
    except FileNotFoundError:
        return

    #write the acts in the file
    for i in range(size):
        story.write(f"- {acts[i].get('1.0',tkinter.END)}")

    #Close the file
    story.close()

    #Close the window
    guiMenu(window)

#N-Act Story GUI English
def n_actGui(mainmenu):
    #Define the lists and tuples
    labels = []
    texts = []
    scrvs = []

    #Close the main menu
    mainmenu.destroy()

    #Main Window 
    window = tkinter.Tk()
    window.title("MLT Storideas")
    window.resizable(False,False)

    #Set Icon
    icon = tkinter.PhotoImage(file="artwork/storideas_icon.png")
    window.iconphoto(False,icon)

    #Title Font
    subtitlefont = Font(size=SUBTITLESIZE,
                    weight="normal")

    #MainFrame
    mainframe = ttk.Frame(window)
    mainframe.grid(padx=10,pady=10)

    #Frames
    frame1 = ttk.Frame(mainframe)
    frame1.grid(row=0)

    frame2 = ttk.Frame(mainframe)
    frame2.grid(row=1)

    frame3 = ttk.Frame(mainframe)
    frame3.grid(row=2)

    #Title
    title = ttk.Label(frame1,text="N-ACT STORY", font=subtitlefont)
    title.grid(row=0,column=0,padx=3,pady=3)

    #Message
    message = ttk.Label(frame1,text="Adjust the acts number and write them down")
    message.grid(row=1,column=0,padx=3,pady=3)

    n_actCreate(frame2, 1, labels, texts, scrvs)

    #Number of Acts Spinbox
    numacts = ttk.Spinbox(frame1,from_=1,to=16,width=20,command=lambda:n_actCreate(frame2,int(numacts.get()),labels,texts,scrvs))
    numacts.set(1)
    numacts.grid(row=2,column=0,padx=3,pady=3)

    #Buttons
    savebutton = ttk.Button(frame3,text="Save",command=lambda:n_actSave(texts,int(numacts.get()),window))
    savebutton.grid(row=0,column=0,padx=3,pady=3)

    cancelbutton = ttk.Button(frame3,text="Cancel",command=lambda:guiMenu(window))
    cancelbutton.grid(row=0,column=1,padx=3,pady=3)

    #Main Loop
    window.mainloop()

#######################################
#Show Idea English
def showIdea():
    #File opening
    try:
        story = io.open("story.txt","r")
    except FileNotFoundError:
        return None

    #Return the idea
    return story.read()

#Copy Idea English
def copyidea(window,button,idea):
    window.clipboard_clear()
    window.clipboard_append(idea)
    window.update()
    button.config(text="Copied!",state="disabled")

#Show Idea GUI English
def showideaGui(mainmenu):
    #Close the main window
    mainmenu.destroy()

    #Main Window 
    window = tkinter.Tk()
    window.title("MLT Storideas")
    window.resizable(False,False)

    #Set Icon
    icon = tkinter.PhotoImage(file="artwork/storideas_icon.png")
    window.iconphoto(False,icon)

    #Title Font
    subtitlefont = Font(size=SUBTITLESIZE,
                    weight="normal")

    #MainFrame
    mainframe = ttk.Frame(window)
    mainframe.grid(padx=10,pady=10)

    #Frames
    frame1 = ttk.Frame(mainframe)
    frame1.grid(row=0)

    frame2 = ttk.Frame(mainframe)
    frame2.grid(row=1)

    frame3 = ttk.Frame(mainframe)
    frame3.grid(row=2)

    #Title
    title = ttk.Label(frame1,text="SHOW IDEA", font=subtitlefont)
    title.grid(row=0,column=0,padx=3,pady=3)

    #Idea
    idea = showIdea()

    #Show Idea
    showidea = tkinter.Text(frame2,width=120,height=20,font=("Arial",10))
    if idea != None:
        showidea.insert("1.0",idea)
    showidea.config(state="disabled")
    showidea.grid(row=0,column=0,padx=3,pady=3)
    scrvidea = ttk.Scrollbar(frame2,command=showidea.yview)
    scrvidea.grid(row=0,column=1,sticky="nsew")
    showidea.config(yscrollcommand=scrvidea.set)

    #Buttons
    okbutton = ttk.Button(frame3,text="OK",command=lambda:guiMenu(window),width=6)
    okbutton.grid(row=0,column=1,padx=3,pady=3)

    copybutton = ttk.Button(frame3,text="Copy to the clipboard",command=lambda:copyidea(window,copybutton,idea),width=20)
    copybutton.grid(row=0,column=2,padx=3,pady=3)

    #Main Loop
    window.mainloop()

#######################################
#Main Menu GUI English
def guiMenu(langmenu = None):
    #Close the language menu
    try:
        langmenu.destroy()
    except AttributeError:
        None

    #Main Window 
    window = tkinter.Tk()
    window.title("MLT Storideas")
    window.resizable(False,False)

    #Set Icon
    icon = tkinter.PhotoImage(file="artwork/storideas_icon.png")
    window.iconphoto(False,icon)

    #Title Font
    titlefont = Font(size=TITLESIZE,
                    weight="normal")

    #MainFrame
    mainframe = ttk.Frame(window)
    mainframe.grid(padx=10,pady=10)

    #Frames
    frame1 = ttk.Frame(mainframe)
    frame1.grid(row=0)

    frame2 = ttk.Frame(mainframe)
    frame2.grid(row=1)

    frame3 = ttk.Frame(mainframe)
    frame3.grid(row=2)

    #Title
    title = ttk.Label(frame1,text="MLT STORIDEAS", font=titlefont)
    title.grid(row=0,column=0,padx=10,pady=10)

    #Buttons
    button1 = ttk.Button(frame2,text="4-Element Story", command=lambda:four_elementGui(window), width=15)
    button1.grid(row=0,column=0,padx=4,pady=4)

    button2 = ttk.Button(frame2,text="3-Act Story", command=lambda:three_actGui(window), width=15)
    button2.grid(row=0,column=1,padx=4,pady=4)

    button3 = ttk.Button(frame2,text="4-Act Story", command=lambda:four_actGui(window), width=15)
    button3.grid(row=0,column=2,padx=4,pady=4)

    button4 = ttk.Button(frame3,text="7-Act Story", command=lambda:seven_actGui(window), width=15)
    button4.grid(row=0,column=0,padx=4,pady=4)

    button5 = ttk.Button(frame3,text="n-Act Story", command=lambda:n_actGui(window), width=15)
    button5.grid(row=0,column=1,padx=4,pady=4)

    button6 = ttk.Button(frame3,text="Show Idea",command=lambda:showideaGui(window), width=15)
    button6.grid(row=0,column=2,padx=4,pady=4)

    window.mainloop()