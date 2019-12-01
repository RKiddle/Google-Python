#1 OK

number = 1
while number <= 7:
	print(number, end=" ")
	number += 1


#2 OK

def loop(start, stop, step):
	return_string = ""
	if step == 0:
		step=-1
	if start>stop:
		step = abs(step) * -1
	else:
		step = abs(step)
	for count in list(range(start, stop, step)):
		return_string += str(count) + " "
	return return_string.strip()


print(loop(11,2,3)) # Should be 11 8 5
print(loop(1,5,0)) # Should be 1 2 3 4
print(loop(-1,-2,0)) # Should be -1
print(loop(10,25,-2)) # Should be 10 12 14 16 18 20 22 24 
print(loop(1,1,1)) # Should be empty

#3 Something wrong with this exercise

def timer(start, stop):
	x = start
	if start>stop:
		return_string = "Counting down: "
		while x >= stop:
			return_string += str(x)
			if x > stop:
				return_string += ","
			x=-1
	else:
		return_string = "Counting up: "
		while x <= stop:
			return_string += str(x)
			if x < stop:
				return_string += ","
				x=+1
	return return_string

print(timer(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(timer(2, 1)) # Should be "Counting down: 2,1"
print(timer(5, 5)) # Should be "Counting up: 5"

#4 wrong Not quite, digits(9999) returned 5, should be 4.
def digits(n):
	count = 0
	if n == 0:
	  return 1
	while count<n:
		count += 1
		n=n/count
	return count-2
#4 alternative

def digits(n):
    n = abs(n)
    count = 1
    while (int(n/10)) > 0:
        count += 1
        n=int(n/10)
    return count

#5 OK

def show_letters(word):
	for i in word:
		print(i)

show_letters("Hello")

#6 OK
def multiplication_table(start, stop):
	for x in list(range(start, stop+1)):
		for y in list(range(start, stop+1)):
			print(str(x*y), end=" ")
		print()

multiplication_table(1, 3)

#7 not initializing variables

def decade_counter():
	while year > 50:
		year += 10
	return year

#8 7

for x in range(1, 10, 3):
    print(x)

#9 8

for x in range(10):
    for y in range(x):
        print(y)

#10 have issue with this q-always wrong, correct is votes['yes', 'no', 'maybe']

def votes(params):
	for vote in params:
	    print("Possible option:" + vote)
