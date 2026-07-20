def findlcs(s1,s2,i,j,a):
    if i== len(s1) or j==len(s2):
        return 0 
    if a[i][j]!=-1:
        return a[i][j]
    if s1[i] == s2[j]:
        a[i][j] =  1+ findlcs(s1,s2,i+1,j+1,a)
        return a[i][j]
    else:
        a[i][j] = max(findlcs(s1, s2, i+1, j, a), findlcs(s1, s2, i, j+1, a))
        return a[i][j]



def lcs(s1,s2):
    a = [[-1] * len(s2) for _ in range(len(s1))]
    return findlcs(s1,s2,0,0,a)


print(lcs("bd","abcd"))
