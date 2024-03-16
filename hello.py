def deplacer(T,k):

    big = []
    smol = []
    for i in range(len(T)):
        if T[i] < k : 
            smol.append(T[i])
        if T[i] > k :
            big.append(T[i])
    T.clear()
    T.extend(smol)
    T.extend(big)


    

lst = [7,1,3,85,63,24,55,39,8,2,5,8,9,848,8,9,51]
deplacer(lst,20)
print(lst)