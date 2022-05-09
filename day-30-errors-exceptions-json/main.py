try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["adasdsa"])
except FileNotFoundError:
    file = open("a_file.txt", "w")  # if it doesn't exist the file will be created
    file.write("Something")
except KeyError as error_message:  # get hold of the error message that was generated
    print(f"The key {error_message} does not exist")
else:  # runs if there were no exceptions
    content = file.read()
    print(content)
finally:  # runs no matter what
    raise TypeError("Made up error")  # raise an exception


# height = float(input("Height: "))
# weight = float(input("Weight: "))
#
# if height > 3:
#     raise ValueError("Too high")
#
# bmi = weight / height**2