###REVIEW QUESTIONS WITH A CHANGE 




####DOUBLES EVERY OTHER INT IN ALIST

##def doublelist(alist):
##    for i in range(1,len(alist),2):
##        alist[i] *= 2

def doublelistReturnNew(alist):
    result = []
    for item in alist[::2]:
        result = item * 2
    return result
##
######converts strings to interger
##new_numbers = []
##for i in numbers:
##    new_numbers.append(int(n))
##numbers = new_numbers

##def areacod(adict):
##    for k, v in adict.items():
##        adict[k] = "518-" + v






def main():
##    adict = {"tom":"344-1111"}
##    areacod(adict)
##    print(adict)

##    
##    alist = [1,2,3,4,4,5,5,6,7]
##    doublelist(alist)
##    print(alist)
    alist = [1,2,3,4,5,6,7]
    x = doublelistReturnNew(alist)
    print(x)
    

main()
