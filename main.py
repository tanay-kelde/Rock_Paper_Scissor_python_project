'''rock vs paper = paper win
rock vs scisor = rock win
paper vs scissor = scissor win '''

import random
list = ["rock", "scissor", "paper"]

while True:
    computercount=0
    usercount=0
    userchoice = int(input('''
Game start ....
1 yes
2 no | Exit

        '''))

    if userchoice == 1:
        for a in range(1,6):
            userinput=int(input('''
1 rock
2 scissor
3 paper
            '''))
            if userinput==1:
               userchoice ="rock"
            elif userinput==2:
               userchoice ="scissor"
            elif userinput==3:
                userchoice="paper"
            computerchoice=random.choice(list)
            if computerchoice==userchoice:
               print("computer value",computerchoice)
               print("user value",userchoice)
               print("Game draw")
               usercount=usercount+1
               computercount=computercount+1
            elif(userchoice == "rock" and computerchoice == "scissor") or (userchoice == "paper" and computerchoice == "rock") or (userchoice == "scissor" and computerchoice == "paper"):
               print("computer value", computerchoice)
               print("user value", userchoice)
               print("You win")
               usercount=usercount+1
            else:
               print("computer value", computerchoice)
               print("user value", userchoice)
               print("Computer win")
               computercount=computercount+1
        if usercount==computercount:
           print("Final Game Draw.....")
           print("User score",usercount)
           print("computer score",computercount)
        elif usercount>computercount:
           print("Final You Win the Game.....")
           print("User score",usercount)
           print("computer score",computercount)
        else:
           print("Final Computer Win the Game.....")
           print("User score",usercount)
           print("computer score",computercount)
    else:
        break
