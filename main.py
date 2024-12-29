def main ():
    with open(r"C:\Users\ayhan\workspace\github.com\AyhanKetre\bookbot\books\frankenstein.txt") as f:
        file_contents = f.read()
    report(file_contents)

def word_count(book):
    words= book.split()
    return len(words)

def count_letters(book):
    low_book= book.lower()
    d={}
    for x in low_book:
        if x in d:
            d[x] = d[x] + 1
        else:
            d[x] = 1
    return d

def sort_on(dict):
    return dict["num"]

def report(book):
    counted = count_letters(book)
    listed=[]
    for i in counted:
        if i.isalpha():
            d={"letter": i,"num": counted[i]}
            listed.append(d)
    listed.sort(key=sort_on, reverse=True)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count(book)} words found in the document")
    for i in listed:
        name = i["letter"]
        count = i["num"]
        print(f"The '{name}' character was found {count} times")
    print("--- End report ---")
main()