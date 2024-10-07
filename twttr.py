text = input("input text: ")
for i in text:
    if i.lower() == "e" or i.lower() == "a" or i.lower() == "i" or i.lower() == "o" or i.lower() == "u":
        i = ""
    print(i, end = "")