# l1=["apple","banana","cherry","mango"]
# l2=[10,20,30,40]
# l3=[True,False]
# l4=list(("jack"))
# l5=list(("jack","john"))

# print(l4)
# print(l5)
# print(l1[0])
# print(l1[0:4])
# print(l1[:4])
# print(l1[0:])
# print(l1[:])
# print(l1[-4:-1])
# print(l1[-1:-4])
# x=len(l1)
# print(x)
# print(type(l1))
# print(type(l1[0]))
# if "apple" in l1:
#     print("Exists")

# l1[1]="Kiwi"
# print(l1)
# l1[1:3]=["Pineapple","Dates","x"]
# print(l1)

# list=["apple","banana","cherry"]
# list[1:2]=["blackcurrent","watermelon"]
# print(list)

# list=["apple","banana","cherry"]
# list[1:3]=["watermelon"]
# print(list)

#insert

# list=["apple","banana","cherry"]
# list.insert(2,"watermelon")
# print(list)

#append

# list=["apple","banana","cherry"]
# list.append("watermelon")
# print(list)

#extend

# list1=["apple","banana","cherry"]
# list2=["mango","pineapple","papaya"]
# list1.extend(list2)
# print(list1)

#remove

# list1=["apple","banana","cherry","banana"]
# list1.remove("banana")
# print(list1)

#pop
# thislist=["apple","banana","cherry"]
# thislist.pop(1)
# print(thislist)

#del
# thislist=["apple","banana","cherry"]
# del thislist[0]
# print(thislist)

# thislist=["apple","banana","cherry"]
# del thislist

#clear
# thislist=["apple","banana","cherry"]
# thislist.clear()
# print(thislist)

#loops
# thislist=["apple","banana","cherry"]
# for x in thislist:
#     print(x)

# thislist=["apple","banana","cherry"]
# for i in range(len(thislist)):
#     print(thislist[i])

# thislist=["apple","banana","cherry"]
# i=0
# while i < len(thislist):
#     print(thislist[i])
#     i=i+1

#list comprehension
# thislist=["apple","banana","cherry"]
# [print(x) for x in thislist]



# fruits=["apple","banana","cherry","kiwi","mango"]
# newlist=[]

# for x in fruits:
#     if "a" in x:
#         newlist.append(x)

# print(newlist)

# fruits=["apple","banana","cherry","kiwi","mango"]
# newlist=[x for x in fruits if "a" in x]

# print(newlist)


#sorting

# thislist=["orange","mango","kiwi","pineapple","banana"]
# thislist.sort()
# print(thislist)

# thislist=[100,50,65,82,23]
# thislist.sort()
# print(thislist)

#sorting based on how close a number is to 50 #customized sort

# def fun(n):
#     return abs(n-50)

# thislist=[100,50,65,82,23]
# thislist.sort(key=fun)
# print(thislist)

#case insensitive

# thislist=["banana","Orange","Kiwi","cherry"]
# thislist.sort(key=str.lower)
# print(thislist)

#write down a program to swap 2 numbers (1st and last numebers)

# def swaplist(li):
#     size=len(li)
#     temp=li[0]
#     li[0]=li[size-1]
#     li[size-1]=temp
#     return li
# li=[12,35,9,56,24]
# print(swaplist(li))

# def swappositions(lis,pos1,pos2):
#     temp=lis[pos1]
#     lis[pos1]=lis[pos2]
#     lis[pos2]=temp
#     return lis
# list =[23,65,19,90]
# pos1,pos2=1,3
# print(swappositions(list,pos1-1,pos2-1))

#declare a list a find sum and average

# list1=[4,9,5,7,6,1]
# sum=0
# for x in list1:
#     sum=sum+x
# print(sum)
# print(sum/len(list1))

#to find first and last element in a list

# list1=[4,9,5,7,6,1]
# sum=0
# for x in list1:
#     sum=sum+x
# print(sum)
# print(sum/len(list1))
# print(list1[0])
# print(list1[len(list1)-1])

#mimimum and maximum

list1=[4,9,5,7,6,1]
sum=0
for x in list1:
    sum=sum+x
print(sum)
print(sum/len(list1))
print(list1[0])
print(list1[len(list1)-1])
list1.sort()
print(list1)
print("minimum ",list1[0])
print("maximum ",list1[len(list1)-1])






    





