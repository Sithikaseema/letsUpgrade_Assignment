n=int(input("Enter the number of elements in list:"))
lst=[]
for i in range(n):
         item=input()
         lst.append(item)
print(lst)
print("List sorted in descending order:")
lst.sort(reverse=True)
print(lst)
