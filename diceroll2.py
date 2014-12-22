import random

def rollOneDie():
    return random.randint(1,6)

def rollTwoDice():
    return rollOneDie() + rollOneDie()

def genBar(value, maxval, width):
    return '*' * int(width * (value / maxval))

def rollTwoDiceCombined():
    counts = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(1000):
        combine = rollTwoDice()
        counts[combine] += 1
    return counts
def randomNumber2Through12():
    counts = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(1000):
        randNumber = random.randrange(2,13)
        counts[randNumber] += 1
    return counts
def makeBar(a):
    for i in range(2,13):
        print(i,a[i],'*'*int(20*a[i]/max(a)))
        
def main():
    b = randomNumber2Through12()
    a = rollTwoDiceCombined()
    makeBar(a)
    print()
    makeBar(b)
    
    
main()
        
  


        
    
    
