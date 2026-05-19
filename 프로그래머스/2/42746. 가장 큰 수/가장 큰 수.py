def solution(numbers):
    numbers = list(map(str, numbers))
    
    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        
        pivot = arr[0]
        left, right = [], []
        
        for x in arr[1:]:
            if x + pivot > pivot + x:
                left.append(x)
            else:
                right.append(x)
        
        return quick_sort(left) + [pivot] + quick_sort(right)
    
    numbers = quick_sort(numbers)
    answer = ''.join(numbers)
    
    if answer[0] == '0':
        return '0'
    
    return answer