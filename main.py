# -------------------- Password Generator -------------------- #
# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#   print(fruit)
#   print(fruit + " Pie")
# print(fruits)
# -------------------- Sum() and Len() ------------------- #
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# totalHeight = 0
# for heights in student_heights: #function to find the total height instead of using SUM()
#     totalHeight = totalHeight + heights
# #print(totalHeight)

# totalStudents = 0
# for students in student_heights: #function to find the total number of students instead of using LEN()
#     totalStudents = totalStudents + 1
# #print(totalStudents)

# average = totalHeight / totalStudents #calculating the average height
# print(round(average)) #rounding up the average and printing it

# -------------------- Max() ------------------- #
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)

# maxScore = 0
# for score in student_scores: #function to find the highest number in a list without using MAX()
#     if score > maxScore:
#         maxScore = score
# print(f"The highest score in the class is: {maxScore}")

# -------------------- Adding numbers in RANGE() -------------------- #
# for number in range(1, 21, 3): #prints from number 1 to 20 skipping adding 3 to the previous number
#   print(number)

# total = 0
# for number in range(1, 101):
#   total += number
# print(total)

# # -------------------- Adding even numbers in RANGE() -------------------- #

# total1 = 0
# for number in range(1, 101): #using REST to set the even numbers
#     if number % 2 == 0:
#         total1 += number
# print(total1)

# total2 = 0
# for number in range(2, 101, 2): #setting the parameter in the RANGE(*, *, _)
#     total2 += number
# print(total2)

# # -------------------- FizzBuzz -------------------- #

# for number in range(1, 101):
#     if(number % 3 == 0) and (number % 5 == 0):
#         print("FizzBuzz")
#     elif (number % 3 == 0):
#         print("Fizz")
#     elif (number % 5 == 0):
#         print("Buzz")
#     else:
#         print(number)

# -------------------------------------------------- Password Gen -------------------------------------------------- #

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
for character in range(1, nr_letters + 1):
  # randomChar = random.choice(letters)
  # password = password + randomChar
  password += random.choice(letters)

for character in range(1, nr_symbols + 1):
  # randomChar = random.choice(symbols)
  # password = password + randomChar
  password += random.choice(symbols)
  
for character in range(1, nr_numbers + 1):
  # randomChar = random.choice(numbers)
  # password = password + randomChar
  password += random.choice(numbers)

print("Your password is: ", password)
  

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P