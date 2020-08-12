# just a .py file with fun math functions
# i didn't end up coming up with something good on my own, but 
# the link below has some nice versions of a solution
# https://discuss.codecademy.com/t/help-with-personal-python-project-converting-base-10-to-other-bases/39218/2

def decimal_to(decimal_num, new_base):
    '''
    A function that will convert any base 10 number to a new base

    :param decimal_num: the original base ten number
    :type: float64
    :param new_base: the new base to conver decimal_num to
    :type: int

    :returns: the base ten decimal_num in base new_base
    '''
    
    x = 0
    max_base = 0
    while max_base < decimal_num:
        x += 1
        max_base = new_base ** x

    dec_rem = decimal_num - (new_base ** x)
    dig1 = str(1)

    if dec_rem > 0:
        new_base ** (x-1)

# from the above website, the most basic version

def convert_base(number, base):
    if base < 2:
        return False
    remainders = []
    while number > 0:
        remainders.append(str(number % base))
        number //= base
    remainders.reverse()
    return ''.join(remainders)
