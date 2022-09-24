from hh_parsing import *
from multiply_binary import *
from arabic_to_roman import *
from bracket_validation import *
from palindrome import *


print('1111 x 101 = ', multiply_binary('1111', '101'))
print('1954 in roman is:', arabic_to_roman(1954))

print('taco cat:', is_palindrome('taco cat'))
print('black cat:', is_palindrome('black cat'))

print('[{}{}([])]:', valid_brackets('[{}{}([])]'))
print('[{():', valid_brackets('[{()'))
input('CHECK')

parse_hh()
