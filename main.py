def main ():
    file_contents = get_content("books/frankenstein.txt")
    word_count = count_words(file_contents)
    print(word_count)
    chars = count_chars(file_contents)
    print(chars)

def count_words (long_string:str):
    arr = long_string.split()
    return len(arr)

def get_content (path:str):
    file_contents = None
    with open (path,"r") as f:
        file_contents = f.read()
    return file_contents

def count_chars (long_sting:str):
    lower_case_str = long_sting.lower()
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    chars = {}
    for letter in alphabet:
        chars[letter] = lower_case_str.count(letter)
    return chars

main()