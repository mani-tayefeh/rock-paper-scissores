                                                            # mani - tayefeh 🌹
import random 
import pyfiglet
from colorama import Fore

txt = pyfiglet.figlet_format('Rock',font='slant')
txt2 = pyfiglet.figlet_format('Paper',font='slant')
txt3 = pyfiglet.figlet_format('Scissor',font='slant')

print(f'{txt}\n{txt2}\n{txt3}')

butt = ['Rock','Paper','Scissors']

Rock_Paper_Scissor = random.choice(butt)


player = input("🕹Let's Play🕹\nType one of these list (Rock Paper Scissors) : ")

if player == 'Rock' or player == 'Paper' or player == 'Scissors' or player == 'rock' or player == 'paper' or player == 'scissors':
    pass
else:
    print(Fore.RED,"\nPlease do not type any text other than the list",Fore.RESET)
    exit()

   

print(f"\nYou : {player}\nMe : {Rock_Paper_Scissor}")

if player == 'rock' or player == 'Rock':
    if Rock_Paper_Scissor == "Paper":
        print(Fore.RED,'\n😕you lose😕',Fore.RESET)
    elif Rock_Paper_Scissor == 'Rock':
        print(Fore.BLUE,"\n😮You are equal😮",Fore.RESET) 
    elif Rock_Paper_Scissor == 'Scissors':
        print(Fore.GREEN,"\n😊You win😊",Fore.RESET) 

elif player == 'scissors' or player == 'Scissors':
    if Rock_Paper_Scissor == 'Rock':
        print(Fore.RED,"\n😕you lose😕",Fore.RESET)
    elif Rock_Paper_Scissor == 'Scissors':
        print(Fore.BLUE,"\n😮You are equal😮",Fore.RESET) 
    elif Rock_Paper_Scissor == 'Paper':
        print(Fore.GREEN,"\n😊You win😊",Fore.RESET)

elif player == 'paper' or player == 'Paper':
    if Rock_Paper_Scissor == 'Scissors':
        print(Fore.RED,"\n😕you lose😕",Fore.RESET)
    elif Rock_Paper_Scissor == 'Paper':
        print(Fore.BLUE,"\n😮You are equal😮",Fore.RESET) 
    elif Rock_Paper_Scissor == 'Rock':
        print(Fore.GREEN,"\n😊You win😊",Fore.RESET)
