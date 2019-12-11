import random
for i in range(1):
    Qu = ["rock", "paper", "scissors"]
    ran_word = random.choice(Qu)
    print(ran_word)
print("Welcome to The \n Rock Paper Scissors ")
ans = str(input("Choose Your word Below and Enter:\n 1.Rock\n2.Paper\n3.scissors\n")).lower()
while True:
    if ans == ran_word:
        print( "You won the Game")
        break
    else:
        print("Loosers")
        break