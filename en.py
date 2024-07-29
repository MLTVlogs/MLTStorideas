import io
from os import system

#######################################
#FUNCTIONS
#ClearEn
def clearEn():
    system("cls")

#ContinueEn
def contEn():
    input("Press Enter for Continue...")

#AboutEn
def aboutEn():
    clearEn()
    print("-----------ABOUT-----------")
    print("MLT Storideas")
    print("Version: 0.1")
    print("Developed in: Python 3.11.9")
    print("MLTVlogs 2024")
    print("---------------------------")
    contEn()

#######################################
#3-Element StoryEn
def four_elementEn():
    clearEn()
    #Open the file
    try:
        story = io.open("story.txt","w")
    except FileNotFoundError:
        print("File Opening Error...")
        contEn()
        return
    
    #Read the elements
    print("-----4-ELEMENT STORY-----")
    chr = input("CHARACTER: ")
    goal = input("GOAL: ")
    obst = input("OBSTACLE: ")
    reso = input("RESOLUTION: ")

    #write the elements in the file
    story.write(f"CHARACTER: {chr}\n")
    story.write(f"GOAL: {goal}\n")
    story.write(f"OBSTACLE: {obst}\n")
    story.write(f"RESOLUTION: {reso}\n")
    contEn()
    
#3-Act StoryEn
def three_actEn():
    clearEn()
    print("-----3-ACT STORY-----")
    #Open the file
    try:
        story = io.open("story.txt","w")
    except FileNotFoundError:
        print("File Opening Error...")
        contEn()
        return
    
    #Read the acts
    set = input("SETUP: ")
    conf = input("CONFRONTATION: ")
    reso = input("RESOLUTION: ")

    #write the acts in the file
    story.write(f"SETUP: {set}\n")
    story.write(f"CONFRONTATION: {conf}\n")
    story.write(f"RESOLUTION: {reso}\n")
    contEn()

#4-Act StoryEn
def four_actEn():
    clearEn()
    print("-----4-ACT STORY-----")
    #Open the file
    try:
        story = io.open("story.txt","w")
    except FileNotFoundError:
        print("File Opening Error...")
        contEn()
        return
    
    #Read the acts
    set = input("SETUP: ")
    inct = input("INCITING INCIDENT: ")
    clmx = input("CLIMAX: ")
    reso = input("RESOLUTION: ")

    #write the acts in the file
    story.write(f"SETUP: {set}\n")
    story.write(f"INCITING INCIDENT: {inct}\n")
    story.write(f"CLIMAX: {clmx}\n")
    story.write(f"RESOLUTION: {reso}\n")
    contEn()

#7-Act StoryEn
def seven_actEn():
    actsnames = ("SETUP","1st PLOT POINT","1st PINCH","MIDPOINT","2nd PINCH","2nd PLOT POINT (CLIMAX)","RESOLUTION")
    acts = []
    clearEn()
    print("-----7-ACT STORY-----")

    #Open the file
    try:
        story = io.open("story.txt","w")
    except FileNotFoundError:
        print("File Opening Error...")
        contEn()
        return
    
    #Read the acts
    for i in range(7):
        acts.append(input(f"{actsnames[i]}: "))

    #write the acts in the file
    for i in range(7):
        story.write(f"{actsnames[i]}: {acts[i]}\n")

    contEn()

#N-Act StoryEn
def n_actEn():
    acts = []
    clearEn()
    print("-----N-ACT STORY-----")

    #Open the file
    try:
        story = io.open("story.txt","w")
    except FileNotFoundError:
        print("File Opening Error...")
        contEn()
        return

    #Read the acts number
    try:
        num = int(input("Write the numbers of acts: "))
    except ValueError:
        print("Invalid Value, It Must Be An Integer.")
        contEn()
        return
    
    #Validate if the number isn't minor than 
    if(num < 1):
        print("Invalid Value, Must have At Least One Act.")
        contEn()
        return

    #Read the acts
    for i in range(num):
        acts.append(input(f"ACT {i+1}: "))

    #write the acts in the file
    for i in range(num):
        story.write(f"- {acts[i]}\n")

    contEn()

#Show IdeaEn
def showideaEn():
    clearEn()
    print("-----SHOW IDEA-----")
    #File opening
    try:
        story = io.open("story.txt","r")
    except FileNotFoundError:
        print("File Opening Error...")
        contEn()
        return

    #Show the idea
    print(story.read())
    contEn()

#######################################
#Main MenuEn
def menuEn():
    op = 0
    while op != 8:
        clearEn()
        print("-----MLT STORIDEAS-----")
        print("1) 4-Element Story")
        print("2) 3-Act Story")
        print("3) 4-Act Story")
        print("4) 7-Act Story")
        print("5) n-Act Story")
        print("6) Show Idea")
        print("7) About")
        print("8) Exit")
        try:
            op = int(input("Select an option (1-8): "))
        except ValueError:
            None
        else:
            if(op == 1):
                four_elementEn()
            if(op == 2):
                three_actEn()
            if(op == 3):
                four_actEn()
            if(op == 4):
                seven_actEn()
            if(op == 5):
                n_actEn()
            if(op == 6):
                showideaEn()
            if(op == 7):
                aboutEn()
            if(op == 8):
                print("Exiting the program...")