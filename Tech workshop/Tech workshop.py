members=[]
def reg_mem():
    while True:
        name=input("Enter participant name:")
        if name in members:
            print(f"{name} has been registered already")
            continue
        club_m=input("Are you a club member(Y/N):").capitalize()
        age=int(input("Enter your age:"))
        if club_m=="Y" and 16<=age<=35:
            members.append(name)
            print(f"{name} has been registered succesfully")
        elif club_m=="N":
            print("Registration failed.Only club members can register")
        elif 16>age or age>35:
            print("Registration failed. Age must be between 16 and 35")
            break
def seat(members):
        if len(members)==0:
            print("The queue is empty")
        else:
            removed=members.pop(0)
            print(f"{removed} has been assigned a seat and removed from the queue.")
    
def search(members):
    name=input("Enter your name:")
    if name in members:
        i=members.index(name)
        print(f"{name} is in position {i+1}")
    else:
        print("Name not found")
def queue(members):
    if len(members)==0:
        print("Queue is empty")
    else:
        print("Registered participants")
        for i in range (len(members)):
            print(f"{i+1}){members[i]}")

print("Tech workshop seat reservation")
while True:
    print("1.Register Participant")
    print("2.Assign seat")
    print("3.Search Participant")
    print("4.View Registration Queue")
    print("5.Exit")
    choice=int(input("Enter your choice:"))
    
    if choice==1:
        reg_mem()
    elif choice==2:
        seat(members)
    elif choice==3:
        search(members)
    elif choice==4:
        queue(members)
    elif choice==5:
        print("Exiting the system")
        break
    else:
        print("Invalid choice")




        

            
