def cnw(st):
    """
    return next item in a Conway audiodescriptive sequence
    """
    res, k = "", 1
    for x, y in zip(st, [*st[1:], None]) :
        if x==y :
            k+=1
        else :
            res += str(k)+x
            k=1
    return res


from math import log as ln
def iter(st, n, pr=True) :
    """
    return cnw iterated n times
    """
    res = st
    for _ in range(n) :
        re = res
        res = cnw(res)
        if pr :
            print(ln(int(res))/ln(int(re)))
    return res


if __name__ == '__main__' :
    cont = True
    while cont :
        st, n = input("Seed ? "), int(input("Iterations ? "))
        iter(st, n)
        cont = not("no"==input("Continue (yes/no) "))
    print("Bye !")
