def solution(A):

    Asorter = A
    
    #sort least to largest
    Asorter.sort()
    
    #initiate empty array to store unique values (sorted)
    Asort = []

	#loop through values for unique values
    for i in Asorter:
        if i not in Asort:
            Asort.append(i)
    
    #all negative integers
    if max(Asort) <= 0:
    	answer = 1
    
    #positive integers
    for j in range(1,1000000):
    	if j not in Asort:
    		answer = j
    		break
    
    #yield results
    print answer
    return answer

   
#Test Examples
A = [1,2,3,4,5,6,7,9]
solution(A)

A = [-2,-4,-5]
solution(A)

A = [-1000000]
solution(A)

A = [1000000]
solution(A)

A = [0,100]
solution(A)
