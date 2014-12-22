def main():
    while True:
        m,n = eval(input("Please enter two integers separated by a comma: "))
        if (m,n) == (0,0):
            print("The greatest common divisor does not exist.")
            break
        else:
            answer = gcd(m,n)
            print("The greatest common divisor is: ", answer)
        

def gcd(m,n):
    while m != 0:
        n, m = m, n % m
    return abs(n)
        
                

if __name__ == '__main__':
    main()
