numbers = [3, 1, 4, 1, 5, 9, 2]

print (numbers[0])
print (numbers[-1])
print (numbers[3])
print (numbers[:-1])
print (numbers[3:4])

if 5 in numbers:
    print ("True")
else:
    print ("False")

if 7 in numbers:
    print ("True")
else:
    print ("False")

if "3" in numbers:
    print ("True")
else:
    print ("False")

print (numbers + [6, 5, 3])


print("\n\n")

numbers[0] = "ten"
numbers[-1] = 1
print(numbers)
print (numbers[2:])

if 9 in numbers:
    print ("True")
else:
    print ("False")