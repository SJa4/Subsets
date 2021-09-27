import itertools
def allcomb(a_list):
    all_combinations = []
    for r in range(len(a_list) + 1):
        combinations_object = itertools.combinations(a_list, r)
        for i in combinations_object:
            all_combinations.append(i)
    j=[]
    for i in all_combinations:
        j.append(list(i))
    return j

#static input
k=allcomb([4,7,8,2,3])

print(k)




