
# pet=input("enter your pet's name")
# company=input("enter your company's name")
# print("your band name will be")
# print(pet+" "+company)

# # print("hello "[0])
# weight=input("enter your weight")
# height=input("enter your height")
# w=int(weight)
# h=float(height)
# BMI=w/(h**h)
# bmi=str(BMI)
# print("your bmi is "+bmi)
# score=0
# height=1.8
# isWinning=True
# print(f"your score is {score},your height is {height},you are winning is{isWinning}")
# print('json and andrew are truely us')

# day 2 last project
# age=input("please enter your age")
# left_yr=90-int(age)
# left_week=left_yr*52
# left_day=left_yr*365
# left_month=left_yr*12
# print(f"you have left {left_yr} years, {left_month} months ,{left_week} weeks, {left_day} days")

#day three exercises 

#1st project-rollercoaster
# print("welcome to the rollercoaster!")
# height=float(input("what is your height"))
# if height>120 or (height>=80 and height<=120):
#     print("you can ride the rollercoaster!")
# else:
#  print("sorry, you have to grow taller before you can ride.")

#2nd project-modulo
# number=input("enter the number to check whether it is even or odd number")
# modulo=int(number)%2
# if modulo==0:
#     print("the number is even")
# else:
#     print("the number is odd")

#3rd project-nested if statements and elif statements
# print("welcome to the rollercoaster!")
# height=float(input("what is your height"))
# if height>120 or (height>=80 and height<=120):
#     print("you can ride the rollercoaster!")
#     age=int(input("what is your age?"))
#     if age<=12: 
#        print("pay 5 $")
#     elif age>=12 and age<=18:
#        print ("pay 7$")
#     elif age>18:
#        print("pay 12$")
# else:
#  print("sorry, you have to grow taller before you can ride.")


# year=float(input("enter the year check "))

# if year%4==0:
#     if year%100==0 and year%400==0 or year%100!=0 and year%400!=0:
#         print("it is a leap year")
#     elif year%100==0 and year%400!=0 or year%100!=0 and year%400==0:
#         print("it is not a leap year")
# else:
#     print("it is not a leap year")


# name1=input("enter name 1")
# name2=input("enter name 2")
# tot=(name1+name2)
# tot_name=tot.lower()
# first_digit=str(tot_name.count("t")+tot_name.count("r")+tot_name.count("u")+tot_name.count("e"))
# last_digit=str(tot_name.count("l")+tot_name.count("o")+tot_name.count("v")+tot_name.count("e"))
# percent=float(first_digit+last_digit)
# if percent<10 or percent>90:
#     print(f"your score is {percent}, you go together like coke and mentos")
# elif percent >=40 and percent<=50:
#     print(f"your score is {percent}, you are alright together")
# else:
#     print(f"your score is {percent}")


# import random

# random_integer=random.randint(0,1)
# num=float(input("do you want to toss a coin? enter 1 to toss or other to exit"))
# if num==1:
#   if random_integer==1:
#     print("Head")
#   elif random_integer==0:
#     print("Tail")
# else:
#   print("thank you for using us")
# print(random_integer)

fruits=["yoni","dero"]
fruits.append("abigu")
sole=fruits.sort()
fruits.index("abigu")
fruits.remove("abigu")
fruits.append("lala")
print(fruits)
 