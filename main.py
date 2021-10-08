def solution(userInput):
    small = userInput[0]
    big = userInput[0]

    for i in userInput:
        if i > big:
            big = i
        elif i < small:
            small = i
    print(big)
    print(small)


solution([1,2,3,4,5])