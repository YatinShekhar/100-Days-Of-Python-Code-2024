# Day 4 - Randomisation and Python List ⚡

## Topics 📃
- **Random Module**
- **Lists**

# Auditorium Exercise 🌌

## **13. Heads or Tails**

Write a virtual coin toss program that tells a random heads or tails.

```python
import random  
random_int = random.randint(0,1)

if random_int == 0:
  print("Tails")
else:
  print("Heads")
```

## **14. Banker Roulette**

Write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

```python
import random
names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
random_int = random.randint(0, len(names) - 1)
print(f"{names[random_int]} is going to buy the meal today!")
```

## **15. Treasure Map**

Write a program that will mark a spot on the map with an X.

```python
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]

map = [line1, line2, line3]

print("Hiding your treasure! X marks the spot.")
position = input()

row = ['1', '2', '3']
column = ['A', 'B', 'C']

row_index = row.index(position[1])
column_index = column.index(position[0])

map[row_index][column_index] = 'X'

print(f"{line1}\n{line2}\n{line3}")
```

# Project - Rock Paper Scissors 🚀

```python
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

random_num = random.randint(0,2)
my_number = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if my_number == 0:
    print(rock)
elif my_number == 1:
    print(paper)
elif my_number == 2:
    print(scissors)
else:
    print("Invalid number")

if my_number == random_num:
    print("It's a draw")
elif my_number > random_num:
    if my_number == 2 and random_num == 0:
        print("You lose")
    elif my_number >= 3:
        print("Invalid number. You lose")
    else:
        print("You win")
elif my_number < random_num:
    if my_number == 0 and random_num == 2:
        print("You win")
    elif my_number < 0:
        print("Invalid number. You lose")
    else:
        print("You lose")



print("Computer chose:")

if random_num == 0:
    print(rock)
elif random_num == 1:
    print(paper)
else:
    print(scissors)

