import random
import pandas

# Example:
# numbers = [1, 2, 3]
# new_list = [new_item for item in list (if test)]  # The key word method
# new_list [n+1 for n in numbers]

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# uppercase_names = [name.upper() for name in names if len(name) > 4]
# print(uppercase_names)


# # Exercise:
# with open("file1.txt") as file1:
#     list_1 = file1.readlines()
#
# with open("file2.txt") as file2:
#     list_2 = file2.readlines()
#
# result = [int(item) for item in list_1 if item in list_2]
#
# print(result)


# # Dictionary comprehension
# # new_dict = {new_key:new_value for item in list (if test)}
# students_scores = {student: random.randint(1, 100) for student in names}
# # new_dict = {new_key:new_value for (key, value) in old_dict.items() (if test)}
# passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}


# # Loop through pandas data frame
# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
# student_data_frame = pandas.DataFrame(student_dict)
# # Loop through rows in data frame
# for (index, row) in student_data_frame.iterrows():
#     print(row.student)

