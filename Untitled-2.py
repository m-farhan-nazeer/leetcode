

def is_eqaution(x,y,n):
    x_dev = devisor(x)
    y_dev = devisor(y)
    maxi = 0
    for i in range(len(x_dev)):
        if x_dev[i] in y_dev and x_dev[i]> maxi:
            maxi = x_dev[i]
    if maxi == 0 and n == 0:
        return True
    if  maxi != 0 and  n % maxi  == 0:
        return True
    return False

def devisor(x):
    val = []
    for i in range(1,x+1):
        if x%i == 0:
            val.append(i)
    return val

    

def main():
    arr = []

    j = int(input())
    cheked = []
    sol = []
    for i in range(j):
        a, b = map(int, input().split())
        arr.append((a, b))

    for x in range(len(arr)):
        n,m = arr[x]
        count = 0
        for i in range(m+1):
            for j in range(m+1):
                for k in range(m+1):
                    x = (i^j)
                    y = (j^k)
                    if x == 0 and y == 0:
                        if n == 0:
                            count += 1
                    elif x == 0:
                        if n % y == 0:
                            count += 1
                    elif y == 0:
                        if n % x == 0:
                            count += 1
                    else:
                        if (x,y,n) in sol:
                            count += 1
                        else :
                            if is_eqaution(x, y, n):
                                count += 1
                                sol.append((x,y,n))
        print(count)

main()