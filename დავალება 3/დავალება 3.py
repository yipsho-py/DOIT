################################ დავალება 1###############################################################
#დაწერეთ პითონის პროგრამა, რომელიც მიიღებს მომხმარებლისგან რიცხვს და შემდენ იყენებს while ციკლს, 
# რომ რევერსულად დაბეჭდოს რიცხვები 0-მდე, მაგალითად თუ შეიყვანს რიცხვს 4, დაიბეჭდოს 4,3,2,1


# number = int(input("Enter a number: "))
 
# if number == 0:
#     print("Wrong number")
# elif number > 0:
#     while number > 0:
#         print(number)
#         number-= 1
# else:
#     while number <0:
#         print (number)
#         number +=1



############################### დავალება 2######################################################################
# დაწერეთ პითონის პროგრამა, რომელიც მიიღებს მუდმივად რიცხვებს. შექმენით საწყისი ცვლადი total_sum = 0, 
# შეამოწმეთ რიცხვი, თუ დადებითია, მხოლოდ მაშინ დაუმატეთ total_sum ცვლადს, ეს პროცესი გაგრძელდეს მანამ, 
# სანამ მომხმარებელი არ შეიყვანს ტექსტს sum, რის შემდეგაც დაიბეჭდება შეყვანილი დადებითი რიცხვების ჯამი.

# total_sum = 0
# userinput = input("enter a number, or to see sum enter the word sum:")

# while userinput != "sum":

#   if int(userinput) > 0:
#       total_sum += int(userinput)
      
#   userinput = input("enter a number, or to see sum enter the word sum:")    

# print (total_sum)



################################### დავალება 3 ###################################################
# დაწერეთ პითონის პროგრამა, რომელიც შემთხვევითობის პრინციპით აირჩევს რიცხვს ნებისმიერ შუალედში, 
# ასევე შექმენით ცვლადი, რომელიც აღნიშნავს სიცოცხლის რაოდენობას. მომხმარებელს მოთხოვეთ,
# რომ შეიყვანოს რიცხვი და შეადარეთ შემთხვევითობის პრინციპით არჩეულ რიცხვს, 
# თუ მომხმარებლის მიერ შეყვანილი რიცხვი უფრო მეტია დაბეჭდეთ რომ რიცხვი უფრო მეტია, 
# თუ უფრო ნაკლებია დაბეჭდეთ რომ რიცხვი ნაკლებია.

# მოქმედება უნდა გახორციელდეს მანამ, სანამ მომხმარებელი არ გამოიცნობს რიცხვს ან არ ამოეწურება სიცოცხლის რაოდენობა

# გამოიყენეთ else ბლოკი while ციკლთან ერთად


# import random 
# number=random.randrange (20)
# usernumber = int(input("Guess the number: "))
# live = 5
# while usernumber != number and live != 1:
    
#     if usernumber < number:
#         print("Your guess is lower" )

#     else: 
#       print("your guess is higher") 
    
#     live -=1    
#     print("You have left ", live, " Guesses ")
#     usernumber = int(input("Guess the number: "))

# if usernumber == number:
#    print("congratulations ")

# else: print("Sorry you are out of lives")   


    