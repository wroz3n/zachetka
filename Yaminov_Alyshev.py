import math as m
# 1
def addition_first(n: int) -> float:
    summation = 0
    for i in range(1, n + 1):
        summation = summation + m.sqrt(m.fabs(m.pow(2, i) * m.log(i + 1) * m.log(i + 2, 3)))
    return summation

# 2
def addition_two(n: int) -> float:
    sum = 0 
    for i in range(1, n):
        sum += (m.log1p(i) + m.factorial(i) * m.log(i+1, 0.4) * m.log(i, 2))
    return sum

# 3
def addition_three(n: int) -> float:
    sum = 0
    for i in range(1, n+1):
        sum += m.pow(m.log2(i) * m.pow(3, i - 1) + i * m.log1p(2), 1/3)
    return sum

# 4
def addition_four(n: int) -> float:
    sum = 0
    for i in range(1,n):
        sum += m.log1p(i + 1) / (m.log10(i + 2) + m.log(i + 3, 7))
    return sum

# 5
def addition_five(n: int) -> float:
    sum = 0
    for i in range(1, n + 1):
        sum += m.pow(m.exp(i) + m.log1p(i) * m.log(i + 1, 5),2)
        return sum

## Арифметические произведения:
# 1
def multiplication_f(n: int) -> float:
    sum = 1
    for i in range(1, n + 1):
        sum *= m.sqrt(m.fabs(m.pow(2, i) * m.log(i + 1) * m.log(i + 1)* m.log(i + 2, 3)))
    return sum

# 2
def multiplication_two(n: int) -> float:
    sum = 1
    for i in range(1, n + 1):
        sum *= (3 * m.log2(i + 2) - (m.exp(-i) / m.log(i+1)) + 2**1-2**i)
    return sum

# 3
def multiplication_three(n : int) -> float:
    sum = 1
    for i in range(1,n+1):
        sum *= m.sqrt( m.fabs( (m.pow(5, i+1) / m.pow(i,3))  + m.log1p(i*2) - m.factorial(i) ) )
    return sum

# 4
def multiplication_four(n : int) -> float:
    sum = 1
    for i in range(1,n+1):
        sum *= m.log1p(i+1) * m.exp(i/7) * addit(i)
    return sum
def addit(k : int) -> float:
    addits = 0
    for i in range(1,k+2):
        addits += (1/k)
    return addits


# 5
def multiplication_five(n : int) -> float:
    sum = 1
    for i in range(1,n+1):
        sum *= (addit1(i) * m.log2(i+2))
    return sum
def addit1(k : int) -> float:
    addits = 0
    for i in range(1,k+3):
        addits += (m.log1p(k+1))
    return addits
