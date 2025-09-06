def count_words(book_text):
    return len(book_text.split())

def count_chars(book_text):
    counts = {}
    for c in book_text.lower():
        counts[c] = counts.get(c, 0) + 1
    return counts 