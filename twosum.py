'''Find two values in an array that sums up to a target value.'''

A = [-2, 1, 2, -5, -1, 4, 7, 10, 11]
target = 9




def twosum(A, target):
    '''Start of the array'''
    i = 0
    '''end of the array'''
    j = len(A) - 1
    '''Sorting the array'''
    A.sort()
    print(sorted(A))

    '''Looping through the array till the condition is met.'''
    while i <= j:
        if A[i] + A[j] == target: 
            print(i, j)
            '''if there is more than one solution we want the loop to continue'''
            i += 1
            continue
            return True
        elif A[i] + A[j] < target:
            i += 1 
        else: # A[i] + A[j] > target
            j -= 1
    return False


'''Print the answer'''
print(twosum(A, target))

'''Further improvements'''
'''The solution prints false, even though there are possible solutions. The program should print true.'''
