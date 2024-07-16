item = ["Apple", "Banana", "Cat", 2003, 95.6, True, "Madhvi", "Rama"]
item.append("Piyush")                           # Add new element at the end of list
print(item)

list1 = [1, 25, 37, 10, 89, 89, 89, 89, 20, 33, 1234, 2]
list1.sort()                                    #sort the list
print(list1)         

list1.pop(1)
print(list1)                                    #remove item on a specific index

list1.reverse()                                 # reverse the list
print(list1)

list1.insert(0, "sona")                         #insert item on a specific index
print(list1)

list1.remove(1)                                 #remove value on the list
print(list1)

list1.extend([1000, 536, 896])                  #add multiple item on the list
print(list1)

index = list1.index(1000)                       # return index value
print(index)

copylist = list1.copy()                         # copy the list
print(copylist)

count = list1.count(89)                         # count the value
print(count)

clear = list1.clear()                           # clear or delete entire list
print(clear)