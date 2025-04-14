def NAND(x1, x2):
    w1 = -0.5
    w2 = -0.5
    b = 0.7
    tmp = x1 * w1 + x2 * w2 + b
    if tmp <= 0:
        return 0
    else:
        return 1
print(NAND(0,0))
print(NAND(1,0))
print(NAND(0,1))
print(NAND(1,1))