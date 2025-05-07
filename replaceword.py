def main():
    file = open("teks.txt", "r")
    text = file.read()
    x = text.replace("\n", " ")
    x = x.replace("adalah", "ialah")
    print(x)
    file.close()
if __name__ == "__main__":
    main()
    