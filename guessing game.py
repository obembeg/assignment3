import random 

print("\tWelcome to 'Guess My Number'!") 
print("\nI'm thinking of a number between 1 and 100.") 
print("Try to guess it in as few attempts as possible.\n") 
# set the initial values 
number = random.randint(1, 100)
guess = int(input("Take a guess: ")) 
attempt = 1

# guessing loop
while guess != number: 
   if guess > number: 
      print("Lower...")
   elif attempt == 3: 
       break 
   else: 
       print("Higher...")
       
   guess = int(input("Take a guess: ")) 
   attempt += 1 
if guess == number: 
   print("You guessed it! The number was", number) 
   print("And it only took you", attempt, "tries!\n") 
input("\n\nPress the enter key to exit.") 
if attempt == 3: 
   print("no") 

