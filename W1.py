import math as ma
#Q1
# print( "Twinkle, twinkle, little star, How I wonder what you are!\n\t Up above the world so high, Like a diamond in the sky.\n\t\t Twinkle, twinkle, little star, How I wonder what you are")

#Q2
# fn = input("ENter first name : ")
# ln = input("Enter last name : ")
# print(ln,fn)

#Q3
# r = float(input("Enter radius : "))
# print("Area : ",ma.pi*r**2)

#Q4
# color_list = ["Red","Green","White" ,"Black"]
# n = len(color_list)
# print(color_list[0],color_list[n-1])

#Q5
# n = int(input("Enter a number : "))
# a = str(n)
# print(f"{n}+{a}{a}+{a}{a}{a}: ",n+int((a+a))+int((a+a+a)))

#Q6
# l = []
# for i in range(1,6):
#     a = int(input("Enter number : "))
#     l.append(a)
# t = tuple(l)
# print(t)
# print(l)

#Q7
# c = float(input("Enter temperature in Celsius: "))
# f = (c * 9/5) + 32
# print(f"{c}C = {f}F")

#Q8
# a = int(input("Enter a number : "))
# b = int(input("Enter a number : "))
# print(f"A : {a}, B : {b}")
# c = a
# a = b
# b = c
# print(f"A : {a}, B : {b+1}")

#Q9
# a  = int(input("Enter a number : "))
# if(a%2==0):
#     print("Even")
# else:
#     print("Odd")

#Q10
# year = int(input("Enter a year: "))
# if (year%4==0 and year%100!=0) or (year%400==0):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")

#Q11
# x1 = int(input("Enter x1 : "))
# y1 = int(input("Enter y1 : "))
# x2 = int(input("Enter x2 : "))
# y2 = int(input("Enter y2 : "))
# print("Distance : ",((x2-x1)+(y2-y1))**0.5)

#Q12
# a1 = int(input("Enter angle 1 : "))
# a2 = int(input("Enter angle 2 : "))
# a3 = int(input("Enter angle 3 : "))
# if(a1+a2+a3==180):
#     print("YES")
# else:
#     print("NO")

#Q13
# principal = float(input("Enter the principal amount: "))
# rate = float(input("Enter the rate of interest (in %): "))
# time = float(input("Enter the time period (in years): "))
# n = int(input("Enter the number of times interest applied per year: "))
# amount = principal * (1 + (rate / 100) / n)**(n * time)
# compound_interest = amount - principal
# print(f"Compound Interest = {compound_interest:.2f}")
# print(f"Total amount after {time} years = {amount:.2f}")

#Q14
# a = int(input("Enter a number : "))
# for i in range(2,a):
#     if(a>1):
#         flag=0
#     if(a%i==0):
#         flag=1
#         break
# if(flag==1):
#     print("Not prime")
# else:
#     print("Prime")

#Q15
# n = int(input("Enter a number : "))
# form = n*(n+1)*(2*n+1)/6
# print(form)
