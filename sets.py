#!/usr/bin/env python3

# James Livulpi
# December 2nd 2013
# Sets

class Set:
    def __init__(self, elements=[]):
        self.dict = {}
        for item in elements:
            self.dict[item] = True

    def addElement(self, x):
        self.dict[x] = True

    def deleteElement(self, x):
        del self.dict[x]

    def member(self, x):
        if x in self.dict:
            return True
        else:
            return False

    def intersection(self, set2):
        result = {}
        for i in self.dict:
            if set2.member(i) == True:
                result[i] = True
        return result

    def union(self, set2):
        result = {}
        for i in set2.dict:
            result[i] = True
        for j in self.dict:
            result[j] = True
        return result

    def subtract(self, set2):
        result = {}
        for i in self.dict:
            if set2.member(i) == False:
                result[i] = True
        return result

    def print(self):
        print(self.dict)
        
def main():
    set1 = Set([1,4,3])
    set2 = Set([1,8,12])
    set1.addElement(10)
    set1.print()
    set1.deleteElement(10)
    set1.print()
    print(set1.member(12))
    print(set1.intersection(set2))
    print(set1.union(set2))
    print(set1.subtract(set2))
    
    

   
    

    
    
    
   
   


   
 


    
    
    
    
    
    
main()    
    
    

    
    
            
                
            
            
        
        
        
    
