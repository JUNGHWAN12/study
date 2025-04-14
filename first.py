def AND(x1, x2):
    w1, w2 = 0.5, 0.5
    b = -0.7
    tmp = x1 * w1 + x2 * w2 + b
    if tmp <= 0:
        return 0
    else:
        return 1
print(AND(0,0))
print(AND(1,0))
print(AND(0,1))
print(AND(1,1))