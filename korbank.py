import math
#Zadanie 1 n liczb ciagu Fibonacciego

def fib(n):
    if n==1:
        return [0]
    elif n==2:
        return [0,1]
    else:
        lst=[0,1]
        while len(lst)<n:
            lst.append(lst[-2]+lst[-1])
        return lst

print(fib(10))

#Zadanie 2 Posortuj liczby rosnaco wedlug czesci ulamkowej


def sortuj(lst):
    #Największy przechodzi do prawej strony
    #Za kazdym razem zaczym od kolejnego indeksu, ale zawsze ide do konca
    for j in range(len(lst)-1):
        for i in range(len(lst)-(j+1)):
            if (lst[i]-math.floor(lst[i]))>(lst[i+1]-math.floor(lst[i+1])):
                lst[i],lst[i+1]=lst[i+1],lst[i]
    return lst


print(sortuj([1.9,2.22,9.1,2.2]))
print(sortuj([2.22,9.1,2.2,1.9]))
print(0.22>0.2)


#Zadanie 3 Zwroc posortowana liste wartosci bezwzglednych bez powtorzen.
#np [-1,-2,-3,0,1,3,2] ma zwrocic  [0,1,2,3]

def sort_bez_pow(lst):
    l = [abs(i) for i in lst]
    l = set(l)
    l = sorted(l)
    return l

print(sort_bez_pow([-1,-2,-3,0,1,3,2]))
