import random


answerlist = ['jocky','pycharm','my','python','goodevening']
random.shuffle(answerlist)
answer = list(answerlist[0])


display = []
used = []
display.extend(answer)
used.extend(display)


for i in range(len(display)):
    display[i] = '_'

print(' '.join(display))
print()

turn=5
correct = 0

while turn <= len(answer)+3:
    guess = input("Enter Your Guess: ")
    file=[]
    file.extend(guess)
    guess = guess.lower()



    for i in range(len(answer)):
        if answer[i]== guess and guess in used:
           display[i]=guess
           correct = correct+1
           used.remove(guess)



    if guess not in display:
        turn=turn-1
        print("Oofs! You Guessed Wrong ")


    print ( " You Guessed: ",correct," Correct  Word ")
    file.remove(guess)
    print("More",turn,"turns")

    print(" ".join(display))
    print()

    if display == answer:
        break
if display == answer:
    print("Wow!You won")

else:
  print("Sorry!You loose")




