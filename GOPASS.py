import random

char1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
char2 = char1.lower()
char3 = "@!#$&*"
char4 = "123456789"

def message():
	print("Password Generator by Jeet Patel (I_am_Dope)")
	print("Your Password is:",gopass())

def gopass():
	password = ""
	for _ in range(4):
		password += random.choice(char1)

	for _ in range(4):
		password += random.choice(char2)
	
	for _ in range(3):
		password += random.choice(char3)

	for _ in range(3):
		password += random.choice(char4)

	password_final = list(password)
	shuff = random.shuffle(password_final)
	passwd = "".join(password_final)
	return passwd
	

message()
