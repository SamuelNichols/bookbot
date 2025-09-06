import sys
from textwrap import dedent, indent
from stats import count_words, count_chars

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def pretty_print_counts(counts):
    counts_sorted = {k: v for k,v in sorted(counts.items(), key=lambda char: -char[1])}
    output = ""
    
    def show(ch):
        if ch == " ": return "<space>"
        if ch == "\t": return "<tab>"
        if ch == "\n": return "<newline>"
        return ch
    
    for k, v in counts_sorted.items():
        output += f"{show(k)}: {v}\n"
    return output
    
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
        
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    word_count = count_words(book_text)
    char_dict = count_chars(book_text)
    pretty_printed_char_dict = pretty_print_counts(char_dict)
    
    header = dedent(f"""\
    ============ BOOKBOT ============
    Analyzing book found at {filepath}...
    ----------- Word Count ----------
    Found {word_count} total words
    --------- Character Count -------
    """)
    
    report = header + pretty_printed_char_dict
    print(report)
    
    
main()