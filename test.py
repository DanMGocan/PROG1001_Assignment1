import math

def fibMemo(i):
    if i in memo:
        return memo[i]
    if i <= 2:
        return 1;
    else:
        f = fibMemo(i-1) + fibMemo(i-2)
        memo[i] = f
    print('calc', i,  memo)
    return f
memo = {}
# print(fibMemo(900))

def formula_test(fib):
    golden = (1 + 5 ** 0.5) / 2
    theta = 1.618034
    return ( (golden ** fib) - ((1 - golden) ** fib)) / math.sqrt(5)

print(formula_test(1200))