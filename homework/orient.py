import os
import random

from orient_data import *

os.system('cls' if os.name=='nt' else 'clear')

print("The Orient Express, 1923")
print("(c) David H. Ahl, 1986, in BASIC")
print("(c) Paul T. Pham, 2013, in Python")

# We discard the input, this is just to build suspense
raw_input('Press enter to continue.')

# The original variable names from BASIC.
# I guess I don't really need to initialize the strings.
C = ""
CN = [0]*25
CP = [0]*25
DA = [0]*25
HZ = [0]*25
LA = [0]*25
LB = [0]*25
ME = [0]*25
N = ""
TA = [0]*25
TD = [0]*25
CS = [0]*25
MB = ""
MD = [0]*26

read_journey_segments()
read_passenger_statements()
read_passenger_names()
read_menu_selections()
shuffle_integers()