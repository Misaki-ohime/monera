from ensurepip import version
from fileinput import close, filename
from pickle import GLOBAL
from sys import argv
from tabulate import tabulate
from matplotlib import numpy

class Main:
    def __init__(self) -> None:
    	version = '0.002'
        print(f"Welcome to Monera version {version}.")
        print("Please, insert the session name:")
        session_name = input(">>")
        global session_file
        session_file = open(session_name, "w")
        Microorganism()
        Antimicrobial()

class Microorganism: # Very simillar to a main_class, atleast considereing our program needs.
    def __init__(self):
       #self.name = mo_name
       #self.standard = mo_standard
       #self.drugs = mo_drugs
       self.mo_name()

    def mo_name(self):
        print("Choose the avaiable species: \n [1] S. aureus \n [2] E. faecium \n [3] E. coli")
        name = str.format(input())
        avaiable_microorganism = '1' or 'S.aureus' or '2' or 'E.faecalis' or '3' or 'E.coli'
        while name != avaiable_microorganism:
            print("This is not a supported microorganism.")
            return self.mo_name()
        if name == avaiable_microorganism:
            self.standards()
           
            
    def standards(self):
        print("Choose the avaiable databases: \n (1) BrCAST \n (2) CLSI")
        std_choice = input()
        if std_choice == '1':
            self.mo_standard = "BrCAST"
        elif std_choice == '2':
            self.mo_standard = "CLSI"
        else:
            while std_choice != '1' or '2':
                print('Error. Invalid argument.')
                return std_choice
        self.drug()
        
    def drug(self):
        print('In this version, you have a limited variety of drugs to choose from.')
        global drugs
        drugs_input = input("Select between: \n [1] Benzilpenicillin, Ceftarolin, Ciprofloxacin, Amicacin, Vancomycin \n >>" )
        if drugs_input == '1':
            drugs = ['Benzilpenicillin', 'Ceftarolin', 'Ciprofloxacin', 'Amicacin', 'Vancomycin']
        else:
            print("Invalid input. Please, choose between the previous option.")
            return self.drug()

class Antimicrobial: #The core input repository.
    def __init__(self):
        self.mo_antimicrobial()
    
    
    def mo_antimicrobial(self):
        Sample_number = int(input(">>"))
        global U_Ant
        U_Ant = []
        i = 0
        while i < Sample_number:
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
            i = i + 1    
        global Checklist
                
	
	def MO_test():
		global R_Ant
	    R_Ant = []
	   # print(U_Ant[0],':')
	    if 26 > U_Ant[0]:
		R_Ant = 'S'
	    elif 26 < U_Ant[0]:
		R_Ant0 = 'R'
	    # U_Ant1
	   # print(Ant[1],':')
	    if 20 < U_Ant[1]:
		R_Ant = 'S'
	    elif 17 >= U_Ant[1]:
		R_Ant = 'R'
	    elif 17 <= U_Ant[1] <= 19:
		R_Ant = 'I'
	    # U_Ant2
	  # print(Ant[2],':')
	    if 50 < U_Ant[2]:
		R_Ant = 'S'
	    elif 21 <= U_Ant[2] <= 49:
		R_Ant = 'I'
	    elif 21 > U_Ant[2]:
		R_Ant = 'R'
	    # U_Ant3
	  #  print(Ant[3],':')
	    if 15 < U_Ant[3]:
		R_Ant = 'S'
	    elif 15 > U_Ant[3]:
		R_Ant = 'R'
	    # U_Ant4
	    if 2 >= U_Ant[4]:
		R_Ant = 'S'    
	    elif 2 < U_Ant[4]:
		R_Ant = 'R'
    AMR()
        
def AMR():
	Resis = R_Ant.count('R')
	Sensi = R_Ant.count('S')
	Inter = R_Ant.count('I')
	Checklist = np.darray([drugs, U_Ant], np.int32)
	Ratio = np.darray(['R', 'I', 'S'], [Resis, Sensi, Inter]
	session_file.write("\n")
        session_file.write(str(Checklist, Ratio))
        print(tabulate(Checklist, headers='firstrow'))
        print(tabulate(Ratio, headers='firstrow')
        print("Do you wish to add more samples?")            
        check_1 = str(input("Y/N: >"))
        if check_1 == "N":
            session_file.close()
        elif check_1 == "Y":
            return self.mo_antimicrobial()
        #if check_2 == "Y":
            return self.mo_antimicrobial()
       # else:  
        print('Working on data')
        print("Be aware that as write on BrCAST, Vancomycin cannot be evalutead using DD-methods. For this particular drug, use MIC concentrations.")
        End()
        
class End():
    def __init__(self) -> None:
        print("Data sucessfully acquired")
        exit

Main()
