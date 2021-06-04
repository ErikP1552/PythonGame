


print("Welcome to Lost in the World Game")
name = input("What is your name? ")
age = input("What is your age?  ")

'''Verification of Input'''
x = age.isdigit()
while x == False:
  age = input("Your age needs to be a number, What is your age?  ")
  x = age.isdigit()
age_int = int(age)
 
print("Hello", name, " ...Welcome, hope your ready!")

if int(age) >= 18:
  print("You are old enough to play") 
  wants_to_play = input("Can you really handle this game? ")

  if wants_to_play == "yes":
    print("Well what are you waiting for!")

    health = 10
    print("You are starting with", health, "health")
    left_or_right = input("First Life choice ... Left  or Right? ")
    if left_or_right == "left":
      answer = input("Great, you continue down a path and see a street suburb and an alleyway... Do you go to the ally or suburb ")
      if answer == "ally":
        print("The ally was clear, you made it through and some new friends")
        shady = input("You see a shady figure in front. What do you do?? Would you approch or run ")
        if shady == "approch":
          print("It was your friend!, You have won! ")
        else:
          print("It was your friend! Now they are angry at you! You have lost! ")
      else:
        print("You ran into the home owners association.. you lost 5 health.")
        health = health - 5
        print(health, "is the amount of health you have left")
        val = input("You see an old classmate running up! What do you do? run or approch ")
        if val == "run":
          print("You have won and made it home ")
        else: 
          print("You have lost. The old classmate was someone else and was akward ")
    else:
      print("You got robbed... you lose ")
  else:
    print("later... ")

else:
  print("You are actually too young to play ")

print("Game has ended ")





