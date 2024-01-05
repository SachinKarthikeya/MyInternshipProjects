def count_words(paragraph):
    words = paragraph.split()
    return len(words)

paragraph = input("Enter a text or a paragraph:")
word_count = count_words(paragraph)
print(f"Number of words in the given paragraph are: {word_count}")