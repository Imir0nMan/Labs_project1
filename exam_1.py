from source import *

#this part make the game more interesting
def intro():
	print("Hi, this is a small game (press enter)")
	a = input()
	print("You have to answer my questions and in the end i'll tell you a story around your answers (enter)")
	a = input()
	print("I know, sounds kinda boring (enter)")
	a = input()
	print("So i suggest you to answer in my questions without hesitstion, and you will get a funny story (enter)")
	a = input()


def main():
	intro()	
	n = input("Lets start, write number from 1 to 3 (choose one of 3 topics) ")
	while not checkInp(n):
		n = input("incorrect, please write one number from 1 to 3 ")
	dialog (int(n))

# Don't worry, this is a generic way to run program
if __name__ == "__main__":
	main()