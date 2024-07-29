import io
from os import system

#######################################
#FUNCTIONS
#ClearEs
def clearEs():
    system("cls")

#ContinueEs
def contEs():
    input("Presiona Enter para continuar...")

#AboutEs
def aboutEs():
    clearEs()
    print("---------ACERCA DE---------")
    print("MLT Storideas")
    print("Versión: 0.1")
    print("Desarrollado en: Python 3.11.9")
    print("MLTVlogs 2024")
    print("---------------------------")
    contEs()

#######################################
#3-Element StoryEs
def four_elementEs():
    clearEs()
    #Abrir el archivo
    try:
        story = io.open("story.txt","w")
    except FileNotFoundError:
        print("Error al abrir el archivo...")
        contEs()
        return
    
    #Leer los elementos
    print("-----HISTORIA DE 4 ELEMENTOS-----")
    chr = input("PERSONAJE: ")
    goal = input("OBJETIVO: ")
    obst = input("OBSTÁCULO: ")
    reso = input("RESOLUCIÓN: ")

    #Escribir los elementos en el archivo
    story.write(f"PERSONAJE: {chr}\n")
    story.write(f"OBJETIVO: {goal}\n")
    story.write(f"OBSTÁCULO: {obst}\n")
    story.write(f"RESOLUCIÓN: {reso}\n")
    contEs()
    
#3-Act StoryEs
def three_actEs():
    clearEs()
    print("-----HISTORIA DE 3 ACTOS-----")
    #Abrir el archivo
    try:
        story = io.open("story.txt","w")
    except FileNotFoundError:
        print("Error al abrir el archivo...")
        contEs()
        return
    
    #Leer los actos
    set = input("INICIO: ")
    conf = input("DESARROLLO: ")
    reso = input("DESENLACE: ")

    #Escribir los actos en el archivo
    story.write(f"INICIO: {set}\n")
    story.write(f"DESARROLLO: {conf}\n")
    story.write(f"DESENLACE: {reso}\n")
    contEs()

#4-Act StoryEs
def four_actEs():
    clearEs()
    print("-----HISTORIA DE 4 ACTOS-----")
    #Open the file
    try:
        story = io.open("story.txt","w")
    except FileNotFoundError:
        print("Error al abrir el archivo...")
        contEs()
        return
    
    #Read the acts
    set = input("INICIO: ")
    inct = input("INCIDENTE INDUCTOR: ")
    clmx = input("CLIMAX: ")
    reso = input("DESENLACE: ")

    #write the acts in the file
    story.write(f"INICIO: {set}\n")
    story.write(f"INCIDENTE INDUCTOR: {inct}\n")
    story.write(f"CLIMAX: {clmx}\n")
    story.write(f"DESENLACE: {reso}\n")
    contEs()

#7-Act StoryEs
def seven_actEs():
    actsnames = ("INICIO","CATALIZADOR","PRIMEROS PASOS","PUNTO MEDIO","PUNTO DE CRISIS","CLIMAX","CONCLUSIÓN")
    acts = []
    clearEs()
    print("-----HISTORIA DE 7 ACTOS-----")

    #Open the file
    try:
        story = io.open("story.txt","w")
    except FileNotFoundError:
        print("Error al abrir el archivo...")
        contEs()
        return
    
    #Read the acts
    for i in range(7):
        acts.append(input(f"{actsnames[i]}: "))

    #write the acts in the file
    for i in range(7):
        story.write(f"{actsnames[i]}: {acts[i]}\n")

    contEs()

#N-Act StoryEs
def n_actEs():
    acts = []
    clearEs()
    print("-----HISTORIA DE N ACTOS-----")

    #Abrir el archivo
    try:
        story = io.open("story.txt","w")
    except FileNotFoundError:
        print("Error al abrir el archivo...")
        contEs()
        return

    #Leer el número de actos
    try:
        num = int(input("Escribe el número de actos: "))
    except ValueError:
        print("Valor inválido, debe ser un número entero.")
        contEs()
        return
    
    #Validar si el número no es menor que 1
    if(num < 1):
        print("Valor inválido, debe tener al menos un acto.")
        contEs()
        return

    #Leer los actos
    for i in range(num):
        acts.append(input(f"ACTO {i+1}: "))

    #Escribir los actos en el archivo
    for i in range(num):
        story.write(f"- {acts[i]}\n")

    contEs()

#Show IdeaEs
def showideaEs():
    clearEs()
    print("-----MOSTRAR LA IDEA-----")
    #File opening
    try:
        story = io.open("story.txt","r")
    except FileNotFoundError:
        print("Error al abrir el archivo...")
        contEs()
        return

    #Show the idea
    print(story.read())
    contEs()

#######################################
#Main MenuEs
def menuEs():
    op = 0
    while op != 8:
        clearEs()
        print("-----MLT STORIDEAS-----")
        print("1) Historia de 3 Elementos")
        print("2) Historia de 3 Actos")
        print("3) Historia de 4 Actos")
        print("4) Historia de 7 Actos")
        print("5) Historia de N Actos")
        print("6) Mostrar la Idea")
        print("7) Acerca de...")
        print("8) Salir")
        try:
            op = int(input("Selecciona una opción (1-8): "))
        except ValueError:
            None
        else:
            if(op == 1):
                four_elementEs()
            if(op == 2):
                three_actEs()
            if(op == 3):
                four_actEs()
            if(op == 4):
                seven_actEs()
            if(op == 5):
                n_actEs()
            if(op == 6):
                showideaEs()
            if(op == 7):
                aboutEs()
            if(op == 8):
                print("Saliendo del programa...")