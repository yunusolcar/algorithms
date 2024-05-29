def count(text):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnprstvyzBCDFGHJKLMNPRSTVYZ"

    vowel_count = 0
    consonant_count = 0

    for i in text:
        if i in vowels:
            vowel_count += 1
        elif i in consonants:
            consonant_count += 1

    return vowel_count, consonant_count


# text = input("text: ")
text = "A long time ago in a galaxy far, far away...."
vowels, consonants = count(text)
print(f"Number of vowels: {vowels} ")
print(f"Number of consonants: {consonants}")