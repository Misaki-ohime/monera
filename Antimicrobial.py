from pydoc import importfile
from sys import argv
from matplotlib import pyplot as plt
import numpy as np
from tabulate import tabulate



# Ant is a variable that simply states what drugs we are evaluating.
# While we have those statics one (correlated to BrCAST recommendation for S. aureus), it should become modular as the we approach the first stable release.

Ant = ["Benzilpenicillin", "Ceftarolin", "Ciprofloxacin", "Amicacin", "Vancomycin"]

# MO _input is the mother function of the whole script.
# Through these lines we can define the core data of our program, that is, the halo diameter from Kirby-bauer's difusion-disk method.
def MO_input():
        MO_in = input("""Select the microorganism:
                      [1]S. aureus 
                      [2]S. pneumoniae, 
                      [3]E. coli:
                        >> """)
        if MO_in == "1" or "[1]":
            print(f'According to BrCAST, the following drugs will be evaluated for S. aureus: {Ant}')
            global U_Ant
            U_Ant = []
            while True:
                print('Assign the halo diameter according to the previous order, then type "done" when finished')
                Ant_ID = input(">", )
                if Ant_ID == 'done':
                    break
                try:
                    fAnt_ID = float(Ant_ID)
                except:
                    print('Invalid input')
                    continue
                try:
                    U_Ant.append(int(Ant_ID))
                except:
                    U_Ant.append(float(Ant_ID))
            
            Checklist = [[Ant [0],Ant[1], Ant[2], Ant[3], Ant[4]], [U_Ant[0], U_Ant[1], U_Ant[2], U_Ant[3], U_Ant[4]]]
            print(tabulate(Checklist, headers='firstrow'))
            print("All fields are correct?")            
            check_1 = input("Y/N: >")
            if check_1 == "Y" or 'y':
                pass
            else:
                return MO_in(1)
                
            print('Working on data')
            print(f"Be aware that as write on BrCAST, {Ant[4]} cannot be evalutead using DD-methods. For this particular drug, use MIC concentrations.")
            MO_test()
        
        else:
            print('At this version, only [1] S. aureus is avaiable.')

# MO_test is a function that run on booleans expressions evaluating if something is equal or different from a given number.
# In this situation, we evaluate if the previous values, from MO_input, is less than, more than, or equal as a given threshold from BrCAST standards.
## Misaki, please, review al those booleans expressions! 19/08-22

def MO_test():
    global R_Ant0, R_Ant1, R_Ant2, R_Ant3, R_Ant4
   # print(U_Ant[0],':')
    if 26 > U_Ant[0]:
        R_Ant0 = 'S', print("S")
    elif 26 < U_Ant[0]:
        R_Ant0 = 'R', print("R")
    # U_Ant1
   # print(Ant[1],':')
    if 20 < U_Ant[1]:
        R_Ant1 = 'S', print("S")
    elif 17 >= U_Ant[1]:
        R_Ant1 = 'R', print("R")
    elif 17 <= U_Ant[1] <= 19:
        R_Ant1 = 'I', print("I")
    # U_Ant2
  # print(Ant[2],':')
    if 50 < U_Ant[2]:
        R_Ant2 = 'S', print("S")
    elif 21 <= U_Ant[2] <= 49:
        R_Ant2 = 'I', print("I")
    elif 21 > U_Ant[2]:
        R_Ant2 = 'R', print("R")
    # U_Ant3
  #  print(Ant[3],':')
    if 15 < U_Ant[3]:
        R_Ant3 = 'S', print("S")
    elif 15 > U_Ant[3]:
        R_Ant3 = 'R', print("R")
    # U_Ant4
    if 2 >= U_Ant[4]:
        R_Ant4 = 'S', print("S")    
    elif 2 < U_Ant[4]:
        R_Ant4 = 'R', print("R")
    MO_loop()

# This is a simple loop function that assures the possibility to add more samples to this unique session, making it more useful.
def MO_loop():
    
    print("Do you wish to add more samples?")
    answ = input("Y/N:" )
    if answ == "Y":
        return(MO_input)
    elif answ == "N":
        AMR()

# AMR is our final function, responsible for giving a full tabulated visualization from our data. 
def AMR():
    R_MO = R_Ant0 + R_Ant1 + R_Ant2 + R_Ant3 + R_Ant4 
    Resis = R_MO.count('R')
    Sensi = R_MO.count('S')
    Inter = R_MO.count('I')
    Table_end = [['Resistant', 'Sensible', 'Intermediate'], [Resis, Sensi, Inter]]
    Table = tabulate(Table_end, headers='firstrow')
    print(Table)

# MO_input is just beign called here so we can start the script.
MO_input()
