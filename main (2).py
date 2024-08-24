student_name = input("Enter student name: ")
tamil = float(input("Enter student's tamil marks: "))
science = float(input("Enter student's science marks: "))
social = float(input("Enter student's social marks: "))
prose = float(input("Enter student's prose marks: "))
grammar = float(input("Enter student's grammar marks: "))

total = tamil + science + social + prose + grammar
average = total / 5
print("Student Name", student_name)
print("Total marks", total)
print("Average Marks", average)

if average >= 90 and average <= 100:
    print("grade A")
elif average >= 80 and average <= 89:
    print("grade B")
elif average >= 70 and average <= 79:
    print("grade C")
elif average >= 60 and average <= 69:
    print("grade D")
else:
    print("grade E")
