import re

def count_words(text):
    words = re.findall(r'\b\w+\b', text)
    return len(words)

if __name__ == "__main__":
    text = input("Enter your text: ")
    word_count = count_words(text)
    print(f"The number of words in the text is: {word_count}")
