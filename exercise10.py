# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 14:01:02 2020

@author: OMISTAJA
"""


def detect_ranges(*lst):
    #print(lst)
    # Moving data to list and sorting it
    LS = []
    ra = []
    tuple = (0,0)
    for i in range(0,len(lst)):
        LS.append(lst[i])
    LS.sort()
    print(f"Sorted list is: {LS}")
    #print("Sorted list is: {}".format(LS))
    #print(len(LS))
    
    j = 0
    a = LS[0]
    b = LS[0+1]
    for i in range(0,len(LS)):
        #print(i,LS[i])
        
        # Viimeinen indeksi, kirjoitetaan single tai range alas
        if i==len(LS)-1:
            #print("loppuu, kirjoita range alas")
            if j==0:
                # tallenna viimeinen luku
                ra.append(LS[i])
            else:
                # tallenna range
                start = LS[i-j]
                end = (LS[i]+1)
                tuple = (start,end)
                ra.append(tuple)
            break
            
            
        a = LS[i]
        b = LS[i+1]
        
        # range loppuu, tallennus
        if a+1 != b:
            if j==0:
                # tallenna viimeinen luku
                #print(F"range loppuu, kirjoita [{LS[i]})")
                ra.append(LS[i]) #-j?
            else:
                # tallenna range
                start = LS[i-j]
                end = (LS[i]+1)
                tuple = (start,end)
                #print(F"range loppuu, kirjoita [{tuple})")
                ra.append(tuple)
            #print("range alkaa, j=0")
            j = 0
        
        # range alkaa tai rangen sisällä
        elif a+1 == b:
            j = j + 1 # kierrokset rangen alusta, jäljitetään alkuarvo
            
    #print(ra)
    return ra
    
L = [2,5,4,8,12,6,7,10,13]
print(L)

print(detect_ranges(*L))
