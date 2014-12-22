#!/usr/bin/env python3

# James Livulpi
# November 25th 2013
# List Functions


from random import *

def count(myList, x): 
    count = 0
    for item in myList:
        if item == x:
            count += 1
    return count
            
def isin(myList, x): 
    item = 0
    while item < len(myList):
        item += 1
        if item == x:
            return True
    return False

def index(myList, x):
    for i in range(len(myList)):
            if myList[i] == x:
                return i
            
    raise ValueError()

def reverseModify(myList):
    length = len(myList)
    for i in range(length // 2):
        myList[i], myList[length - i - 1] = myList[length - i - 1], myList[i]
    
def reverseReturnNew(myList): 
    newlist = []
    for i in range(1, len(myList) + 1):
        newlist.append(myList[-i])
    return newlist

def shuffleModify(myList): 
    i = len(myList)
    while i  > 1:             
        i = i - 1
        index = randrange(i)
        myList[index], myList[i] = myList[i], myList[index]

def innerProduct(list1, list2): 
    count = 0
    for i in range(len(list1)):
        count += list1[i] * list2[i]
    return count

def removeDuplicatesModify(myList):
    max = len(myList)
    i = 0
    while i < max - 1:
        if myList[i] == myList[i + 1]:
            del myList[i + 1]
            max = max - 1
        else:
            i = i + 1

def removeDuplicatesReturnNew(myList): 
    newlist = []
    for item in myList:
        if item not in newlist:     
            newlist.append(item)
    return newlist

def main():
    list = [1, 2, 2, 2, 4, 5, 8, 10]
    x = 2
    number = count(list, x)
    print("In the list", list, x, "occurs", number, "times")
    trueOrFalse = isin(list, x)
    print("Is", x, "in", list, trueOrFalse)
    number = index(list, x)
    print("In the list", list, x, "is at index", number)
    myList = [1, 2, 2, 2, 4, 5, 8, 10]
    reverseModify(list)
    print("The list", myList, "gets reversed and modified to", list)
    x = reverseReturnNew(myList)
    print("The list", myList, "gets reversed and returns a new list", x)
    shuffleModify(myList)
    print("The list", list, "gets shuffled and modified to", myList) 
    list1 = [2, 4, 6, 8]
    list2 = [3, 6, 9, 12]
    x = innerProduct(list1, list2)
    print("The inner product of the lists", list1, "and", list2, "is", x)
    removeDuplicatesModify(list)
    print("The list", myList,
          "will be removed of duplicates and modified to", list) 
    x = removeDuplicatesReturnNew(list)
    print("The list", myList,
          "will be removed of duplicates returning a new list", x)

if __name__ == '__main__':
    main()







    
    
