from source import *

def checkInp(x):
	try:
		x = int(x)
		if 0 < x < 4:
			return True
		else:
			return False
	except:
		return False

def main_dialog():
	print("Hi, this is a small game (press enter)")
	a = input()
	print("You have to answer my questions and in the end i'll tell you a story araund your answers (enter)")
	a = input()
	print("I know, sounds kinda boring (enter)")
	a = input()
	print("So i suggest you to answer in my questions without hesitstion, and you will get a funny story (enter)")
	a = input()
	n = input("Lets start, write number from 1 to 3 (choose one of 3 topics) ")
	while not checkInp(n):
		n = input("incorrect, please write one number from 1 to 3 ")
	topic = dialog(n)
	print(topic)


def main():
	main_dialog()

if __name__ == "__main__":
	main()