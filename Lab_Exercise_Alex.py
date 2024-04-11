import re
from collections import Counter

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

STOP_WORDS = ['a', 'an', 'the', 'etc.']
def count_words(text):
    words = re.findall(r'\w+', text.lower())
    words = [word for word in words if word not in STOP_WORDS]
    return Counter(words)
def top_10_words(word_count):
    return word_count.most_common(10)

file_path = 'Lincoln.txt'
text = read_file(file_path)
word_count = count_words(text)

# Find the top 10 words
top_words = top_10_words(word_count)

# Print the top 10 words and their counts
for word, count in top_words:
    print(f'{word}: {count}')
