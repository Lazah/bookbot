def main ():
    file_contents = get_content("books/frankenstein.txt")
    word_count = count_words(file_contents)
    chars = count_chars(file_contents)
    chars.sort(reverse=True,key=sort_on)
    print_report(word_count,chars,"books/frankenstein.txt")

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
    result_list = []
    for letter in alphabet:
        char = {}
        char["count"] = lower_case_str.count(letter)
        char["char"] = letter
        result_list.append(char)
    return result_list

def sort_on(dict):
    return dict["count"]

def print_report(total_count:int,char_list:list,book_path:str):
    print(f"--- Begin report of {book_path} ---")
    print(f"{total_count} words found in the document\n")
    for char_dict in char_list:
        print(f"The '{char_dict["char"]}' character was found {char_dict["count"]} times")

    print("--- End report ---")

main()