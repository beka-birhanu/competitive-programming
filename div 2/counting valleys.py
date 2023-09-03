def countingValleys(steps, paths):
    # Write your code here
    altitude = 0
    valleys = 0
    movem_bellowSeaLevel = False
    for path in paths:
        if path == 'D':
            altitude -= 1
            if altitude < 0:
                movem_bellowSeaLevel = True
        elif path == 'U':
            altitude += 1
        if altitude == 0 and movem_bellowSeaLevel:
            valleys += 1
            movem_bellowSeaLevel = False
    return valleys
