import random
class Game:
    def Display(Machine_choice,User_choice,userchoice,MachineChoice):
        if Machine_choice==0 and userchoice==1 or Machine_choice==1 and userchoice==0:
            result="Paper"
            if MachineChoice=="Paper":
                print("Computer Wins "+"and his choice is"+ MachineChoice)
            else:
                print("User Wins and his choice is"+ User_choice)
        elif Machine_choice==0 and userchoice==2 or Machine_choice==2 and userchoice==0:
            result="Rock"
            if MachineChoice=="Rock":
                print("Computer Wins and his choice is"+ MachineChoice)
            else:
                print("User Wins and his choice is"+ User_choice)
        elif Machine_choice==2 and userchoice==1 or Machine_choice==1 and userchoice==2:
            result="Scissors"
            if MachineChoice=="Scissors":
                print("Computer Wins and his choice is"+ MachineChoice)
            else:
                print("User Wins and his choice is"+ User_choice)
        else:
            print("Both Choices are Same")
    def  __init__(self,a):
        while a!=0:
            print("Enter Choices\n 0:Rock\n 1:Paper \n 2:Scissors")
            cho=["Rock","Paper","Scissors"]
            Choices=[0,1,2]
            print("it is Computers turn")
            Machine_choice=random.choice(Choices)
            MachineChoice=cho[Machine_choice]
            print(MachineChoice)
            print("It is users turn")
            userchoice=int(input())
            if userchoice>=0 and userchoice<=2:
                User_choice=cho[userchoice]
                print(User_choice)
            Game.Display(Machine_choice,User_choice,userchoice,MachineChoice)
            a=a-1
a=int(input("How many times you want to play"))
obj=Game(a)
