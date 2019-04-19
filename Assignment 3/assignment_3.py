import math


def shiftbits(number):
    log10 = math.log(number+1)
    log2 = log10 / math.log(2)
    shifts = math.ceil(log2)
    return shifts


while True:
    try:
        number = int(input("What number do you want to do a bitwise calculation on?"))
    except ValueError:
        print("Please input an integer (whole number) only.")
    else:
        break


shift = shiftbits(number)

print("Using for")
x = 0
for i in range(-1, shift):
    if number & (1 << x) > 0:
        print(1)
    else:
        print(0)
    x = x + 1

print("Using while")
while shift >= 0:
    if number & (1 << shift) > 0:
        print(1)
    else:
        print(0)
    shift = shift-1
