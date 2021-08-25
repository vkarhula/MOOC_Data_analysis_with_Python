# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 10:31:44 2020

Exercise 9 (merge)
Suppose we have two lists L1 and L2 that contain integers which are sorted in ascending order. 
Create a function merge that gets these lists as parameters and returns a new sorted list L 
that has all the elements of L1 and L2. So, len(L) should equal to len(L1)+len(L2). 
Do this using the fact that both lists are already sorted. You can’t use the sorted function 
or the sort method in implementing the merge method. You can however use these sorted 
in the main function for creating inputs to the merge function. Test with a couple of examples 
in the main function that your solution works correctly.

Note: In Python argument lists are passed by reference to the function, they are not copied! 
Make sure you don’t modify the original lists of the caller.

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
