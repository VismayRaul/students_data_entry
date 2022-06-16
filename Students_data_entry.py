#Enter number of students
#ask student details individually like name then marks of sub phy sic math
#store in dictionary
#print name topScoredSubject and percentage optained 
#take student name as input and print his details


a=int(input('Enter no. of students : '))
student_inp={}
stud={}
final={}
for i in range(a):
    student_inp["name"]=input("Enter name : ")
    phy=input("Enter physics marks : ")
    math=input("Enter maths marks : ")
    eng=input("Enter english marks : ")
    x=[phy,math,eng]
    avg=0
    for arr in x:
        z=[]
        avg = int(arr)+avg
    z.append(avg/3)
    x.sort()
    large=x[len(x)-1]
    z.append(large)
    stud[student_inp["name"]] = x
    final[student_inp["name"]] = z
print(stud)
print(final)
checkInp=input('Enter name of student whose info is required : ')
print(final[checkInp])