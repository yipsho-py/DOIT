###### დავალება 1 ######

# file_name = 'read.txt'

# with open(file_name, 'w') as f:
#     for i in range(1, 1001):
#         f.write(f"ეს არის ხაზი №{i}\n")

# with open(file_name, 'r') as f:
#     lines = f.readlines()

# print(f"ფაილში {len(lines)} ხაზი არის შევსებული.")



###### დავალება 2 #######


# file_name = 'named_lines.txt'

# names = {
#     2: "Second",
#     8: "Eighth",
#     10: "Tenth",
#     12: "Twelfth",
#     17: "Seventeenth"
# }

# with open(file_name, 'w') as f:
#     for i in range(1, 21):
#         if i in names:
#             f.write(f"{names[i]}\n")
#         else:
#             f.write(f"Line {i}\n")

# with open(file_name, 'r') as f:
#     content = f.readlines()

# for line in content:
#     print(line.strip())


###### დავალება 3 #######

# file1 = 'file1.txt'
# file2 = 'file2.txt'
# merged_file = 'merged_file.txt'

# with open(file1, 'r') as f1, open(file2, 'r') as f2:
#     content1 = f1.readlines()
#     content2 = f2.readlines()

# with open(merged_file, 'w') as f3:
#     f3.writelines(content1)
#     f3.writelines(content2)

# with open(merged_file, 'r') as f3:
#     merged_content = f3.read()

# print(merged_content)


###### დავალება 4 #######

# def is_palindrome(s):
#     return s == s[::-1]

# def print_palindromes_from_file(file_name):
#     with open(file_name, 'r') as f:
#         lines = f.readlines()
    
#     for line in lines:
#         line = line.strip()
#         if is_palindrome(line):
#             print(line)


# file_name = 'example.txt'
# print_palindromes_from_file(file_name)



###### დავალება 5 #######

# def split_file_into_parts(file_name):
#     with open(file_name, 'r') as f:
#         lines = f.readlines()

#     num_files = (len(lines) // 10) + (1 if len(lines) % 10 != 0 else 0)

#     for i in range(num_files):
#         part_file_name = f"part_{i + 1}.txt"
#         with open(part_file_name, 'w') as part_file:
#             part_file.writelines(lines[i*10:(i+1)*10])


# file_name = 'example.txt'
# split_file_into_parts(file_name)








