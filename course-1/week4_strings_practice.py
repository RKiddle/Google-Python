#1

def is_palindrome(input_string):

# make it suitable for caseless comparison

#remove whitespaces
  input_string.replace(" ", "")

  input_string.lower().strip()
  input_string = list(input_string)
# reverse the string
  rev_str = input_string[::-1]
# check if the string is equal to its reverse
  if input_string == rev_str:
   return True
  else:
   return False
  	

print(is_palindrome("Never Odd or Even")) # Should be True #my program says false
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True


#2

def convert_distance(miles):
	km = miles * 1.6 
	result = "{0} miles equals {1:.1f} km".format(miles, km)
	return result

print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km
