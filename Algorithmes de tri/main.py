

def tri_par_insertion(l):
    for i in range(1, len(l)):
        cle = l[i]
        j = i-1
        print(f"i = {i} , cle = {cle} , j = {j}")
        while j>=0 and cle < l[j]:
            print(f"l[j] = {l[j]}")
            l[j+1] = l[j]
            j -= 1
        l[j+1] = cle
            
l = [5,3,2,7]
tri_par_insertion(l)
print(l) 
