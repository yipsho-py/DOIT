###### დავალება 1 ######

# import collections

# def is_anagram(str1, str2):
    
#     str1 = str1.replace(" ", "").lower()
#     str2 = str2.replace(" ", "").lower()
    
    
#     return collections.Counter(str1) == collections.Counter(str2)


# str1 = "listen"
# str2 = "silent"
# print(is_anagram(str1, str2)) 



# ###### დავალება 2 ######

# def count_symbol_occurrences(string, symbol):
#     if len(symbol) != 1:
#         return "მეორე პარამეტრი უნდა იყოს ერთი სიმბოლო."
#     return string.count(symbol)

# text = "hello world"
# character = "o"
# result = count_symbol_occurrences(text, character)
# print(f"სიმბოლო '{character}' {result} ჯერ გვხვდება სტრიქონში '{text}'.")


# ###### დავალება 3 ######

# def fibonacci_sequence(n):
#     if n <= 0:
#         return "რიცხვი უნდა იყოს დადებითი."
#     if n == 1:
#         return [0]
#     if n == 2:
#         return [0, 1]
#     sequence = [0, 1]
#     for _ in range(2, n):
#         sequence.append(sequence[-1] + sequence[-2])
#     return sequence

# n = 10
# result = fibonacci_sequence(n)
# print(f"ფიბონაჩის {n} რიცხვის მიმდევრობა: {result}")

