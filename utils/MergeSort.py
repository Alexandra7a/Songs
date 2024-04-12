

def MergeSort(lst,key,cmp):
    """
    Functie de sortare
    :return:
    key=o functie lamda
    """
    if len(lst)==0:
        return
    if len(lst)==1:
        return lst
    mij=len(lst)//2
    stanga=MergeSort(lst[:mij],key,cmp)
    dreapta=MergeSort(lst[mij:],key,cmp)

    i=j=0
    new_list=[]
    while i<len(stanga) and j<len(dreapta):
        if cmp(stanga[i],dreapta[j])==True:#din comparator
            new_list.append(stanga[i])
            i=i+1
        else:
            new_list.append((dreapta[j]))
            j=j+1

    while i<len(stanga):
        new_list.append(stanga[i])
        i = i + 1
    while j<len(dreapta):
        new_list.append((dreapta[j]))
        j = j + 1
    return new_list

