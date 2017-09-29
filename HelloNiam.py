
print(5*5*5)
#awesome
for x in range(0,3):
    print'Value of x:', x
#loop
string = 'hello'
for letter in string:
    print(letter)
#or
lister = (0, 1, 'hey')
for value in lister:
    print value
#while loop
print ("while loop")
var = 10
while(var>0):
    print(var)
    var-= 1

print("loop exited")

var = 10
while True:
    var -= 1
    print(var)
    if (var == 0):
        break
    
print("done loop")

#cool, now:
var1 = 10

while True:
    var1 -= 1
    if (var1 == 6):
       continue #no 6 when the model is running (it is skipped)
    print(var1)
    if (var1 == 0):
        break
    
print("Done loop")
    

var1 = 10

for x in range(3):
    pass #nothing happens when I run it

#inputs from USER

number = int(input("Number:"))

print"The value of my time is", number,"dollars per hour."

str.nombre = input("Name:")

print"Your name is", nombre


##FUNCTIONS

def sum_list(lister):
	sum = 0
	for x in lister:
		sum += x
	print (sum)
#define lister and you can call the function by saying sum_list(lister)
	
