def intro():
	print ("Hi there!My name is Cathy.")
	print(" ")
	answer=input("Greetings!")
	if answer == "hi":
		icecream()
		sport()
		music()
		phone()

	elif answer == "bye":
		print(" ")
		print("Umm bye?")
		print(" ")
	else:
		print("Excuse me?!")
		print(" ")

def icecream():
	answer = input("What is your favorite ice cream flavor?")
	print(" ")
	print ("That's cool!Mine is rainbow sherbet from baskin robins")
	print(" ")

def sport():
	answer = input("What about your favorite sport? (If you don't have one say no)")
	print(" ")
	print ("Cool, mine is softball/baseball.")
	print(" ")
	if answer == ("no"):
		print("Alright no problem, next question:")
		print(" ")




def music():
	answer = input("Spotify or Apple Music?")
	print(" ")
	if answer == ("spotify"):
		print ("Me too!")
		print(" ")
			#phone()
			#music=False
	else:
		print("Okay, you do you girl.")

			#phone()
			#music=False

def phone():
	answer = input("Apple or Samsung?")
	if answer == ("apple"):
		print(" ")
		print ("Me too!")

	else:
		print("Alright.")
		print(" ")



def main():
	intro()

if __name__ == "__main__":
	main()
