import sys
import math
import numpy as np
import matplotlib.pyplot as plt


def sieve_1(nmax):
    ''' First method of implementing Eratosthenes' sieve algorithm
    '''

    all_primes = []

    if nmax == 2: 
        all_primes = [2]
    else:
        primes_head = [2]
        first = 3
        primes_tail = np.arange(first,nmax+1,2)
        while first <= round(math.sqrt(primes_tail[-1])):
            first = primes_tail[0]
            primes_head.append(first)
            non_primes = first * primes_tail
            primes_tail = np.array([ n for n in primes_tail[1:]
                                    if n not in non_primes ])

    all_primes = primes_head + primes_tail.tolist()
    return all_primes

def sieve_2(nmax):
    
    ''' Second method of implementing Eratosthenes' sieve algorithm
    '''

    all_primes = []

    if nmax == 2: 
        all_primes = [2]

    else:

        primes_head = [2]
        first = 3

        # The primes tail will be kept both as a set and as a sorted list
        primes_tail_lst = range(first,nmax+1,2)
        primes_tail_set = set(primes_tail_lst)

        # Now do the actual sieve
        while first <= round(math.sqrt(primes_tail_lst[-1])):
            # Move the first leftover prime from the set to the head list
            first = primes_tail_lst[0]
            primes_tail_set.remove(first)  # remove it from the set
            primes_head.append(first) # and store it in the head list

            # Now, remove from the primes tail all non-primes.  For us to be able
            # to break as soon as a key is not found, it's crucial that the tail
            # list is always sorted.
            for next_candidate in primes_tail_lst:
                try:
                    primes_tail_set.remove(first * next_candidate)
                except KeyError:
                    break

            # Build a new sorted tail list with the leftover keys
            primes_tail_lst = list(primes_tail_set)
            primes_tail_lst.sort()

        all_primes = primes_head + primes_tail_lst

    return all_primes


def get_primes(nmax):
    ''' Returns outputs of both implementations of sieve algorithms
    '''
    return sieve_1(nmax), sieve_2(nmax)


def proportion_primes(all_nmax):
    ''' returns proportion of prime numbers found from sieve algorithm
    '''
    
    all_proportions = []

    for nmax in all_nmax:

        all_primes = []

        if nmax == 2: 
            all_primes = [2]

        else:

            primes_head = [2]
            first = 3

            # The primes tail will be kept both as a set and as a sorted list
            primes_tail_lst = range(first,nmax+1,2)
            primes_tail_set = set(primes_tail_lst)

            # Now do the actual sieve
            while first <= round(math.sqrt(primes_tail_lst[-1])):
                # Move the first leftover prime from the set to the head list
                first = primes_tail_lst[0]
                primes_tail_set.remove(first)  # remove it from the set
                primes_head.append(first) # and store it in the head list

                # Now, remove from the primes tail all non-primes.  For us to be able
                # to break as soon as a key is not found, it's crucial that the tail
                # list is always sorted.
                for next_candidate in primes_tail_lst:
                    try:
                        primes_tail_set.remove(first * next_candidate)
                    except KeyError:
                        break

                # Build a new sorted tail list with the leftover keys
                primes_tail_lst = list(primes_tail_set)
                primes_tail_lst.sort()

            all_primes = primes_head + primes_tail_lst

        all_proportions.append(len(all_primes) / nmax)
        
    return all_proportions