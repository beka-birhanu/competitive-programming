def countSwaps(a):
    # Write your code here
    swaps = 0
    for i in range(len(a)-1):
        for j in range(i,len(a)):
            if a[i] > a[j]:
                x = a[i]
                y = a[j]
                a[j] = x
                a[i] = y
                swaps+=1

    print(f'Array is sorted in {swaps} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[-1]}')
