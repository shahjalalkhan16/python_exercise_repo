input_str = input()
input_str = input_str.lower()

vowels = ['a','e','i','o','u']

for vowel in vowels:
    #print('now in:',vowel)
    count = 0
    for letter in input_str:
        #print(letter)
        if letter == vowels:
            count = count + 1

    print(f'{vowel} is  {count}')