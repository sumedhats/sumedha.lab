# Program to count the frequency of each word in a sentence

def word_count():
    # Get the sentence from the user
    sentence = input("Enter a sentence: ")

    # Convert the sentence to lowercase to make the word count case-insensitive
    sentence = sentence.lower()

    # Split the sentence into words (splitting by spaces)
    words = sentence.split()

    # Count the frequency of each word using a dictionary
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    # Calculate the total number of words
    total_words = len(words)

    # Display the total word count and the frequency of each word
    print(f"Total word count: {total_words}")
    print("Word frequencies:")
    print(word_freq)

# Call the function to execute
word_count()

