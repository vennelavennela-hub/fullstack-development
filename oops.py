# class student:  # class   name
#     name = "venny"  # attribute
#     def study(self):   #represent current object
#         print("venny is sleeping")
# s1 = student()         #s1 is a object
# print(s1.name)
# s1.study() # study is a method

# class student:
#     def details(self):
#         print("had breakfast")
# s1 = student()
# s1.details()

# student.details(s1)

# class student:
#     def __init__(self,name,age):    #initisalize is a constructor
#         self.name = name
#         self.age = age
# s1 = student("venny",22)
# s2 = student("hemu",21)
# s3 = student("shru",21)
# print(s1.name,s2.name,s3.name)
# print(s1.age,s2.age,s3.age)   #name nd age is attribute

# class bank:
#     def __init__(self,balance):
#         self.balance = balance
#     def check_balance(self):
#         print(self.balance)
# account = bank(10000)
# account.check_balance()

# class user:
#     def __init__(self,name):
#         self.name = name
#     def login(self):
#         print(self.name,"logged in")

# u1 = user("venny")
# u2 = user("hemu")
# u1.login()
# u2.login()

########################inheritance#####################
# class father:
#     def house(self):
#         print("father has a house")

# class son(father):
#     def bike(self):
#         print("son has a bike")
# s=son()
# s.house()
# s.bike()

# class grandfather:
#     def land(self):
#         print("grandfather's land")

# class father(grandfather):
#     def house(self):
#         print("father's land")

# class son(father):
#     def bike(self):
#         print("son has a bike")

# obj = son()
# obj.land()
# obj.house()
# obj.bike()

# class Father:
#     def father(self):
#         print("Father")

# class Mother:
#     def mother(self):
#         print("Mother")

# class Son(Father, Mother):
#     pass

# obj = Son()
# obj.father()
# obj.mother()

# class father:
#     def house(self):
#         print("father's house")

# class mother:
#     def car(self):
#         print("mother's land")

# class son(father,mother):
#     def bike(self):
#         print("son's bike")

# thirdclass =son()
# thirdclass.house()
# thirdclass.car()
# thirdclass.bike()

# class Father:
#     def house(self):
#         print("Father's house")

# class Son(Father):
#     def bike(self):
#         print("Son's bike")

# class Daughter(Father):
#     def car(self):
#         print("Daughter's car")

# son = Son()
# daughter = Daughter()

# print("Son:")
# son.house()
# son.bike()

# print("Daughter:")
# daughter.house()
# daughter.car()

###################magic method##############################
# class student:
#     def __init__(self,name):
#         self.name=name

#     def __str__(self):
#         return self.name

# s= student("king")
# print(s)

# def login(func):
#     def wrapper():
#         print("checking login")
#         func()
#     return wrapper 
# @login
# def dashboard():
#     print("dashboard page")
# dashboard()


# def message(func):
#     def wrapper():
#         print("function started")
#         func()
#         print("function ended")
#     return wrapper
# @message
# def hello():
#     print("hello python")
#     print("python is easy")
# hello()


# import json

# student = {
#     "name": "Vennela",
#     "age": 21
# }

# json_data = json.dumps(student)
# print(json_data)


# import json

# x = '{"name":"Vennela","age":22}'

# y = json.loads(x)

# print(y)
# print(y["name"])
# print(y["age"])



import requests
response = requests.get(
    "https://github.com/vennelavennela-hub/fullstack-development.git"
)
data = response.json()
print(data)