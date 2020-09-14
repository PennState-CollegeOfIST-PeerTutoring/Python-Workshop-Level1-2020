# -------- Variables --------

# String
sentence = "This is a sentence"

# Double/Number
temp = 60
temp2 = 70.2

# Boolean
is_raining = True
is_snowing = False

# -------- Print --------

print(sentence)
print(temp)
print(is_raining)

# -------- Reference Multiple Variables --------

val1 =111
val2 = 222
val1,val2 = val2,val1 #(Swaps values in variables)
print(val1)
print(val2)

# -------- Math Operators --------

val3 = val1 + val2
val3 = val1 -val2
val3 = val1 * val2
val3 = val1 / val2

product = 2 ** 4

sum = 1
sum +=3
sum -=1
sum *= 5
sum /= 2

# -------- User Input --------

new = input("Please Input a ____")
print(new)

# -------- Conditions --------
# Indentation is important!!  Shows what is with what

temp = input("What is the temperature outside?")
if temp < 50:
	print("It’s a bit chilly outside, grab a jacket")
elif temp > 88:
	print("It’s HOT outside, string down a layer")
else:
	print("It’s just right outside")
	
if is_raining:
	print("Grab an umbrella")

# -------- Loops --------

is_done = True
while is_done:
	user = input("is it done yet?")
	if user == "yes":
		print("It’s STILL going on?!!")
	else:
		is_done = False
		print("Thank goodness it’s done!")
		
for i in range(10):
	print(i)

for _ in range(10):
	print("Hi")

# -------- Formatting Strings -------- 

cost = 3.89999999
print("Cost: ${}".format(cost)) # {} placeholder for a variable
print("Cost: ${:.2f}".format(cost)) #Rounding until 2 places
print("Cost \n High")
print(f"Cost: ${cost})
print(f"Cost: ${cost:.2f})

# -------- Lists --------

cars = ["Honda", "Toyota", "Mazda", "Subaru"]
print(cars)
stuff = ["This is a string", 500.599123, True]
print(stuff)
for c in cars:
	print("I like " + c)
print("Subaru" in cars) # Searches list to see if Subaru is in the cars list, returns True/False
nums = list(range(10)) # creates a list with numbers 0 through 9
print(nums)
print ("The number is: {:.2f}".format(stuff[1]))print(cars[1:]) # Take the list cars and start at element 1 and go to the end of the list
print(cars[1:-1}) # Take the list cars and start at element 1 and go until the second to last
cars.append("Chevy")
print(cars)
results = []
for i in range(15):
	results.append(i ** 3)
print(results)
other_results = [i ** 3 for I in range(15)] # Generator
print(other_results)

# -------- Functions --------

food = ['Apple', 'Banana', 'Apricot', 'Avacado']
def my_filter(some_list, character):
	results = []
	for item in some_list:
		if item[0] == character:
			results.append(item)
	return results

def lowercase(some_list, character):
	results = []
	for item in some_list:
		if item[0].lower() == character.lower():
			results.append(item)
	return results
print(my_filter(food, 'A'))print(my_filter(food, 'B'))
