# prompt user to enter variable in camel case 
def main():
    variable = input("camelCase: ")
    isCap(variable)

def isCap(x):
    print("snake_case: ", end = "")
    for letter in x :
        if letter.isupper() == True:
            print("_" + letter.lower(), end = "")
        else :
            print(letter, end = "")

main()