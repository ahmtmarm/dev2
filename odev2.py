students = ["Ahmet MARIM","Deniz MARIM","Ali MARIM","Ümmü MARIM"]
print(students)

#addStudent
addStudent = input("Enter your name and username :")
students.append(addStudent)
print(students)

#  print("**********")
#  print("**********")

#removeStudent
removeStudent = input("Enter the name and surname of the student you want to remove :")
students.remove(removeStudent)
print(students)

# print("**********") print("**********")

# #addStudents
addStudents = []
hms = int(input("how many names do you want to add :"))
for i in range(hms):
   name=input("Write the students you want to add :")
   addStudents.append(name)
students.extend(addStudents)
print(students)

# print("**********")
# print("**********")

#What are the names on the list
a = 0
while a < len(students):
   print(a+1,". name:",students[a])
   a+= 1

print("**********")
print("**********")

#studentNumber

who = input("which student's number do you want to know ?")
for w in range(len(students)):
   if who == students[w]:
     print(who,"student number:",w)

#removeStudents
rmv = int(input("how many names do you want to remove :"))
for i in range(rmv):
  name=input("the name you want to delete :")
  for r in students:
    if r == name:
      students.remove(name)
print(students)
