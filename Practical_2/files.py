out_file = open("capitalist_conrad.py", "w")
price = input("Enter your price: ")
print("${:}".format(price), file=out_file)
out_file.close()

in_file = open("name.txt", "r")
name = in_file.read().strip()
print("Your name is ", name)
in_file.close()