# Day 3 - Word Frequency Counter

def word_frequency(text):
    """
    Counts frequency of each word in a text.
    Returns top 5 most common words.
    """
    words = text.lower().split()

    cleaned_words = []
    for word in words:
        clean = word.strip(".,!?;:\"'()[]")
        if clean:
            cleaned_words.append(clean)

    frequency = {}
    for word in cleaned_words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    sorted_words = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

    return sorted_words[:5]


def display_top5(text):
    """Displays top 5 words with their counts."""
    print("--- Word Frequency Counter ---")
    print(f"Input text: {text[:60]}...")
    print()
    top5 = word_frequency(text)
    print("Top 5 most frequent words:")
    for rank, (word, count) in enumerate(top5, 1):
        print(f"  {rank}. '{word}' → {count} times")


sample_text = """
Python is a great programming language. Python is easy to learn.
Python is used for web development, data science, and artificial intelligence.
Many developers love Python because Python is simple and powerful.
Learning Python is one of the best decisions for any developer.
"""

display_top5(sample_text)

print()
sample_text2 = """
Machine learning and deep learning are subsets of artificial intelligence.
Artificial intelligence is transforming the world. Machine learning models
learn from data. Deep learning uses neural networks. Data is the new oil.
Data science combines statistics and machine learning to extract insights from data.
"""

display_top5(sample_text2)