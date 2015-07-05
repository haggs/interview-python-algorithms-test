#########################################################################################################
# This file contains the definition and unit test of the print_depth() function, which prints
# the depth of all dictionary keys found in a provided (potentially nested) dictionary.
#
# NOTE: The question simply asked me to print all keys and their depth, BUT the sample output
#       from the problem was formatted in a very specific way. I decided to match the sample output
#       even though it made my code more complex, because I like to give the "client" what they expect ;-)
#
# Author: Dan Haggerty
# Date:   July 5th, 2015
#########################################################################################################
def print_depth(data, depth=0):

    # Error checking
    if not isinstance(data, dict):
        print "print_depth(): Non-dictionary data type received"
        return

    elif not len(data):
        print "print_depth(): received empty dictionary"
        return

    depth += 1

    dicts_at_this_depth = []

    # I sort the keys as it was done in the sample output
    for key in sorted(data, key=data.get):
        print key, depth
        if isinstance(data[key], dict):
            dicts_at_this_depth.append(key) # Also build a list of values that are dictionaries

    # Print any values that are dictionaries last
    for key in dicts_at_this_depth:
        print_depth(data[key], depth)

# Define some test data
not_a_dictionary = 123
empty_dictionary = {}

test1 = { "key1" : 1,
          "key2" : { "key3" : 1,
                     "key4" : { "key5" : 4,
                              }
                   }
        }

test2 = { "key1" : 1,
          "key2" : 2,
          "key3" : 3,
        }

test3 = { "key1" : 1
        }

# Call our function on the test data
print "Test - Provided test data"
print_depth(test1)

print "\nTest - Passing a non-dictionary"
print_depth(not_a_dictionary)

print "\nTest - Passing an empty dictionary"
print_depth(empty_dictionary)

print "\nTest - Single level dictionary"
print_depth(test2)

print "\nTest - Single key dictionary"
print_depth(test3)