def open_book():    
    try:
        with open("books/frankenstein.txt") as f:
            file_contents = f.read()
            return file_contents
    except FileNotFoundError:
        print("File not found.")

def count_words(file_contents):
    if file_contents == None:
        return "File contents returned None."
    else:
        words = file_contents.split()
        return len(words)

def character_count(file_contents):
    character_dict = {}
    if file_contents == None:
        return "File contents returned None"
    else:
        for char in file_contents.lower():
            if char.isalpha():
                if char in character_dict:
                    character_dict[char] += 1
                else:
                    character_dict[char] = 1
    return character_dict

def convert_dict_to_list(char_dict):
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char": char, "count": count})
    return char_list

def sort_on(dict):
    return dict["count"]

def main():
    file_contents = open_book()
    word_count = count_words(file_contents)
    char_dict = character_count(file_contents)
    char_list = convert_dict_to_list(char_dict)
    char_list.sort(reverse=True, key=sort_on)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    for char_data in char_list:
        print(f"The '{char_data['char']}' character was found {char_data['count']} times")
    print("--- End report ---")

main()
