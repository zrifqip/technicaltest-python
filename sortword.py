
        
def main():
    file = open("teks.txt", "r")
    text = file.read()
    x = text.replace("\n", " ")
    words = x.split(" ")
    words.sort()
    newText = " ".join(words)
    print(newText)
    file.close()


if __name__ == "__main__":
    main()
