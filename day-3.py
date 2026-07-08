# student =("venny","hemu",'veha')
# print(student[-2])
# #### tuple is a collection used to store multiple
# numbers = (10,20,30,40)
# print(numbers[-3])

# data = [1,2,3]
# data[0] =100
# print(data)

# x=(1,2,3,2,1,1,1,4,4,5,7,9)
# print(x.count(1))
# print(x.count(2))

# x =("apple","banana","banana","orange","apple","apple")
# print(x.count("apple"))
# print(x.count("banana"))

#tuple slicing
# num =(10,20,30,40,50)
# print(num[2:4])

#sets is a collection of: remove duplicate values :store uniq indexing :no indexing : unordered

# x ={1,2,3,2,1,1,1,4,5}
# print(x)
# data = {1,2,3}
# data.add(4)      # we can remove
# print(data)

# a ={1,2,3}
# b = {3,4,5}
# print (a|b)

# a ={1,2,3}
# b = {3,4,5}
# print (a & b)

#####################functions#################

# def greeting():
#     print("hello students")
# greeting()

# def add():
#     return 10 + 20
# result = add()
# print(result)

# def sub():
#     return 10 -20
# result = sub()
# print(result)


# def multiply():
#     return 10*20
# result = multiply()
# print(result)

# def add(a,b):
#     print(a+b)
# add(10,20)

# def sub(a,b):
#     print(a-b)
# sub(10,20)

# def multiply(a,b):
#     print(a*b)
# multiply(10,20)

# def add(*numbers):
#     print(numbers)
# add(10,20,30,40,50,60)

# def venny (*num):
#     total = 0
#     for i in num:
#         total +=i
#     print(total)
# venny (10,20,30,40,50,60)

###################kwargs#########################

# def student(**details):
#     print(details)

#     student(
#         name="venny",
#         age=22,
#         job="sales",
#     )
#     print(details)

# def students(**details):
#     print("name :",details["venny"])
#     print("age :",details["22"])
#     print("job :",details["sales"])
# student(
#     name="venny",
#     age=22,
#     job="sales",
# )


# import math

# num = 36
# result = math.sqrt(num)
# print("Square root:", result)

# num = int(input("Enter a number: "))
# sqrt = num ** 0.5
# print("Square root:", sqrt)

# def square(x):
#     return x*x
# print(square(4))

# square = lambda x:x*x
# print(square(25))

# add = lambda a,b:a+b
# print(add(10,20))


# num = int(input("Enter a number: "))

# check = lambda x: "Even" if x % 2 == 0 else "Odd"
# print(check(num))

# text = input("Enter text: ")

# upper_case = lambda x: x.upper()
# print(upper_case(text))


# text = input("Enter a name: ")

# length = lambda x: len(x)

# print("Length of name:", length(text))


# file = open("student.txt","w")
# file.write("hello vennela")
# file.close()

# print("data written successfully")

# file = open("student.txt","r")
# data=file.read()
# print(data)
# file.close()

# file = open("student.txt","a")
# file.write("\nhello students")
# file.close()

# print("data written successfully")

# file=open("student.txt","r")
# print(file.read())
# file.close()

# try:
#     a=10
#     b=0
#     print(a/b)
# except:
#     print("you are beautiful")

# try:
#     string = (input("enter string:"))
#     print(string)
# except ValueError:
#     print("only string allowed")

# try:
#     a=int(input("enter A:"))
#     b=int(input("enter B"))
#     print(a/b)
# except ZeroDivisionError:
#     print("cannont divide by zero")
# except ValueError:
#     print("enter only numbers")

# try:
#     file = open("data.txt")
#     print(file.read())
# except:
#     print("file error")

# finally:
#     print("program completed")

try:
    print(10/2)
except:
    print("error")
else:
    print("success")