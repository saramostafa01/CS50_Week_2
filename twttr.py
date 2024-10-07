def main():
    text = input("input text: ")
    vowels(text)

def vowels(vow):
    for i in vow:
        if i.lower() == "e" or i.lower() == "a" or i.lower() == "i" or i.lower() == "o" or i.lower() == "u":
            i = ""
        print(i, end = "")

main()
