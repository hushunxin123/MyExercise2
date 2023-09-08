import sqlite3

# Read the file and copy all the content to a list
with open('stephen_king_adaptations.txt', 'r') as file:
    stephen_king_adaptations_list = [line.strip().split(',') for line in file]

# Establish a connection with a  SQLite database
con = sqlite3.connect('stephen_king_adaptations.db')
cursor = con.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS stephen_king_adaptations_table 
                  (movieID TEXT, movieName TEXT, movieYear INTEGER, imdbRating REAL)''')

# Insert data into the table
cursor.executemany('INSERT INTO stephen_king_adaptations_table VALUES (?, ?, ?, ?)', stephen_king_adaptations_list)

while True:
    print('Options:')
    print('1. Search by Movie name')
    print('2. Search by Movie year')
    print('3. Search by Movie rating')
    print('4. STOP')
    option = input('Enter your choice: ')

    if option == '1':
        movie_name = input('Enter the movie name: ')
        cursor.execute('SELECT * FROM stephen_king_adaptations_table WHERE movieName = ?', (movie_name,))
        result = cursor.fetchone()

        if result:
            print('Search results:')
            print('Movie ID:', result[0])
            print('Name:', result[1])
            print('Year:', result[2])
            print('IMDB Rating:', result[3])
        else:
            print('No such movie exists in our database')

    elif option == '2':
        movie_year = input('Enter the year: ')
        cursor.execute('SELECT * FROM stephen_king_adaptations_table WHERE movieYear = ?', (movie_year,))
        result = cursor.fetchall()

        if result:
            print('Search results:')
            for row in result:
                print('Movie ID:', row[0])
                print('Name:', row[1])
                print('Year:', row[2])
                print('IMDB Rating:', row[3])
        else:
            print('No movies were found for that year in our database.')

    elif option == '3':
        rating = float(input('Enter the rating: '))
        cursor.execute('SELECT * FROM stephen_king_adaptations_table WHERE imdbRating >= ?', (rating,))
        result = cursor.fetchall()

        if result:
            print('Search results:')
            for row in result:
                print('Movie ID:', row[0])
                print('Name:', row[1])
                print('Year:', row[2])
                print('IMDB Rating:', row[3])
        else:
            print('No movies at or above that rating were found in the database.')

    elif option == '4':
        break
    print()

# Close connection
con.close()