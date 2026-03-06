records=[]
members=[]
try:
    with open ("Tech record.txt","r") as file:
        for line in file:
            data=line.split(",")
            name=data[0].strip()
            club_mem=data[1].strip()
            age=int(data[2].strip())
            records.append([name,club_mem,age])
except FileNotFoundError:
    print("File is not found")

def reg_mem():
    for record in records:
        name=record[0]
        club_mem=record[1]
        age=record[2]
        if name in members:
            print(f"{name} is already registered")
        elif club_mem=="Y" and 16<=age<=35:
            members.append(name)
            print(f"{name} has been registered successfully")
        elif club_mem=="N":
            print(f"Registration failed for {name}.Only club members can register")
        else:
            print(f"Registration failed for {name}. Age must be between 16 and 35")
def seat(members):
    if len(members)==0:
        print("The queue is empty")
    else:
        removed=members.pop(0)
        print(f"{removed} has been assigned a seat and removed from the queue.")
        print(f"Remaining members {len(members)}")
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
        

        