# The program checks whether a number is an Armstrong number or not
# eg: if 407 = 4^3 + 0^3 + 7^3 then the number is an armstrong number.

#take user input
number = int(input("Enter the number you want to check for armstrong number: "))

# find the order of the input number 
numOfDigits = len(str(number))

sum = 0
copy = number

while copy > 0:
    temp = copy % 10
    sum += temp ** numOfDigits
    copy //= 10

if sum == number:
    print(True)
else:
    print(False)