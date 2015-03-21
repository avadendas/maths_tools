# Determine whether or not the given set is a difference set.

def getDifferences(s, n):
    '''Find the number of times each differences occurs in s.

    params:
        s - the list of integers, each in range(0, n).
        n - the thing to modulo by.

    returns:
        a list in which the ith entry is the number of times the
        difference i occurs in list s.
    '''
    
    # the ith index stores how many times the difference i occurs
    diffs = n*[0]

    listSize = len(s)
    
    for i in range(listSize):
        for j in range(i+1, listSize):
            d1 = (s[i] - s[j]) % n
            d2 = n - d1
            diffs[d1] = diffs[d1] + 1
            diffs[d2] = diffs[d2] + 1

    return diffs

def differenceIsR(s, n, r):
    '''Determine whether or not s is a difference set modulo n with each
    difference occuring r times.
    
    params:
        s - the list of integers, each in range(0, n).
        n - the thing to modulo by.
        r - the number of times we expect each difference to occur

    returns:
        True if each difference (except 0, of course) occurs r times,
        False otherwise.
        
    '''
    
    diffs = getDifferences(s, n)
    if diffs[0] != 0:
        return False
    
    for i in range(1, len(diffs)):
        if diffs[i] != r:
            return False

    return True

def isDifferenceSet(s, n):
    '''Determine whether or not s is a difference set modulo n.
    
    params:
        s - the list of integers, each in range(0, n).
        n - the thing to modulo by.
        r - the number of times we expect each difference to occur

    returns:
        True if each difference (except 0, of course) occurs r times,
        False otherwise.
        
    '''
    diffs = getDifferences(s, n)
    if diffs[0] != 0:
        return False
    
    theDiff = diffs[1]

    for i in range(2, len(diffs)):
        if diffs[i] != theDiff:
            return False

    return True
    
if __name__ == '__main__':
    theSet = [1, 3, 4, 5, 9]
    print(getDifferences(theSet, 11))
    print(isDifferenceSet(theSet, 11))
