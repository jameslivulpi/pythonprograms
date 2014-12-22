


def ff(mydict):
  keylist = []
  for value in mydict.values():
    keylist.append(value)
  keylist.sort()
  for value in keylist:
    print(mydict[value])








##def delete(adict):
##  newdict = {}
##  for k, v in adict.items():
##    newdict[k] = v
##  for k, v in newdict.items():
##    if v < 0:
##      del adict[k] 
##      
      

      
      
  
   

  
##def negativedouble(myList):
##  result = []
##  for item in myList:
##    if item < 0:
##      item *= 2
##    result.append(item)
##      
##  return result
    
    
def main():
  adict = {3:"aa",1:"bb",4:"cc",6:"tt",0:"gg"}
  ff(adict)
  
 
  
  
  
  


  
##  adict = {3:"aa",1:"bb",4:"cc"}
##  arrange(adict)

##  dict = {"aa":-3,"bb":0,"cc":-4}
##  deletenegative(dict)
##  print(dict)
main()

  
  
  
  
  


