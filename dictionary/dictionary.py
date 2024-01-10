books = {
    'Como hacer amigos e influir sobre las personas':{
        'author':'Dale Carnegie',
        'publication_year': 1936
    },
    'The every day Hero':{
        'author':'Robin Sharma',
        'publication_year': 2021
    },
    'Atomic Habits':{
        'author':'James Clear',
        'publication_year': 2018
    }
}

book_title = 'Como hacer amigos e influir sobre las personas'
if book_title in books:
    book = books[book_title]
    print(f 'title:{book_title}')
    print(f 'author:{books['author']}')
    print(f 'pubiclation_year:{books['publication_year']}')

else:
    print('Book title not found in the dictionary')