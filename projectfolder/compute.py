#####################
# Yousef Mohamed
# First Interview Step Challenge
# Junior Software Developer - Analyze Re
#####################

import sys
# Implementing an exception handeling block that prints an error and quits the program if the number of
# arguments passed to the script are invalid.
# Note: Intentionally did not stop program if more than 2 arguments are passed for future expansion possibilities.
try :
    Threshold = float(sys.argv[1]) # Creating a variable to store the threshold argument as a float type
    Limit = float(sys.argv[2])     # Creating a variable to store the limit argument as a float type
except IndexError:
    print("Error: Too few arguments passed to script. Please enter 2 arguments (Threshold,Limit)")
    quit()

# Checking if input file is passed to the input stream of the script
# The isatty() method returns True if the file stream is interactive
# If input file is not provided print error and exi
if not sys.stdin.isatty():
    print("Error: Script initialization missing input file!")
    quit()

# Creating a list to hold the input line values
input = []

# iterating over each line in the input file
for line in sys.stdin:
    # Stripping the new line character from the end of each input line
    line = line.strip('\n')
    # Casting the type of each input line from string to float type
    line = float(line)
    # Appending the new float value to the end of the input list
    input.append(line)

# By now we have a list of all the N inputs in float type stored in the input list
print(input)

# Creating a sum variable that will hold the total sum of the output lines (sum should be <= limit)
sum = 0

# iterating over each input value
for value in input:
    if value > Threshold:
        # if value is greater than the threshold then the output value will be equal to input value - threshold
        value -= Threshold
        # checking if the total sum will exceed limit if the current output value is added to the sum
        if sum + value > Limit:
            # if it will exceed the limit then the new value will be qual to limit - sum so that when
            # new value is added to total sum in the next step the total sum will exactly be equal to limit
            value = Limit - sum
        sum += value
        print(value)
    # if the value is not greater than the threshold then the output corresponding to this input value
    # will always be 0
    else:
        print(0.0)

# Printing the total sum of N outputs at the end of the output(at N+1 line)
print(sum)