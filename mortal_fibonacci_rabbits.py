#!/usr/bin/env python3

"""
n - number of months elapsed (total)
m - number of months rabbits can live

return # of pair of rabbits after nth month

"""

##Not sure that this is correct but it's too slow to do recursion anyway
def mortal_rabbits (n,m):
    if n==0 or n==1:
        return 1
    else: 
        #term 1 
        if n<m:
            return mortal_rabbits(n-1,m) + mortal_rabbits(n-2,m) 
        else: 
            return mortal_rabbits(n-1,m) + mortal_rabbits(n-2,m) - mortal_rabbits(n-m,m)

#print(mortal_rabbits(99,18))


def mortal_rabbits_iter(n,m):
    

    if n==0 or n==1: 
        return 1


    #these values change dynamically
    producing_rabbits = 1
    d0_rabbits=1 #newborns
    d1_rabbits=0 #developing rabbits

    #keep track of the # of newborns that will evenutally die in "m" months
    newborns=[1,0,1]
    for i in range(3,n):

        temp=d0_rabbits

        producing_rabbits += d1_rabbits # Developed rabbits are the new producers

        d0_rabbits = producing_rabbits
        newborns.append(d0_rabbits) #Keeping track of newborns

        d1_rabbits = temp #The old newborns are now developed 


        #dying happens after reproduction
        if i>=m :
                dying_rabbits = newborns[i-m]
                producing_rabbits -=dying_rabbits

        total_rabbits = d0_rabbits + d1_rabbits + producing_rabbits
                    
    return total_rabbits


#print(mortal_rabbits_iter(81,19))






