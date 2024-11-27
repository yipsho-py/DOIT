### დავალება 1 ###
# class BankAccount:
#     def __init__(self, account_number, account_holder, balance=0):
#         self.account_number = account_number
#         self.account_holder = account_holder
#         self.balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"{amount} ჩარიცხულია ანგარიშზე {self.account_number}. ახალი ბალანსი: {self.balance}")
#         else:
#             print("ჩარიცხვის რაოდენობა უნდა იყოს დადებითი.")

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("არ არის საკმარისი ბალანსი.")
#         elif amount <= 0:
#             print("გადახდის რაოდენობა უნდა იყოს დადებითი.")
#         else:
#             self.balance -= amount
#             print(f"{amount} გამოტანილია ანგარიშიდან {self.account_number}. ახალი ბალანსი: {self.balance}")

#     def get_balance(self):
#         return self.balance


# account1 = BankAccount("123456", "დავით კასრაძე", 1000)
# account2 = BankAccount("789012", "ირაკლი კეკელიძე", 500)


# account1.deposit(300)
# account1.withdraw(200)
# account2.deposit(100)
# account2.withdraw(700)

# print(f"ანგარიში 1-ის ბალანსი: {account1.get_balance()}")
# print(f"ანგარიში 2-ის ბალანსი: {account2.get_balance()}")












### დავალება 2 ###

# class Student:
#     def __init__(self, name, student_id):
#         self.name = name
#         self.student_id = student_id
#         self.courses = []

#     def enroll_course(self, course_name):
#         if course_name not in self.courses:
#             self.courses.append(course_name)
#             print(f"{self.name} has enrolled in the course: {course_name}")
#         else:
#             print(f"{self.name} is already enrolled in the course: {course_name}")

#     def display_info(self):
#         print(f"Student Name: {self.name}")
#         print(f"Student ID: {self.student_id}")
#         print("Courses:", ", ".join(self.courses) if self.courses else "No courses enrolled")


# student1 = Student("Nini", "S001")
# student2 = Student("Beka", "S002")


# student1.enroll_course("Mathematics")
# student1.enroll_course("Physics")
# student2.enroll_course("Programming")
# student2.enroll_course("Mathematics")


# student1.display_info()
# print()  
# student2.display_info()





