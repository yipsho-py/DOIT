# class Person:
#     def __init__(self, name, deposit=1000, loan=0):
#         self.name = name
#         self.deposit = deposit
#         self.loan = loan

#     def __str__(self):
#         return f"Name: {self.name}, Deposit: {self.deposit}, Loan: {self.loan}"

# class House:
#     def __init__(self, ID, price, owner):
#         self.ID = ID
#         self.price = price
#         self.owner = owner
#         self.status = "გასაყიდი"

#     def sell(self, buyer, loan_amount=None):
#         if loan_amount is None:
#             self.owner.deposit += self.price
#             self.owner = buyer
#             self.status = "გაყიდული"
#             print(f"{self.owner.name} now owns the house. Status: {self.status}.")
#         else:
#             self.owner.deposit += self.price
#             self.owner = buyer
#             self.status = "გაყიდული სესხით"
#             buyer.loan += loan_amount
#             print(f"{self.owner.name} now owns the house with a loan of {loan_amount}. Status: {self.status}.")

# owner = Person("George", 5000, 0)
# buyer = Person("Anna", 1500, 0)

# house = House(1234, 2000, owner)

# print(f"House ID: {house.ID}, Price: {house.price}, Owner: {house.owner.name}, Status: {house.status}")

# house.sell(buyer)

# buyer2 = Person("John", 2000, 0)
# house2 = House(5678, 3000, owner)
# house2.sell(buyer2, 2500)

# print(f"New House Status: {house2.status}, New Owner: {house2.owner.name}, Buyer Loan: {buyer2.loan}")
