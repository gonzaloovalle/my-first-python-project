###Variables & Data Types###
# age = 20
# price = 19.95
# first_name = "Gonzalo"
# is_online = True
# print(age)

###Input Method###
# name = input("What is your name? ")
# print("Hello " + name)

###Type Coercion###
# birth_year = input("Enter your birth year: ")
# age = 2022 - int(birth_year)
# print("Your age is " + str(age))

# input1 = input("First: ")
# num1 = float(input1)
# input2 = input("Second: ")
# num2 = float(input2)
# sum = float(num1 + num2)
# print("Sum: " + str(sum))

##Alternate Solution##
# first = float(input("First: "))
# second = float(input("Second: "))
# sum = first + second
# print("Sum: " + str(sum))

###Strings###
# course = "Python for Beginners"
# print(course.find("y"))
# print(course.find("Y"))
# print(course.find("for"))
# print(course.replace("for", "4"))
# print(course.find("Python"))
# print("Python" in course)

###Arithmetic Operators###
# print(10 + 3)
# x = 10
# print(x)
# x = x + 3
# print(x)
# x += 3
# print(x)
# x *= 3
# print(x)
# x -= 3
# print(x)

###Operator Precedence###
# x = 10 + 3 * 2
# print(x)
# x = (10 + 3) * 2
# print(x)

###Comparison Operators###
# x = 3 > 2
# print(x)
# x = 3 == 2
# print(x)
# price = 25
# print(price > 10 and price < 30)
# print(price < 10 or price < 30)
# print(not price < 10)

###If Statements###
# temperature = 75
# if temperature > 80:
#     print("It's a warm day")
#     print("Stay hydrated!")
# elif temperature > 65:
#     print("It's a nice day")
#     print("Enjoy the day!")
# elif temperature > 50:
#     print("It's a cold day")
#     print("Bundle up!")
# print("Done")

# weight = float(input("Weight: "))
# choice = input("(K)g or (L)bs: ")
# if choice.upper() == "K":
#     converted = weight / 0.45
#     print("Weight in Lbs: " + str(converted))
# else:
#     converted = weight * 0.45
#     print("Weight in Kgs: " + str(converted))

###While Loops###
# i = 1
# while i <= 10:
#     print(i * "*")
#     i += 1

###Lists###
# names = ["Gonzalo", "Johnneisha", "Tori"]
# print(names)
# print(names[1])
# print(names[-1])
# print(names[2])
# names[0] = "Peaches"
# print(names)
# print(names[0:2])
# print(names)

# numbers = [1, 2, 3, 4, 5]
# print(numbers)
# numbers.append(7)
# print(numbers)
# numbers.insert(5, 6)
# print(numbers)
# numbers.remove(7)
# print(numbers)
# numbers.clear()
# print(numbers)
# print(1 in numbers)
# print(10 in numbers)
# print(len(numbers))

###For Loops###
# numbers = [1, 2, 3, 4, 5]
# for item in numbers:
#     print(item)

##Same result in a while loop##
# i = 0
# while i < len(numbers):
#     print(numbers[i])
#     i += 1

###range() Function###
# numbers = range(5)
# print(numbers)
# for number in numbers:
#     print(number)

# numbers = range(5, 10)
# for number in numbers:
#     print(number)

# numbers = range(5, 10, 2)
# for number in numbers:
#     print(number)

# for number in range(5):
#     print(number)

###Tuples###
# numbers = (1, 2, 3)
# numbers[0] = 2
