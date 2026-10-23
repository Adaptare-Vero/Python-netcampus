
#print('Hello world...')
#print('This is your first Python program!')
#print("""I am experimenting with 
#python to create new applications.""")

#Name = "Hlamulo"
#Age = 20

#print("Name is:" + Name)
#print("Age is:", Age)

#print(type(Name))

#Name = Age

#print("Name is:", Name)
#print("Age is:", Name/2)

#print(type(Name)) 

# print("Let's get to know each other!")
# 
# Name = input("What is your name? ")
# print("Nice to meet you, " + Name + "!")
# 
# Age = input("How old are you? ")
# print("So you are " + Age + " years old. Nice!")
# 
# City = input("Where do you live? ")
# print("I like " + City + " too!")
# 
# work = input("What is your occupation? ")
# print("I work as a/an: " + work)
# 
# Hobby = input("What do you enjoy doing in your free time? ")
# print("That sounds fun! I enjoy learning new things too.")
# 
# print("It was nice talking to you, " + Name + "! Have a great 


#calculating average marks

#t1 = int(input("Enter your first test marks: "))
#t2 = int(input("Enter your second test marks: "))
#t3 = int(input("Enter your third test marks: "))

#Total = t1 + t2 + t3

#Average = Total / 3

#Display outputs
#print("Test 1", t1, "\nTest 2", t2, "\nTest 3", t3)
#print("Total is:" , Total)
#print("Average is:", Average)


#Functions

# def input_marks():
#     global t1, t2, t3
#     t1 = int(input("Enter your first test marks: "))
#     t2 = int(input("Enter your second test marks: "))
#     t3 = int(input("Enter your third test marks: "))

# def display_marks():
#     print("test 1 :",t1)
#     print("test 2 :",t2)
#     print("test 3 :",t3)

# def total():
#     return t1 + t2 + t3

# def average():
#     return total() / 3

# #def main():
#     #input_marks()
#     display_marks()
    #print("Total marks is:", total())
    #print("Average marks is:", average())

#main()
    



# def main():
#     n1, n2 = calculation.inputs()
#     calculation.add_num(n1, n2)
#     calculation.sub_num(n1, n2)
#     calculation.mul_num(n1, n2)
#     calculation.div_num(n1, n2)


#     main()

    # import numbers


# def devide(n1, n2):
#         remaind = n1%n2
#         floor = n1//n2
#         print(n1, "divided by", n2, "=", floor, "with a remainder of", remaind)

# def main():
#     num = int ("input numerator")
#     den = int ("input denominator")
#     divide(num, den)

# print("Hello")

#importing libraries

# import math

# print("ceil: ", math.ceil(5.4))
# print("Trunc: ", math.trunc(5.4))
# print("power: ", math.pow(5,4))
# print("square: ", math.sqrt(25))

# import random

# print("Random Int: ",random.randint(2,10))
# print("Random Range: ",random.randrange(10))
# num = print("Random Range: ",random.randrange(10))
# print(num)

#string manipulation

# phrase = "Monty Python"

# print(phrase)
# print(phrase[0])
# print(phrase[-1])
# print(phrase[4])
# print(phrase[6:])
# print(phrase[:4])
# print(phrase[4:])
# name = phrase[:4]
# print(name)
# print(name.isdigit())
# print(name.isalpha())

# text = 'Monty Python'
# print('{0:s} is an {1:s} movie!'.format(text,'awesome'))

# import math 

# print('Pi = {:.2f}'.format(math.pi))




# import random
# colors = ["red","blue","green","orange"]
# print(random.choice(colors))

# def remove_random(the_list):
#     x = random.choice(the_list)
#     the_list.remove(x)
#     return

# def show_type(obj):
#     print(type(obj))
# magenta = (255, 0, 255)

# def main():
#     colors = ["red","blue","green","orange"]
#     remove_col = remove_random(colors)
#     print(f'The removed color was:{remove_col}.')
#     print(f'The remaining color are:{colors}.')

#     #Tupple
#     MAGENTA = 255, 0, 255
#     show_type(MAGENTA)

#     magenta = (255, 0, 255)
#     show_type(magenta)

# main()


# import random

# def main():
#     play = ["Rock","Paper","Scissor"]

#     comp_choice = random.choice(play)
#     num = input("Enter 1 for rock, 2 for paper and 3 for scissor: ")
#     num = int(num) - 1
#     user_choice = play[num]

#     if num < 0 or num > 2:
#         print("Invalid input. Please enter a number between 1 and 3.")
#         return

#     print("computer: ", comp_choice)
#     print("user: ", user_choice)

#     if comp_choice == user_choice:
#         print("It's a tie!")

#     if comp_choice == "Rock" and user_choice == "Paper":
#         print("User wins!") 
        
#     if comp_choice == "Rock" and user_choice == "Scissor":
#         print("Computer wins!")

#     if comp_choice == "Paper" and user_choice == "Rock":        
#         print("Computer wins!")

#     if comp_choice == "Scissor" and user_choice ==  "Paper":
#         print("Computer wins!")

#         #ask to play again

#     again = input("Do you want to play again? (y/n): ").lower()

#     if again != "yes":

#         print("Thank you for playing!") 
#         break
     

# main()

grades = {"English":97,"Math":93,"Technology":89,"Art":74,"Music":86}

# Try error handling


# def error_handling():

# try:

#     grades = {"English":97,"Math":93,"Technology":89,"Art":74,"Music":86}


#     for course in grades:

#       print(course)

#     for course in grades.keys():

#       print(course)

#     for item in grades.items():
#      course = item[0]
#      grade = item[1]
#      print(f'{course}: {grade}')
          
# except Exception as e:

#     print (type(e))
#     print(e, '\n')

#     #exception handling 
# def divide():

#     try:
#         numerator = int(input("Enter the numerator: "))
#         denominator = int(input("Enter the denominator: "))
#         result = numerator / denominator
#         print(numerator, '/', denominator, '=', result)
#         print(f"The result of {numerator} divided by {denominator} is: {result}")

#     except ZeroDivisionError:
#         print("Error: Cannot divide by zero.")
#         divide()
#     except ValueError:
#         print("Error: Please enter valid integers.")
#         divide()
#     except KeyboardInterrupt:
#         print("\nQuitter")
#     except Exception as e:
#         print(f"An unexpected error occurred: I have no idea  dude {e}")
       
# def main ():
#         divide()

# main()

# print(grades["English"])  #print the value of the key "English" in grades

# print(grades)    #print grades
 
# grades["Gym"] = 90 # create a new key value pair in grades

# print(grades)    #print grades

# del grades["Gym"] # delete the key value pair with key "Art" in grades

# print(grades)    #print grades

# grades["Gym"] = 90 # create a new key value pair in grades 


       #dates

# from datetime import datetime


#current_time

# c_time = datetime.today().strftime("%H:%M,%S")
# c_date = datetime.today().strftime("%Y,%M,%D")
# print(f"Current time: {c_time}")
# print(f"Current date: {c_date}")


#file Processing

#1: write to a file

with open("example.txt", "w") as file:
    file.write("Hello, Python!\n")
    file.write("This is my test file.\n")
   

    #reading from a file

with open("example.txt", "r") as file:
    content = file.read()
    print(content)
