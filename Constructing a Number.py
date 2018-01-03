
def canConstruct(a):
    # Return "Yes" or "No" denoting whether you can construct the required number.
    arr=[]
    for i in range(len(a)):
        if len(str(a[i])) > 1:
            value = str(a[i])
            if len(value) > 1:
                for j in range(len(value)):
                    arr.append(value[j])
            if len(value) == 1:
                arr.append(value)
        if len(str(a[i])) == 1:
            arr.append(a[i])
    num = 0
    k = 0
    while k < len(arr):
        num = num + int(arr[k])
        k = k + 1
    if num%3 == 0:
        return "Yes"
    else:
        return "No"
            
if __name__ == "__main__":
    t = int(raw_input().strip())
    for a0 in xrange(t):
        n = int(raw_input().strip())
        a = map(int, raw_input().strip().split(' '))
        result = canConstruct(a)
        print result
