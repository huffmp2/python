books = ['fiction', 'sci-fi', 'history', 'poetry', 'romance']
for book in books:
    print ("I like reading " + book + " books!")
message = input ("What kind of books do you like to read? ")
books.append(message)
print (books)
