def solution(s: str):
    numOfParts = 1
    slicePointer = 0
    sliceEnd = 0
    for x in range(1, len(s)):
        if slicePointer < sliceEnd and s[slicePointer] == s[x]:
            slicePointer += 1
        elif slicePointer == sliceEnd:
            if s[slicePointer] == s[x]:
                numOfParts +=1
                slicePointer = 0
            else:
                sliceEnd = x
                slicePointer = 0
                numOfParts = 1
        else:
            sliceEnd = x
            slicePointer = 0
            numOfParts = 1
        print(f'x = {x}, numOfParts = {numOfParts}, slicePointer = {slicePointer}, sliceEnd = {sliceEnd}')
    return numOfParts

