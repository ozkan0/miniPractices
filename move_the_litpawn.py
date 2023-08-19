# @author dono/ozkan0
# en, a mini game named the lit pawn game I just made up
#TODO: add a timer to the game set to 10 seconds per move
#TODO: make the source code more readable
#TODO: continue making error handling for new features

import random
import time
def move_the_litpawn():
    print("Welcome to the move the lit pawn game! You should move the pawn properly to win the game. You should imagine the chess board and its coordinates.\nThe pawn can move only one step forward (all directions) and can't step where it was earlier. You can move the pawn by typing the coordinates of the pawn.\nThe coordinates should be like this: 'a1' or 'h8'. To win this, you should make 10 succesful moves.\nGood luck!")
    start = int(input("Type 1 to start the game: "))
    if start == 1:
        move=0
        over=False
        coordinates_converted = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8}
        used_coordinates = []
        pawn_xy = random.choice("abcdefgh") + str(random.randint(1,8))
        used_coordinates.append(pawn_xy)
        while move < 10 and not over:
            pawn_x = coordinates_converted[pawn_xy[0]]
            pawn_y = int(pawn_xy[1])
            print("The pawn is at: __"+pawn_xy+"__\n")
            pawn_xy_user = input("Type the coordinates to move the pawn: ")
            #error handling
            try:
                pawn_usery_reloaded = int(pawn_xy_user[1])
            except:
                over = True
            else:
                pass
            try:
                pawn_userx_reloaded = coordinates_converted[pawn_xy_user[0]]
            except:
                over = True
            else:
                pass
            if pawn_usery_reloaded > 8 or pawn_usery_reloaded < 1:
                over = True
                print("Not proper move! Game over")
                break
            #error handling end
            if pawn_xy_user == pawn_xy:
                print("You can't type the same coordinates!\n")
            
            #checking if the move is proper
            elif (pawn_x==pawn_userx_reloaded and (pawn_y+1==pawn_usery_reloaded or pawn_y-1==pawn_usery_reloaded)) or \
                (pawn_x+1==pawn_userx_reloaded and (pawn_y==pawn_usery_reloaded or pawn_y-1==pawn_usery_reloaded or pawn_y+1==pawn_usery_reloaded)) or \
                (pawn_x-1==pawn_userx_reloaded and (pawn_y==pawn_usery_reloaded or pawn_y-1==pawn_usery_reloaded or pawn_y+1==pawn_usery_reloaded)):
                same=False
                for i in used_coordinates:
                    if i == pawn_xy_user:
                        print("You attempted to move the pawn where it was earlier! Your pawn just burned")
                        same = True
                        over = True
                if same == False:
                    move += 1
                    print(f"\n\n\nYou achieved your {move}. move.")
                    pawn_xy = pawn_xy_user 
                    used_coordinates.append(pawn_xy_user)
            
            #instant game over block
            else:
                print("Not proper move! Game over")
                over = True
        if move == 10:
            print("You won the game!")
move_the_litpawn()