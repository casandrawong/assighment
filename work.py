
# remove space and dash for calculating
def clean_num(phonenum):
    phonenum = phonenum.strip()
    phonenum = phonenum.replace(" ", "")
    phonenum = phonenum.replace("-", "")
    return phonenum
#function meet all = 10 characters, all digits, and first start with 0
def is_valid(number):
    if len(number) != 10:
        return False
    if number.isdigit() == False:
        return False
    if number[0] != "0":
        return False
    return True
# calculate sum
def digit_sum(number):
    total = 0
    for digit in number:
        total += int(digit)
    return total


ma = (input("Phone number: "))
clean_text = clean_num(ma)

# function
if is_valid(clean_text) == False:
    print("Invalid phone number")
else:
    p1 = clean_text[0:3]
    p2 = clean_text[3:6]
    p3 = clean_text[6:10]

    formatted = p1 + "-" + p2 + "-" + p3
    hidden = p1 + "-xxx-" + p3
    total = digit_sum(clean_text)
    print(f"Formatted: {formatted}\nHidden: {hidden}\n Digit sum: {total}")

