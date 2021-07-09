def my_reverse(array):
    return array[::-1]

def my_reverse2(array):
    n = len(array)
    for i in range(n//2):
        array[i],array[n-1-i] = array[n-1-i],array[i]
    return array

if __name__ == '__main__':
    
    A = [1,2,3,4]
    print(my_reverse2(A))