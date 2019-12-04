#1 didn't solve yet

def format_address(address_string):
  # Declare variables

  # Separate the address string into parts

  # Traverse through the address parts
  for __:
    # Determine if the address part is the
    # house number or part of the street name

  # Does anything else need to be done 
  # before returning the result?
  
  # Return the formatted string  
  return "house number {} on street named {}".format(__)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"

#2

def highlight_word(sentence, word):
  sentence1 = sentence.replace(word, word.upper())
  return sentence1 

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))

#3

def combine_lists(list1, list2):
  # Generate a new list containing the elements of list2
  # Followed by the elements of list1 in reverse order
  list1 = reversed(list1)
  for x in list1:
    list2.append(x)
  return list2
	
Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))

#4

def squares(start, end):
	return [x**2 for x in range(start, end+1)]

print(squares(2, 3)) # Should be [4, 9]
print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#5

def car_listing(car_prices):
  result = ""
  for keys, values in car_prices.items():
    result += "{} costs {} dollars".format(keys, values)+ "\n"
  return result

print(car_listing({"Kia Soul":19000, "Mercedes Benz":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))

#6

def party_list(list1, list2):
  # Combine both dictionaries into one, with each key listed 
  # only once, and the value from list1 taking precedence
  z = list2.copy()
  z.update(list1)
    
  return z

Rorys_list = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_list = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(party_list(Rorys_list, Taylors_list))

#7

def count_letters(text):
  result = {}
  import re
  text1 = re.sub('[^A-Za-z]+','', text.lower())
  
  # Go through each letter in the text
  for letter in text1:
    # Check if the letter needs to be counted or not
    if letter in result: 
        result[letter] += 1
    else: 
        result[letter] = 1
    # Add or increment the value in the dictionary
    
  return result

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}

#8

pop, t, us

#9

["red", "white", "yellow", "blue"]

#10

['router, 'localhost', 'google']

