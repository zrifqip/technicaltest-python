
def main():
    search_word = input("Input Kata: ")
    file = open("teks.txt", "r")
    text = file.read()
    x = text.replace("\n", " ")
    words = x.split(" ")
    cleaned_words = [
    ''.join(ch for ch in word if ch.isalnum()) 
    for word in words
    ]
    count = 0
    for word in cleaned_words:
        if word.lower() == search_word.lower():
            count += 1
    print(f"Kata '{search_word}' : {count}")
    file.close()
if(__name__ == "__main__"):
    main()