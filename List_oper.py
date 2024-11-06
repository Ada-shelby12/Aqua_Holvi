
#PYTHON PROGRAM TO PERFORM LIST OPERATIONS

mylist=[1,2,3,'python','makes learning fun!']
mylist.append(4)
mylist.append(5)
mylist.append(6)
for i in range(7,9):
 mylist.append(i)
print("using append",mylist)
mylist.extend([7,8,9])
print("using extends",mylist)
mylist.insert(3,"hi")
mylist.insert(4,23)
print("using insert",mylist)
mylist.pop(3)
print("using pop()",mylist)
print("********slice operation******")
print(mylist[:4])
print(mylist[2:])
print(mylist[2:4])
print(mylist[:])
print("*********count operation*********")
print(mylist.count(7))
