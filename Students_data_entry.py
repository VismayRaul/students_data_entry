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
    x=[]
    sub={}
    student_inp=input("Enter name : ")
    sub['phy']=input("Enter physics marks : ")
    sub['math']=input("Enter maths marks : ")
    sub['eng']=input("Enter english marks : ")
    x.append(sub)
    avg=0
    for arr in x:
        arr1=arr.values()
        marks_list=[]
        for arr2 in arr1:
            marks_list.append(arr2)
            # print(arr2)
            z=[]
            info={}
            avg = int(arr2)+avg
            percent=avg/3
            info['percentage']=percent
    # z.append(info['average'])
    marks_list.sort()
    large=marks_list[len(marks_list)-1]
    info['top_sub_marks']=large
    z.append(info)
    stud[student_inp] = x
    final[student_inp] = z
print(stud)
print(final)
checkInp=input('Enter name of student whose info is required : ')
print(final[checkInp])