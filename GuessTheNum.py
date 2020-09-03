import random

print("				   GUESS THE NUMBER					")
print(''' 
		Enter a digit between the selected range
		You will be told if the number is greater or less than the number you've entered
		If you guess the number in the given number of tries remaining, You win!!
		''')
level = int(input('''
        #####   Choose a difficulty level(Enter just the number) #####
                LEVEL 1 --> range is (1,3) && Number of tries - 2
                LEVEL 2 --> range is (1,15) && Number of tries - 4
                LEVEL 3 --> range is (1,127) && Number of tries - 7
                LEVEL 4 --> range is (1,2097151) && Number of tries - 21
        #############################################################
'''))
ranges = [3, 15, 127, 2097151]
my_dict = {1:2, 2:4, 3:7, 4:21}
n = 0
x = 0

for i in my_dict:
    if i==level:
        n = my_dict[level]
        x = i

range_limit = ranges[x-1]

num = random.randrange(1,range_limit)
print("The number is in the range: (1,{})\n".format(ranges[x-1]))
for i in range(n):
	x = int(input("Guess a number "))
	if x > num:
		print("X is less than ",x)
		print("Number of tries remaining: ",n-i-1,"\n")
	elif x < num:
		print("X is greater than, ",x)
		print("Number of tries remaining: ",n-i-1,"\n")
	elif x == num:
		print("YOU WIN!!! X is-->", x)
		break
	if i == n-1 and x!=num:
		print("YOU LOSE")
