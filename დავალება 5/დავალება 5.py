################## დავალება 1.###########
#მოცემულია სია my_list:
# mylist = [36, 73, 1, 7, 54, 100, 237, 34, 76, 10, 7, 9 , 12, 34, 49]
# დაწერეთ პროგრამა, რომელიც შეკრებს ამ სიის მე–3, მე–9 და მე–14 ელემენტებს და მიღებულ შედეგ დაბეჭდავს ტერმინალში.



# my_list = [36, 73, 1, 7, 54, 100, 237, 34, 76, 10, 7, 9, 12, 34, 49]
# print(my_list[2] + my_list[8] + my_list[13])



######## დავალება 2 #########
#შექმენით 20 რენდომ რიცხვისგან შემდგარი ლისტი, შექმენით ახალი ლისტი, რომელშიც შეინახავთ პირველი ლისტიდან
# მხოლოდ კენტ მნიშვნელობებს და დაბეჭდეთ ლისტში ყველაზე მცირე და 
# ყველაზე დიდი ელემენტი. არ გამოიყენოთ ფუნქციები min() და max()




# import random
# main_list = [random.randint(1, 60) for _ in range(20)]

# odd_numbers = [num for num in main_list if num % 2 != 0]

# smallest = odd_numbers[0]
# largest = odd_numbers[0]

# for num in odd_numbers:
#     if num < smallest:
#         smallest = num
#     if num > largest:
#         largest = num


# print("odd numbers:", odd_numbers)
# print("smallest number:", smallest)
# print("largest number:", largest)


#####დავალება 3###########

# დაწერეთ პითონის პროგრამა, რომელიც შექმნის ლისტს my_llist = [43, '22', 12, 66, 210, ["hi"]], და შეასრულებს
# შემდეგ ნაბიჯებს:
# a. დაბეჭდავს 210-ის ინდექს, თუ მერამდენე ინდექსზეა
# b. დაამატებს ბოლო ელემენტში ტექსტს "hello"
# c. წაშლის მეორე ინდექსზე მდგომ ელემენტს და დაბეჭდავს ლისტს
# d. შექმენით ახალი ლისტი my_llist_2 , რომელსაც ექნება my_llist მნიშვნელობა, გაასუფთავეთ my_llist_2 
# მნიშნველობა და დაბეჭდეთ my_llist და my_llist_2 ლისტები



# my_list= [43, '22', 12, 66, 210, ["hi"]]

# my_list2= my_list.copy()
# my_list2.clear()

# print(my_list)
# print(my_list2)

# # print(my_list.index(210))

# # my_list.append("hello")
# # print(my_list)

# # del my_list [2]
# # print(my_list)


################ დავალება 4 ###############
#დაწერეთ პროგრამა, რომელიც დაბეჭდავს ორი მატრიცის ჯამს, ჯამი გამოითვლება შემდეგი წესით, 
# ერთი და იგივე ადგილზე მდგომი ელემენტები ემატება ერთმანეთს,
#  მატრიცების განზომილებები უნდა იყოს ერთი და იგივე.

# matrix= [
#     [2, 4, 5],
#     [3, 6, 1],
#     [8, 2, 3]
# ]
# matrix1= [
#     [8, 6, 3],
#     [1, 5, 8],
#     [9, 3, 6]
# ]


# sum=[
#     [0,0,0],
#     [0,0,0],
#     [0,0,0]
# ]

# for i in range (3):
#     for j in range(3):
#         sum[i][j] = [matrix[i][j]+matrix1[i][j]]


# print(sum)
        

# დაწერეთ პროგრამა რომელიც გააკეთებს კვადრატული 3x3 მატრიცის ტრანსპონირებას, 
# ტრანსპონირება ნიშნავს ინდექსების შებრუნებას, მაგ. თუ გვაქვს ერთ-ერთი ჩანაწერი ინდექსით list[2][3], 
# ტრანსპონირების შემდეგ მისი ინდექსი უნდა გახდეს list[3][2], ასე ხდება ყველა ჩანაწერზე
        
# matrix= [
#     [2, 4, 5],
#     [3, 6, 1],
#     [8, 2, 3]
# ]

# newMatrix = [
#     [0, 0, 0],
#     [0, 0, 0],
#     [0, 0, 0]
# ]


# for i in range(3):
#     for j in range(3):
#         newMatrix[i][j] = matrix[j][i]

# print(newMatrix)


# list comprehension გამოყენებით შექმენით რენდომ რიცხვებისგან შემდგარი 4x4 კვადრატული მატრიცა

# import random

# matrix=[[],[],[],[]]
# for i in range(4):
#     a = []
#     for j in range(4):
#         a.insert(j,random.randint(1,10))
#     matrix[i]=a

# print(matrix)