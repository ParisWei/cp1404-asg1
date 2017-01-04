import sys
import csv

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

#   pseudo code for loadBook
#	books = empty list
#	load csv file with csv reader into f_csv
#	for row in f_csv
#		add row into books

def loadBook():
	books = []
	with open('books.csv') as f:
		f_csv = csv.reader(f)
		for row in f_csv:
			books.append(row)
	print (str(len(books)) + " books load from books.csv")
	return books

def addBook():
	title = getInputString("Title:")
	author = getInputString("Author:")
	page = getInputInt("Pages:")
	print (title + " by " + author + ", (" + str(page) + " pages) added to reading list")
	return [title, author, page, "r"]



def main():
	bookList = loadBook()
	bookList.append(addBook())
	print(bookList)


	
	

if __name__ == "__main__":main()