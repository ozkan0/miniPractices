# @author dono/ozkan0
# tr, bilgisayara karşı taş kağıt makas
# en, rock paper scisssors vs computer
import random
compinput=""
userinput=""
userscore=0
compscore=0
fark=0
def skorinfo():
    print(f'Skor: Siz {userscore} - {compscore} PC')

print("\nSıranızı oynarken Taş için t, Kağıt için k, Makas için m tuşuna basmalısınız.\n")
while fark != 3:
    compinput = random.choice(['t','k','m'])
    userinput = input("Taş, Kağıt, Makas: ")
    #draw statement
    if (userinput =="t" and compinput =="t") or (userinput=="k" and compinput=="k") or (userinput=="m" and compinput=="m"):
        print("Berabere!\n")
        skorinfo()
    #user lost statement
    elif (userinput =="t" and compinput =="k") or (userinput=="k" and compinput=="m") or (userinput=="m" and compinput=="t"):
        print("1 sayı bilgisayara!\n")
        compscore += 1
        skorinfo()
    #user won statement
    elif (userinput =="t" and compinput =="m") or (userinput=="k" and compinput=="t") or (userinput=="m" and compinput=="k"):
        print("1 sayı size!\n")
        userscore += 1
        skorinfo()
    fark=abs(userscore-compscore)
if compscore > userscore:
    print(f'\nBilgisayar {compscore} - {userscore} kazandı!')
elif compscore < userscore:
    print(f'\nSiz {userscore} - {compscore} kazandınız!')