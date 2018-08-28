x = input("Enter Number of Grades: ")
i = 0
list = []

while(i < int(x)):
    sample_grade = float(input("Enter Grade: "))
    if(sample_grade < 1.0 or sample_grade > 5.0):
        print("Error. Input Number between 1.0 and 5.0, please try again.\n", end="")
    else:
        list.append(sample_grade)
        i += 1
print("\n")

i = 0

while(i < int(x)):
    if(list[i] < 3.1):
        print("Grade # " + str(i + 1) + ": " + str(list[i]) + " = PASS\n", end="")
        i += 1
    else:
        print("Grade # " + str(i + 1) + ": " + str(list[i]) + " = FAIL\n", end="")
        i += 1

input()



