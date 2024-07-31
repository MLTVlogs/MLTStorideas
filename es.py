import io
import tkinter
import tkinter.ttk as ttk
from tkinter import font as tkfont
from os import system

#######################################
#FUNCTIONS
#######################################
#4-Element Story Save Spanish
def four_elementSaveEs(chr,goal,obst,reso,window):
    #Open the file
    try:
        story = io.open("story.txt","w")
    except FileNotFoundError:
        return

    #write the elements in the file
    story.write(f"PERSONAJE: {chr}")
    story.write(f"OBJETIVO: {goal}")
    story.write(f"OBSTÁCULO: {obst}")
    story.write(f"RESOLUCIÓN: {reso}")

    #Close the file
    story.close()

    #Close the window
    window.destroy()

#4-Element Story GUI Spanish
def four_elementGuiEs(mainmenu):
    #Close the main menu
    mainmenu.destroy()

    #Main Window 
    window = tkinter.Tk()
    window.title("MLT Storideas")
    window.resizable(False,False)

    #Theme
    style = ttk.Style()

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
    title = ttk.Label(frame1,text="HISTORIA DE 4 ELEMENTOS", font=("Arial",16,"bold"))
    title.grid(row=0,column=0,padx=3,pady=3)

    #Character
    labelchr = ttk.Label(frame2,text="PERSONAJE", font=("Arial",10))
    labelchr.grid(row=1,column=0,sticky="w")
    textchr = tkinter.Text(frame2,width=80,height=2,font=("Arial",10))
    textchr.grid(row=2,column=0,padx=3,pady=3,sticky="w")
    scrvchr = ttk.Scrollbar(frame2,command=textchr.yview)
    scrvchr.grid(row=2,column=1,sticky="nsew")
    textchr.config(yscrollcommand=scrvchr.set)

    #Goal
    labelgoal = ttk.Label(frame2,text="OBJETIVO", font=("Arial",10))
    labelgoal.grid(row=3,column=0,sticky="w")
    textgoal = tkinter.Text(frame2,width=80,height=3,font=("Arial",10))
    textgoal.grid(row=4,column=0,padx=3,pady=3,sticky="w")
    scrvgoal = ttk.Scrollbar(frame2,command=textgoal.yview)
    scrvgoal.grid(row=4,column=1,sticky="nsew")
    textgoal.config(yscrollcommand=scrvgoal.set)

    #Obstacle
    labelobst = ttk.Label(frame2,text="OBSTÁCULO", font=("Arial",10))
    labelobst.grid(row=5,column=0,sticky="w")
    textobst = tkinter.Text(frame2,width=80,height=3,font=("Arial",10))
    textobst.grid(row=6,column=0,padx=3,pady=3,sticky="w")
    scrvobst = ttk.Scrollbar(frame2,command=textobst.yview)
    scrvobst.grid(row=6,column=1,sticky="nsew")
    textobst.config(yscrollcommand=scrvobst.set)

    #Resolution
    labelreso = ttk.Label(frame2,text="RESOLUCIÓN", font=("Arial",10))
    labelreso.grid(row=7,column=0,sticky="w")
    textreso = tkinter.Text(frame2,width=80,height=3,font=("Arial",10))
    textreso.grid(row=8,column=0,padx=3,pady=3,sticky="w")
    scrvreso = ttk.Scrollbar(frame2,command=textreso.yview)
    scrvreso.grid(row=8,column=1,sticky="nsew")
    textreso.config(yscrollcommand=scrvreso.set)

    #Buttons
    savebutton = ttk.Button(frame3,text="Guardar",command=lambda:four_elementSaveEs(textchr.get("1.0",tkinter.END),
                                                                                     textgoal.get("1.0",tkinter.END),
                                                                                     textobst.get("1.0",tkinter.END),
                                                                                     textreso.get("1.0",tkinter.END),
                                                                                     window))
    savebutton.grid(row=0,column=0,padx=3,pady=3)

    cancelbutton = ttk.Button(frame3,text="Cancelar",command=window.destroy)
    cancelbutton.grid(row=0,column=1,padx=3,pady=3)

    #Main Loop
    window.mainloop()

    #Open the main menu
    guiMenuEs()

#######################################
#3-Act Story Save Spanish
def three_actSaveEs(set,conf,reso,window):
    #Open the file
    try:
        story = io.open("story.txt","w")
    except FileNotFoundError:
        return

    #write the acts in the file
    story.write(f"INICIO: {set}")
    story.write(f"DESARROLLO: {conf}")
    story.write(f"DESENLACE: {reso}")

    #Close the file
    story.close()

    #Close the window
    window.destroy()

#3-Act Story GUI Spanish
def three_actGuiEs(mainmenu):
    #Close the main menu
    mainmenu.destroy()

    #Main Window 
    window = tkinter.Tk()
    window.title("MLT Storideas")
    window.resizable(False,False)

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
    title = ttk.Label(frame1,text="HISTORIA DE 3 ACTOS", font=("Arial",16,"bold"))
    title.grid(row=0,column=0,padx=3,pady=3)

    #Setup
    labelset = ttk.Label(frame2,text="INICIO", font=("Arial",10))
    labelset.grid(row=1,column=0,sticky="w")
    textset = tkinter.Text(frame2,width=80,height=5,font=("Arial",10))
    textset.grid(row=2,column=0,padx=3,pady=3,sticky="w")
    scrvset = ttk.Scrollbar(frame2,command=textset.yview)
    scrvset.grid(row=2,column=1,sticky="nsew")
    textset.config(yscrollcommand=scrvset.set)

    #Confrontation
    labelconf = ttk.Label(frame2,text="DESARROLLO", font=("Arial",10))
    labelconf.grid(row=3,column=0,sticky="w")
    textconf = tkinter.Text(frame2,width=80,height=5,font=("Arial",10))
    textconf.grid(row=4,column=0,padx=3,pady=3,sticky="w")
    scrvconf = ttk.Scrollbar(frame2,command=textconf.yview)
    scrvconf.grid(row=4,column=1,sticky="nsew")
    textconf.config(yscrollcommand=scrvconf.set)

    #Resolution
    labelreso = ttk.Label(frame2,text="DESENLACE", font=("Arial",10))
    labelreso.grid(row=5,column=0,sticky="w")
    textreso = tkinter.Text(frame2,width=80,height=5,font=("Arial",10))
    textreso.grid(row=6,column=0,padx=3,pady=3,sticky="w")
    scrvreso = ttk.Scrollbar(frame2,command=textreso.yview)
    scrvreso.grid(row=6,column=1,sticky="nsew")
    textreso.config(yscrollcommand=scrvreso.set)

    #Buttons
    savebutton = ttk.Button(frame3,text="Guardar",command=lambda:three_actSaveEs(textset.get("1.0",tkinter.END),
                                                                                  textconf.get("1.0",tkinter.END),
                                                                                  textreso.get("1.0",tkinter.END),
                                                                                  window))
    savebutton.grid(row=0,column=0,padx=3,pady=3)

    cancelbutton = ttk.Button(frame3,text="Cancelar",command=window.destroy)
    cancelbutton.grid(row=0,column=1,padx=3,pady=3)

    #Main Loop
    window.mainloop()

    #Open the main menu
    guiMenuEs()

#######################################
#4-Act Story Save Spanish
def four_actSaveEs(set,inct,clmx,reso,window):
    #Open the file
    try:
        story = io.open("story.txt","w")
    except FileNotFoundError:
        return

    #write the acts in the file
    story.write(f"INICIO: {set}")
    story.write(f"INCIDENTE INDUCTOR: {inct}")
    story.write(f"CLÍMAX: {clmx}")
    story.write(f"DESENLACE: {reso}")

    #Close the file
    story.close()

    #Close the window
    window.destroy()

#4-Act Story GUI Spanish
def four_actGuiEs(mainmenu):
    #Close the main menu
    mainmenu.destroy()

    #Main Window 
    window = tkinter.Tk()
    window.title("MLT Storideas")
    window.resizable(False,False)

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
    title = ttk.Label(frame1,text="HISTORIA DE 4 ACTOS", font=("Arial",16,"bold"))
    title.grid(row=0,column=0,padx=3,pady=3)

    #Setup
    labelset = ttk.Label(frame2,text="INICIO", font=("Arial",10))
    labelset.grid(row=1,column=0,sticky="w")
    textset = tkinter.Text(frame2,width=80,height=5,font=("Arial",10))
    textset.grid(row=2,column=0,padx=3,pady=3,sticky="w")
    scrvset = ttk.Scrollbar(frame2,command=textset.yview)
    scrvset.grid(row=2,column=1,sticky="nsew")
    textset.config(yscrollcommand=scrvset.set)

    #Inciting Incident
    labelinct = ttk.Label(frame2,text="INCIDENTE INDUCTOR", font=("Arial",10))
    labelinct.grid(row=3,column=0,sticky="w")
    textinct = tkinter.Text(frame2,width=80,height=5,font=("Arial",10))
    textinct.grid(row=4,column=0,padx=3,pady=3,sticky="w")
    scrvinct = ttk.Scrollbar(frame2,command=textinct.yview)
    scrvinct.grid(row=4,column=1,sticky="nsew")
    textinct.config(yscrollcommand=scrvinct.set)

    #Climax
    labelclmx = ttk.Label(frame2,text="CLÍMAX", font=("Arial",10))
    labelclmx.grid(row=5,column=0,sticky="w")
    textclmx = tkinter.Text(frame2,width=80,height=5,font=("Arial",10))
    textclmx.grid(row=6,column=0,padx=3,pady=3,sticky="w")
    scrvclmx = ttk.Scrollbar(frame2,command=textclmx.yview)
    scrvclmx.grid(row=6,column=1,sticky="nsew")
    textclmx.config(yscrollcommand=scrvclmx.set)

    #Resolution
    labelreso = ttk.Label(frame2,text="DESENLACE", font=("Arial",10))
    labelreso.grid(row=7,column=0,sticky="w")
    textreso = tkinter.Text(frame2,width=80,height=5,font=("Arial",10))
    textreso.grid(row=8,column=0,padx=3,pady=3,sticky="w")
    scrvreso = ttk.Scrollbar(frame2,command=textreso.yview)
    scrvreso.grid(row=8,column=1,sticky="nsew")
    textreso.config(yscrollcommand=scrvreso.set)

    #Buttons
    savebutton = ttk.Button(frame3,text="Guardar",command=lambda:four_actSaveEs(textset.get("1.0",tkinter.END),
                                                                                 textinct.get("1.0",tkinter.END),
                                                                                 textclmx.get("1.0",tkinter.END),
                                                                                 textreso.get("1.0",tkinter.END),
                                                                                 window))
    savebutton.grid(row=0,column=0,padx=3,pady=3)

    cancelbutton = ttk.Button(frame3,text="Cancelar",command=window.destroy)
    cancelbutton.grid(row=0,column=1,padx=3,pady=3)

    #Main Loop
    window.mainloop()

    #Open the main menu
    guiMenuEs()

#######################################
#7-Act Story Save Spanish
def seven_actSaveEs(acts, window):
    actsnames = ("INICIO","1er PUNTO DE GIRO","1er OBSTÁCULO","PUNTO MEDIO","2do OBSTÁCULO","2do PUNTO DE GIRO","RESOLUCIÓN")

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
    window.destroy()

#7-Act Story GUI Spanish
def seven_actGuiEs(mainmenu):
    #Define the lists and tuples
    actsnames = ("INICIO","1er PUNTO DE GIRO","1er OBSTÁCULO","PUNTO MEDIO","2do OBSTÁCULO","2do PUNTO DE GIRO","RESOLUCIÓN")
    labels = []
    texts = []
    scrvs = []

    #Close the main menu
    mainmenu.destroy()

    #Main Window 
    window = tkinter.Tk()
    window.title("MLT Storideas")
    window.resizable(False,False)

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
    title = ttk.Label(frame1,text="HISTORIA DE 7 ACTOS", font=("Arial",16,"bold"))
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
    savebutton = ttk.Button(frame3,text="Guardar",command=lambda:seven_actSaveEs(texts, window))
    savebutton.grid(row=0,column=0,padx=3,pady=3)

    cancelbutton = ttk.Button(frame3,text="Cancelar",command=window.destroy)
    cancelbutton.grid(row=0,column=1,padx=3,pady=3)

    #Main Loop
    window.mainloop()

    #Open the main menu
    guiMenuEs()

#######################################
#N-Act Story Create Spanish
def n_actCreateEs(parent, num, labels, texts, scrvs):
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
        labels.append(ttk.Label(parent,text=f"ACTO {i+1}", font=("Arial",10)))
        labels[i].grid(row=((i*2)%num),column=(((i*2)//num)*2),sticky="w",padx=0,pady=0)
        texts.append(tkinter.Text(parent,width=80,height=3,font=("Arial",10)))
        texts[i].grid(row=((i*2)%num)+1,column=(((i*2)//num)*2),padx=0,pady=0,sticky="w")
        scrvs.append(ttk.Scrollbar(parent,command=texts[i].yview))
        scrvs[i].grid(row=((i*2)%num)+1,column=(((i*2)//num)*2)+1,sticky="nsew")
        texts[i].config(yscrollcommand=scrvs[i].set)

#N-Act Story Save Spanish
def n_actSaveEs(acts, size, window):
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
    window.destroy()

#N-Act Story GUI Spanish
def n_actGuiEs(mainmenu):
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
    title = ttk.Label(frame1,text="HISTORIA DE N ACTOS", font=("Arial",16,"bold"))
    title.grid(row=0,column=0,padx=3,pady=3)

    #Message
    message = ttk.Label(frame1,text="Ajusta el número de actos y escríbelos")
    message.grid(row=1,column=0,padx=3,pady=3)

    n_actCreateEs(frame2, 1, labels, texts, scrvs)

    #Number of Acts Spinbox
    numacts = ttk.Spinbox(frame1,from_=1,to=12,width=20,command=lambda:n_actCreateEs(frame2,int(numacts.get()),labels,texts,scrvs))
    numacts.grid(row=2,column=0,padx=3,pady=3)

    #Buttons
    savebutton = ttk.Button(frame3,text="Guardar",command=lambda:n_actSaveEs(texts,int(numacts.get()),window))
    savebutton.grid(row=0,column=0,padx=3,pady=3)

    cancelbutton = ttk.Button(frame3,text="Cancelar",command=window.destroy)
    cancelbutton.grid(row=0,column=1,padx=3,pady=3)

    #Main Loop
    window.mainloop()

    #Open the main menu
    guiMenuEs()

#######################################
#Show Idea Spanish
def showideaEs():
    #File opening
    try:
        story = io.open("story.txt","r")
    except FileNotFoundError:
        return

    #Return the idea
    return story.read()

#Copy Idea Spanish
def copyideaEs(window,button,idea):
    window.clipboard_clear()
    window.clipboard_append(idea)
    window.update()
    button.config(text="Copiado!",state="disabled")

#Show Idea GUI English
def showideaGuiEs(mainmenu):
    #Close the main window
    mainmenu.destroy()

    #Main Window 
    window = tkinter.Tk()
    window.title("MLT Storideas")
    window.resizable(False,False)

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
    title = ttk.Label(frame1,text="MOSTRAR LA IDEA", font=("Arial",16,"bold"))
    title.grid(row=0,column=0,padx=3,pady=3)

    #Idea
    idea = showideaEs()

    #Show Idea
    showidea = tkinter.Text(frame2,width=120,height=20,font=("Arial",10))
    showidea.insert("1.0",idea)
    showidea.config(state="disabled")
    showidea.grid(row=0,column=0,padx=3,pady=3)
    scrvidea = ttk.Scrollbar(frame2,command=showidea.yview)
    scrvidea.grid(row=0,column=1,sticky="nsew")
    showidea.config(yscrollcommand=scrvidea.set)

    #Buttons
    okbutton = ttk.Button(frame3,text="Aceptar",command=window.destroy)
    okbutton.grid(row=0,column=1,padx=3,pady=3)

    copybutton = ttk.Button(frame3,text="Copiar en el Portapapeles",command=lambda:copyideaEs(window,copybutton,idea))
    copybutton.grid(row=0,column=2,padx=3,pady=3)

    #Main Loop
    window.mainloop()

    #Open the main window
    guiMenuEs()  

#######################################
#Main Menu GUI Spanish
def guiMenuEs(langmenu = None):
    #Close the language menu
    try:
        langmenu.destroy()
    except AttributeError:
        None

    #Ventana principal
    window = tkinter.Tk()
    window.title("MLT Storideas")
    window.resizable(False,False)

    #Marco principal
    mainframe = ttk.Frame(window)
    mainframe.grid(padx=10,pady=10)

    #Marcos
    frame1 = ttk.Frame(mainframe)
    frame1.grid(row=0)

    frame2 = ttk.Frame(mainframe)
    frame2.grid(row=1)

    frame3 = ttk.Frame(mainframe)
    frame3.grid(row=2)

    #Título
    title = ttk.Label(frame1,text="MLT STORIDEAS", font=("Arial",16,"bold"))
    title.grid(row=0,column=0,padx=3,pady=3)

    #Mensaje
    message = ttk.Label(frame1,text="Selecciona una opción")
    message.grid(row=2,column=0,padx=3,pady=3)

    #Botones
    button1 = ttk.Button(frame2,text="Historia de 4 Elementos", command=lambda:four_elementGuiEs(window))
    button1.grid(row=0,column=0,padx=3,pady=3)

    button2 = ttk.Button(frame2,text="Historia de 3 Actos", command=lambda:three_actGuiEs(window))
    button2.grid(row=0,column=1,padx=3,pady=3)

    button3 = ttk.Button(frame2,text="Historia de 4 Actos", command=lambda:four_actGuiEs(window))
    button3.grid(row=0,column=2,padx=3,pady=3)

    button4 = ttk.Button(frame3,text="Historia de 7 Actos", command=lambda:seven_actGuiEs(window))
    button4.grid(row=0,column=0,padx=3,pady=3)

    button5 = ttk.Button(frame3,text="Historia de n Actos", command=lambda:n_actGuiEs(window))
    button5.grid(row=0,column=1,padx=3,pady=3)

    button6 = ttk.Button(frame3,text="Mostrar la Idea",command=lambda:showideaGuiEs(window))
    button6.grid(row=0,column=2,padx=3,pady=3)

    window.mainloop()