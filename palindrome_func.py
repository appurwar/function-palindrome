

def longest_palindrome(input):
    
    maxLength = 1
    start = 0
    length = len(input)
    print(length)

    low = 0
    high = 0

    for i in range(1, length):

        # Case 1 - Even Length

        low = i - 1
        high = i

        while low >= 0 and high < length and ((input[low].lower() \
            == input[high].lower()) or (input[low].isspace() == True \
            and input[high].isspace() == True)):
            if high - low + 1 > maxLength:
                start = low
                maxLength = high - low + 1
            low = low - 1
            high = high + 1
            
        # Case 2 - Odd Length 
        low = i - 1
        high = i + 1

        while low >= 0 and high < length and ((input[low].lower() \
            == input[high].lower()) or (input[low].isspace() == True \
            and input[high].isspace() == True)):
            if high - low + 1 > maxLength:
                start = low
                maxLength = high - low + 1
            low -= 1
            high += 1
    print(start)
    print(maxLength)
    if maxLength - start == 1:
        return ""
    else:
        return input[start:start + maxLength]



			
