def mean(a,b):
    return (a+b)/2

def squareRoot(target, low, high):
    """
    P.71 Math adv.
    Input
    -----
        target: float
            Number you want to take the squareRoot
        low: float
            Number you know it's S.R is below the S.R of target
        high: float
            Number you know it's S.R is above the S.R of target
    """
    for i in range(20):
        guess = mean(low,high)
        if guess == target:
            return guess
        elif guess**2>target:
            high = guess
        else:
            low = guess
    return guess

if __name__=="__main__":
    guess = squareRoot(60,7,8)
    print(guess)
