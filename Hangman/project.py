import random
import sys

WORDLIST_FILENAME= "answerlist.txt"
def game():

  def beginning():
      """Start The Game"""
      while True:
          name= input("please enter your name :-  ")
          if name==" ":
             print("You can't do that!No blank lines")
             continue
          else:
            break
      print("Hello!",name.capitalize())
  beginning()


  def choice():
      while True:
          gamechoice=input("Do You Want To Play?   ").upper()
          if gamechoice == "YES"or gamechoice=="Y":
              break
          elif gamechoice=="NO"or gamechoice=="N":
                sys.exit("Ohk!Have a nice day")
          else:
               print("Please answer only in YES or NO")
               continue
  choice()

  def newfunc():
       with open("answerlist.txt") as f:
          word_list = f.read().rsplit(",")
       random_num = random.randint(0, len(word_list) - 1)
       answer = word_list[random_num]

       print("Let's Start...\n")
       display =[]
       used=[]
       display.extend(answer)
       used.extend(display)
       for i in range(len(display)):
         display[i] = "-"
       print(' '.join(display))
       print()
       
       turn=5
       correct=0
       while turn<=len(answer):
          guess = input("Please Enter Your Guess :- ")
          guess = guess.lower()
          file = []
          file.extend(guess)

          for i in range(len(answer)):
            if guess == answer[i] and guess in used:
                display[i] = guess
                correct = correct+1
                used.remove(guess)

          if guess not in display and guess in file:
                print("Oofs! You Guessed Wrong ")
                turn = turn-1

                if turn == 4:
                   print("|""\n"
                        "|""\n"
                        "|""\n"
                        "|""\n"
                        "|""\n")
                if turn == 3:
                   print("  ""|""\n"
                         "  ""|""\n"
                         "  ""|""\n"
                         "  ""|""\n"
                         "  ""|__")
                if turn==2:
                   print("   ""__________""\n"
                         "  ""|""\n"
                         "  ""|""\n"
                         "  ""|""\n"
                         "  ""|""\n"
                         "  ""|__")
                if turn==1:
                   print("  ""__________""\n"
                         " ""|""          ""|""\n"
                         " ""|""          ""|""\n"
                         " ""|"          "\n"
                         " ""|"          "\n"
                         " ""|__")
                if turn== 0:
                   print("   _________""\n"
                         "  |""         ""|""\n"
                         "  |""         ""|""\n"
                         "  |""        ""DEAD""\n"
                         "  |"              "\n"
                         "  |__")
                   break

          print("You Guessed: ", correct, " Correct  Word ")
          print("More", turn, "turns")

          print(" ".join(display))
          print()

          if display == answer:
              break

       if display == answer:
          print("WOW! You Won")
       else  :
          print("You Guessed: ", correct, " Correct  Word ")
          print("More", turn, "turns")
          print("SORRY! You Loose")
          print ("Game Over!")
  newfunc()
game()

def repeat():
  while True:
    choice=input("Try Again :- ").upper()
    if choice=="YES" or choice=="Y":
        game()
    elif choice == "NO" or choice == "N":
        sys.exit("Bye. See you next time & Have a nice day!")
    else:
        print(" Please answer only in YES or NO")
        continue
repeat()







