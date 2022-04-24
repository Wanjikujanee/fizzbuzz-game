#1. If the input is divisible by 3,the function will return a string "fizz"
#2. If the input is divisible by 5,it will return "buzz"
#3. If the input is divisible by both 3 and 5 it will return "FizzBuzz"
#4. prints number 1 - 100
#5. For any other number it will return the same input
def fizz_Buzz(input):
   
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    if input % 3 and input % 5 == 0:
        return "FizzBuzz"
    
    return input
print(fizz_Buzz(5))
   