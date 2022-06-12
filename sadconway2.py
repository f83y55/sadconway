def cnw(st):
    """return next item in a Conway audiodescriptive sequence"""
    res, k = "", 1
    for x, y in zip(st, [*st[1:], None]) :
        if x==y :
            k+=1
        else :
            res += str(k)+x
            k=1
    return res


from math import log as ln
def iteration(st, n, pr=True) :
    """return cnw iterated n times"""
    res = st
    for _ in range(n) :
        re = res
        res = cnw(res)
        if pr :
            print("C_{n} = ", re)
            print("ln(C_{n})/ln(C_{n-1})", ln(int(res))/ln(int(re)))
    return res

def conversion(st):
    """convert a Conway sequence to a 3D path"""
    ech = float(len(st))/3
    path_x, path_y, path_z = [0], [0], [0]
    for el in st :
        if el=='1' :
            path_x.append(path_x[-1]+float(el)/ech)
            path_y.append(path_y[-1])
            path_z.append(path_z[-1])
        if el=='2' :
            path_x.append(path_x[-1])
            path_y.append(path_y[-1]+float(el)/ech)
            path_z.append(path_x[-1])
        if el=='3' :
            path_x.append(path_x[-1])
            path_y.append(path_y[-1])
            path_z.append(path_z[-1]+float(el)/ech)
    return [path_x, path_y, path_z]


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
def plotting(st, n, m):
    """Plot 3d paths from the Conway sequences between n and m"""
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for k in range(n, m) :
        path_x, path_y, path_z = conversion(iteration(st, k, pr=False))
        ax.plot(path_x, path_y, zs=path_z)
    return plt

if __name__ == '__main__' :
    cont = True
    while cont :
        st, n, m = input("Seed ? "), int(input("Iterations min ? ")),  int(input("Iterations max ? "))
        plotting(st, n, m).show()
        cont = not("no"==input("Continue (yes/no) "))
    print("Bye !")
