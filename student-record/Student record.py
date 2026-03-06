#University Enrollment system
student_record=[]
with open ("Student records.txt","r") as file:
    for line in file:
        if "|" in line and "Student" not in line:
            data=line.split("|")
            student_id=data[0].strip()
            name=data[1].strip()
            credit=int(data[2].strip())
            gpa=float(data[3].strip())
            student_record.append([student_id,name,credit,gpa])
def calc_avg():
    total=0
    for record in student_record:
        total+=record[3]
    avg=total/len(student_record)
    return avg
    
def academic_standing(student_record):
    stud_id=input("Enter your student ID:")
    for student in student_record:
        if stud_id==student[0]:
            gpa=student[3]
            print(f"{student[1]} has a GPA of {gpa}")
        
            if gpa>=3.5:
                print("Academic Standing:Dean's list")
            elif gpa>=2.0:
                    print("Academic Standing:Satisfactory")
            else:
                print("Academic Standing:Academic probation")
            return
    print("Invalid Student ID")
        
while True:
    print("=========University Enrollment system=========")
    print("1.View all students")
    print("2.Calculate Average GPA")
    print("3.Check Academic Standing")
    print("4.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        try:
            with open ("Student records.txt","r") as file:
                print(file.read())
        except FileNotFoundError:
            print("File is not found")
    elif choice==2:
        avg=calc_avg()
        print(f"The average GPA of all students is: {avg:.2f}")
    elif choice==3:
        academic_standing(student_record)
    elif choice==4:
        print("Exiting system.Goodbye!")
        break


