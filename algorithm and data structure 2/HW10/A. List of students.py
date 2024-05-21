n = int(input())
students = set()

for i in range(n):
    student = str(input())
    h_student = hash(student)
    students.add(h_student)  

print(len(students))