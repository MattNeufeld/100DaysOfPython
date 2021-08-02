student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
total = 0
for x in student_heights:
    total = total + x
avg = total / len(student_heights)
print(round(avg))
