#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the journeyToMoon function below.
def journeyToMoon(n, astronaut):
    countries=[] # list of list of astronauts by country
    astronauts=[i for i in range(n)] # List of all astronauts
    numCountries=0
    for pair in astronaut:
        #print('Processing ',pair)
        belong=[]
        for c in countries:
            if pair[0] in c:
                # first astronaut is in group c
                belong.append(c)
                num=1
                break
        for d in countries:
            if pair[1] in d:
                # second astronaut is in group d
                belong.append(d)
                num=0
                break
        if len(belong)==0:
            # This is a new country
            #print(pair,' contains 2 new astronauts')
            countries.append(pair)
            astronauts.remove(pair[0])
            astronauts.remove(pair[1])
        elif len(belong)==2:
            # Both astronauts belong to a country
            # Are they same country already?
            if belong[0] != belong[1]:
                #print('merging ',belong[0],' and ',belong[1])
                belong[0].extend(belong[1])
                countries.remove(belong[1])
            #else:
            #    #print('%i and %i both belong to country'%(pair[0],pair[1]),belong[0])
        else:
            #print('Adding astronaut',pair[num],'to country',belong[0],'(num=%i)'%num)
            belong[0].append(pair[num])
            astronauts.remove(pair[num])
    #print('Countries:')
    #for c in countries:
    #    print(c)
    #print('Astronauts not listed:',astronauts)
    # I have found the number of combinations for countries with ni astronauts in each
    # is given by ( sum(ni)^2 - sum(ni^2) )/2
    sni=sni2=0
    for c in countries:
        n=len(c)
        sni += n
        sni2+= n*n
    # Now add astronauts not in previous list
    n=len(astronauts)
    sni += n
    sni2+= n # This one is the sum of 1*1+1*1+1*1...
    return (sni*sni - sni2)//2


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    np = input().split()

    n = int(np[0])

    p = int(np[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()

