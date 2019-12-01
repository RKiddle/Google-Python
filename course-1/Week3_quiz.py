#1

number = 1
while number <= 7:
	print(number, end=" ")
	number += 1


#2

def loop(start, stop, step):
	return_string = ""
	if step == 0:
		___
	if ___:
		step = abs(step) * -1
	else:
		step = abs(step)
	for ___:
		return_string += str(count) + " "
	return return_string.strip()

print(loop(11,2,3)) # Should be 11 8 5
print(loop(1,5,0)) # Should be 1 2 3 4
print(loop(-1,-2,0)) # Should be -1
print(loop(10,25,-2)) # Should be 10 12 14 16 18 20 22 24 
print(loop(1,1,1)) # Should be empty

#3

#4

#5

def show_letters(word):
	for i in word:
		print(i)

show_letters("Hello")

#6

#7

def decade_counter():
	while year > 50:
		year += 10
	return year

#8

for x in range(1, 10, 3):
    print(x)

#9

for x in range(10):
    for y in range(x):
        print(y)

#10

def votes(params):
	for vote in params:
	    print("Possible option:" + vote)
