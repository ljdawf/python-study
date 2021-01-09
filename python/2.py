for i in range(100,1000):
    sum = 0
    temp = i
    while temp:
        sum = sum + (temp%10)*(temp%10)*(temp%10)
        temp = int(temp/10)
    if sum == i:
        print(i)