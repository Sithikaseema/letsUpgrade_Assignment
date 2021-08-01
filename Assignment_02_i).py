n=int(input("Enter the number of elements in list:"))
lst=[]
for i in range(n):
         item=input()
         lst.append(item)
print(lst)
element=input("Enter the element to be deleted:")
count=lst.count(element)
for i in range(count):
          lst.remove(element )
print("The list after deleting the element ",element)
print(lst)
