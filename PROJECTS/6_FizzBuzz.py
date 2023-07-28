# FizzBuzz

# It is often said as the Game of Counting where the participants have to replace the multiple of three by speaking Fizz, the multiple of 5 by Buzz and the multiple of 3 and 5 both by calling out FizzBuzz. The rest of the numbers should be called as it is with no change. A number is given at the start of the play and the counting in the game must be performed till the number is encountered.


start = int(input("Enter starting point: "))
end = int(input("Enter ending point: "))

for i in range(start, end+1):
    if (i%3==0) and (i%5==0):
        print("FizzBuzz")
    elif (i%5==0):
        print("Buzz")
    elif (i%3==0):
        print("Fizz")
    else:
        print(i)
