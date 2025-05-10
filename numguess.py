import random
def Replay():
    randnum=random.randint(1,100)
    attempts=0
    while(True):
        guessnum=input("guess the number or quit(Q): ")
        if(guessnum=='Q'):
            break
        guessnum=int(guessnum)
        attempts=attempts+1 
        if(attempts>10):
            print("you have used all your chances! play again")
            break
        if(guessnum==randnum):
            print("success! correct guess :)")
            break
        elif(guessnum<randnum):
            print("too small, take a bigger guess")
        else:
            print("too big, take a smaller guess")
    if(guessnum==randnum):
        print(f"you have guessed in {attempts} attempts")     
    print("====GAME OVER====")
    again = input("Do you want to play again? (Y/N): ")
    if again.upper()== 'Y':
        Replay()
    else:
        print("exit")

Replay()