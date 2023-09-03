def maxFrequency( nums: list[int], k: int) -> int:
    nums.sort()
    k_again = k
    freq = 0
    for i in nums:
        i_freq = nums.count(i)
        x = nums[:nums.index(i)]
        for j in x[::-1]:
            k -= (i-j)
            if k >= 0:
                i_freq += 1
            else:
                break
        k = k_again
        freq = max(freq,i_freq)
    return freq
