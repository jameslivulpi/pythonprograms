def main():
    n = int(input("Please enter a positve integer: "))
    print(n,end=' ')
    seq = syracuse(n)
    for num in seq:
        print(num,end=' ')
    

def syracuse(n):
    retval =[]
    
    while n > 1:
        if n % 2 == 0:
            nextnum = n//2
        else:
            nextnum = 3 * n +1
        n = nextnum
        retval.append(nextnum)
    return retval 

if __name__ == '__main__':
    main()

