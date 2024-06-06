import random
print("🤗🤗_____Welcome To Rock Paper Scissor Game_____🤗🤗")
while(True):
    def game(comp,you):
        if(comp==you):
            return 2
        elif(comp=="R"):
            if(you=="P"):
                return 1
            elif(you=="Si"):
                return 0 
        elif(comp=="P"):
            if(you=="Si"):
                return 1
            elif(you=="R"):
                return 0 
        elif(comp=="Si"):
            if(you=="R"):
                return 1
        elif(you=="P"):
                return 0   

    rno=random.randint(1,3)
    if (rno==1):
        comp="R"
    elif(rno==2):
        comp="P"
    elif(rno==3):
        comp="Si"
    print("Computor choosed")
    print("Now your turn")
    you=input("Choose Rock(s),Paper(p),Scissor(si):")
    you=you.capitalize()
    print("Computor choosed:",comp)
    print("You choosed:",you)
    if you=="R":
        a=game(comp,you)
        if(a==2):
            print("The game is tie!")
        elif(a==1):
            print("You won!")
        elif(a==0):
            print("You lost")
    
    elif you=="P":
        a=game(comp,you)
        if(a==2):
            print("The game is tie!")
        elif(a==1):
            print("You won!")
        elif(a==0):
            print("You lost")
    
    elif you=="Si":
        a=game(comp,you)
        if(a==2):
            print("The game is tie!")
        elif(a==1):
            print("You won!")
        elif(a==0):
            print("You lost")
    
    else:
        print("Invalid input(Reminder:-Only choose 'r','p','si')")
        print("Try again!!!😊")

    
    game_info=input("Want to play again(Y/N):").capitalize()

    if game_info=="N":
        print("Thanks for playing game...😀")
        break