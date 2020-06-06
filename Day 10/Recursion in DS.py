def recursive_multiply(x, y):
    if y==1:
        return x
    else:
        return x+recursive_multiply(x,y-1)
print(recursive_multiply(5,3))

vowels = "aeiou"

def iterative_count_consonants(input_str):
    consonant_count = 0
    for i in range(len(input_str)):
        if input_str[i].lower() not in vowels and input_str[i].isalpha():
            consonant_count += 1
    return consonant_count

def recursive_count_consonants(input_str):
    if input_str == '':
        return 0

    if input_str[0].lower() not in vowels and input_str[0].isalpha():
        return 1 + recursive_count_consonants(input_str[1:])
    else:
        return recursive_count_consonants(input_str[1:])

input_str = "abcde"
print(input_str)
print(iterative_count_consonants(input_str))
input_str = "Hello, How are you?"
print(input_str)
print(recursive_count_consonants(input_str))
