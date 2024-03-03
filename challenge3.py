def solution(N):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # Calculate the number of times each letter should occur
    occurrences_per_letter = N // 26
    remainder = N % 26

    # Create the string with equal occurrences of each letter
    result = alphabet[:remainder] + alphabet * occurrences_per_letter

    return result[:N]
    
    # Usage
print(solution(3))
print(solution(5))
print(solution(20))