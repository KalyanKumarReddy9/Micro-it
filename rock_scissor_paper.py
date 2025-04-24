import random
a=["rock","paper","scissor"]
computer=random.choice(a)
computer_score=0
human_score=0
while True:
    player=input("which choice do you want?rock!,paper!,scissor:")
    if player==computer:
        print("The game was draw")
    elif player=="rock":
        if computer=="paper":
            print("you lost the game")
            computer_score+=1
        else:
            print("you won the game")
            human_score+=1
    elif player=="paper":
        if computer=="scissor":
            print("you lost the game")
            computer_score+=1
        else:
            print("you won the game")
            human_score+=1
    elif player=="scissor":
        if computer=="rock":
            print("you lost the game")
            computer_score+=1
        else:
            print("you won the game")
            human_score+=1
    elif player=="stop":
        print("reults of this game:")
        print("computer score is:",computer_score)
        print("human_score is:",human_score)
        break
            
            
            

        
