def fizz_buzz(num):
    """
    This will be fizz Buzz. 
    If number is divisible by 3 return fizz
    if number is divisible by 5 return buzz
    if number is divisible by 3 and 5 return fizzbuzz
    if number is not divisibly by any, return the number
    3 - > Fizz
    10 - > Buzz
    15 - > FizzBuzz
    2 - > 2
    """
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    if num % 3 == 0:
        return 'Fizz'
    if num % 5 == 0:
        return "Buzz"

    return num

def fizz_buzz_alternate(num):
    word = ''
    if num % 3 == 0:
        word = 'Fizz'
    if num % 5 == 0:
        word += "Buzz"
    return word or num
