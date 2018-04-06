# ask user name
name = input("What is your name?: ")

# ask user age
age = input("How old are you?: ")

# ask user location and store a variable called "city"
city = input("What city do you live in?: ")

# ask user about the thing he likes to do the most and save it as a variable called "love"
love = input("What is that one thing you love doing the most?: ")

# create output text
string = "Your name is {} and you are {} years old. You live in {} and you love {}"
output = string.format(name, age, city, love)

# print the output to the screen
print(output)


