programming_dictionaries = {"Bug": "An error in a program that prevents the program from running as expected.",
                            "Program": "A set of instructions that feeds to the computer.",
                            "Loop": "A set of instructions that likely to do over again and again."}
# print(programming_dictionaries["Bug"])

# To add key and value to the dictionaries

programming_dictionaries["Function"] = "A piece of code that you can call easily over and over again."
# print(programming_dictionaries)

# Modifying the dictionaries

programming_dictionaries["Program"] = "Nothing but a set of commands or instructions."
# print(programming_dictionaries)

# loop dictionaries

for i in programming_dictionaries:
    print(i)
    print(programming_dictionaries[i])
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60 }

student_grades['Harry'] = 'Exceeds Expectations'
student_grades['Ron'] = 'Acceptable'
student_grades['Hermione'] = 'Outstanding'
student_grades['Draco'] = 'Acceptable'
student_grades['Neville'] = 'Fail'
print(student_scores)
print(student_grades)
