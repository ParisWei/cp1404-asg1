import sys

def getInputString(question):
	result = input(question)
	while(len(result) == 0):
		print ("Input can not be blank")
		result = input(question)
	else:
		return result

def getInputInt(question):
	num = ""
	while True:
		try:
		   num = int(input(question))
		except ValueError:
		   print("Invalid input; enter a valid number")
		   continue
		else:
			if num >= 0:
				return num
			else:
				print("Number must be >= 0")
				continue


def addBook():
	title = getInputString("Title:")
	author = getInputString("Author:")
	page = getInputInt("Pages:")
	print (title + " by " + author + ", (" + str(page) + " pages) added to reading list")
	return [title, author, page, "r"]



def main():
	newBook = addBook()
	print(newBook)


	
	

if __name__ == "__main__":main()