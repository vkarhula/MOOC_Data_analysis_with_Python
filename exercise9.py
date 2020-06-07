# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 10:31:44 2020

@author: OMISTAJA
"""

"""
def merge(*lst):
    lst3 = []
    print(*lst)
    lst1 = sorted(lst[0])
    lst2 = sorted(lst[1])
    for i in range(0,len(lst1)):
        lst3.append(lst1[i])
    for i in range(0,len(lst2)):
        lst3.append(lst2[i])
    print(lst3)
    print(sorted(lst3))
"""

def merge(*lst):
    lst3 = []
    # Print original lists
    print(f"\n\nOriginal list are: ")
    print(*lst)
    lst1 = (lst[0])
    lst2 = (lst[1])
    len_orig_lst1=len(lst1)
    lst3 = lst1
 
    i = 0
    j = 0
    while j <= len(lst2)-1:
        #print(f"while alkaa ({i},{j})")
        #print(f"len(lst3)={len(lst3)}")
        #print(f"({i},{j}),\t{lst3}")
        # If lst3 item is smaller than lst2, only increase index i
        # If lst3 is at last item, add lst2 items to the end of lst3 
        # if there are some left
        if lst3[i] <= lst2[j]:
            #print(f"({i},{j}),({lst1[i]},{lst2[j]}) if {lst1[i]} <= {lst2[j]}")
            # If last of lst2 are bigger than last of lst1, add them
            if i==len(lst3)-1:
                #print("**** if i==len(lst3):")
                lst3.append(lst2[j])
                j=j+1
            else:
                # In the middle of the lst3, move comparison to next lst3 item
                i=i+1
            #print(f"({i},{j})*\t{lst3}")
        else:
            # Insert lst2 items in the middle of lst3
            #print(f"({i},{j}),({lst1[i]},{lst2[j]}) else insert {lst2[j]}, indeksiin {i}")
            lst3.insert(i, lst2[j])
            j=j+1
            #print(f"({i},{j})INSERT \t{lst3}")
    
    print("Sorted list: ")
    print(f"{lst3}")
    print(f"\nOriginal lists were size of {len_orig_lst1} and {len(lst2)}.")
    print(f"Sorted list has {len(lst3)} items.")
    

L1 = [1,3,7,5]
L2 = [2,4,8,6,10]    
merge(sorted(L1),sorted(L2))

L1=[1,1,9,4,7,7]
L2 = [2,4,8,2,10] 
merge(sorted(L1),sorted(L2))   


#help(list)