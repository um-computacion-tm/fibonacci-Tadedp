def fibonacciIterative(num):
    if num <= 1:
        return num
    else:
        result = [0,1]
        for i in range(2, num + 1):
            result.append(result[i-2] + result[i-1])
        return result[-1]
    
if __name__ == '__main__':
    pass