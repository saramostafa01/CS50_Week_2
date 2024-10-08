# Prompt user to enter license plate
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if check_letter(s) and check_length(s) and check_numbers(s) and check_format(s) :
        return True
    else:
        return False

# Check if the license starts with two letters
def check_letter(s):
    if s[0:2].isalpha():
        return True
    else:
        return False

# Check if the license length is greater than or equal 2 but less than or equal 6
def check_length(s):
    if 2 <= len(s) <= 6:
        return True
    else:
        return False

# Check the numbers 
def check_numbers(s):
    firstnum = None
    for c in s:
        if c.isdigit():
            firstnum = c
            break
    if int(firstnum) == 0:
        return False
    index = s.index(firstnum)
    position = len(s) - index
    for c in s[-position:]:
        if not c.isdigit():
            return False
    return True

# Check is there is no punctuation included 
def check_format(s):
    for i in s:
        if  not i.isalpha() and not i.isdigit():
            return False
    return True
main()