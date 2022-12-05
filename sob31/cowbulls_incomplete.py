import random

def compare_numbers(number, user_guess):
    cowbull=[0,0,0,0]
    for i in range(len(number)):
        if number[i]==user_guess[i]:
            cowbull[i]+=1
        
    return cowbull

playing = True #gotta play the game
number = str(random.randint(1000,9999)) #random 4 digit number
guesses = 0
print(number)

print("Let's play a game of Cowbull!") #explanation
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("For every number that exists in the sequence but is in wrong place, you get a cow. For every one in the right place, you get a bull.")
print("The game ends when you get 4 bulls!")
print("Type exit at any prompt to exit.")

while playing:
    user_guess = input("Give me your best guess!")
    if user_guess == "exit":
        break
    cowbullcount = compare_numbers(number,user_guess)
    guesses+=1
    bullcount=sum(cowbullcount)
    cowcount= len(number)-bullcount

    print("You have "+ str(cowcount) + " cows, and " + str(bullcount) + " bulls.")

    if bullcount==4:
        playing = False
        print("You win the game after " + str(guesses) + " guesses! The number was "+str(number))
        break #redundant exit
    else:
        print("Your guess isn't quite right, try again.")
