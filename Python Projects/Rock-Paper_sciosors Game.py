import random
Qu = ["Rock", "Paper", "Sciosors"]
answer = random.choice(Qu)
print(answer)
Ent = int(input("Enter to Start Game"))
inp = int(input("Choose Your Number Below and Enter:\n 1.Rock\n2.Paper\n3.Scisors\n"))
if inp == answer:
    print("You won the Game")
else:
    print("Loosers")