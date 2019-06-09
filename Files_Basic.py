# Computers use file systems to store and retrieve data. Each file is an individual container of related information. If you’ve ever saved a document, downloaded a song, or even sent an email you’ve created a file on some computer somewhere. Even script.py, the Python program you’re editing in the learning environment, is a file.

with open("welcome.txt") as text_file:
  text_data = text_file.read()
print(text_data)

#iterating
# When we read a file, we might want to grab the whole document in a single string, like .read() would return. But what if we wanted to store each line in a variable? We can use the .readlines() function to read a text file line by line instead of having the whole thing
with open("how_many_lines.txt") as lines_doc:
  for line in lines_doc.readlines():
    print(line)
	
# readline() will only read a single line at a time. If the entire document is read line by line in this way subsequent calls to .readline() will not throw an error but will start returning an empty string ("")
with open("just_the_first.txt") as first_line_doc:
  first_line = first_line_doc.readline()
print(first_line)

#Writing a File
# here we pass the argument 'w' to open() in order to indicate to open the file in write-mode. The default argument is 'r' and passing 'r' to open() opens the file in read-mode as we’ve been doing.
# This code creates a new file in the same folder as script.py and gives it the text What an incredible file!. It’s important to note that if there is already a file called generated_file.txt it will completely overwrite that file, erasing whatever its contents were before.
with open("bad_bands.txt", "w") as bad_bands_doc:
  bad_bands_doc.write("Maroon 5, they suck")
  
#Appending to a File
# Instead of opening the file using the argument 'w' for write-mode, we open it with 'a' for append-mode. 
with open("cool_dogs.txt", "a") as cool_dogs_file: 
  cool_dogs_file.write("Air Buddy")
  
# The with keyword invokes something called a context manager for the file that we’re calling open() on. This context manager takes care of opening the file when we call open() and then closing the file after we leave the indented block
# The with syntax replaces older ways to access files where you need to call .close() on the file object manually. We can still open up a file and append to it with the old syntax, as long as we remember to close the file connection afterwards.

#CSV Files!!!
with open("logger.csv") as log_csv_file:
  print(log_csv_file.read())
  
# Even though we can read these lines as text without a problem, there are ways to access the data in a format better suited for programming purposes. In Python we can convert that data into a dictionary using the csv library’s DictReader object. 
# pass the additional keyword argument newline='' to the file opening open() function so that we don’t accidentally mistake a line break in one of our data fields as a new row in our CSV 
# don't forget the CSV module!
import csv
with open('cool_csv.csv') as cool_csv_file:
  cool_csv_dict = csv.DictReader(cool_csv_file)
  for row in cool_csv_dict:
    print(row['Cool Fact'])

#with @ delimiter 
import csv
with open('books.csv') as books_csv:
  books_reader = csv.DictReader(books_csv, delimiter='@')
  isbn_list = [book['ISBN'] for book in books_reader]

#Writing a CSV File
# In our code above we had a set of dictionaries with the same keys for each, a prime candidate for a CSV. We import the csv library, and then open a new CSV file in write-mode by passing the 'w' argument to the open() function.
# We then define the fields we’re going to be using into a variable called fields. We then instantiate our CSV writer object and pass two arguments. The first is output_csv, the file handler object. The second is our list of fields fields which we pass to the keyword parameter fieldnames.
# Now that we’ve instantiated our CSV file writer, we can start adding lines to the file itself! First we want the headers, so we call .writeheader() on the writer object. This writes all the fields passed to fieldnames as the first row in our file. Then we iterate through our big_list of data. Each item in big_list is a dictionary with each field in fields as the keys. We call output_writer.writerow() with the item dictionaries which writes each line to the CSV file.
import csv
access_log = [{'time': '08:39:37', 'limit': 844404, 'address': '1.227.124.181'}, {'time': '13:13:35', 'limit': 543871, 'address': '198.51.139.193'}, {'time': '19:40:45', 'limit': 3021, 'address': '172.1.254.208'}, {'time': '18:57:16', 'limit': 67031769, 'address': '172.58.247.219'}, {'time': '21:17:13', 'limit': 9083, 'address': '124.144.20.113'}, {'time': '23:34:17', 'limit': 65913, 'address': '203.236.149.220'}, {'time': '13:58:05', 'limit': 1541474, 'address': '192.52.206.76'}, {'time': '10:52:00', 'limit': 11465607, 'address': '104.47.149.93'}, {'time': '14:56:12', 'limit': 109, 'address': '192.31.185.7'}, {'time': '18:56:35', 'limit': 6207, 'address': '2.228.164.197'}]
fields = ['time', 'address', 'limit']
with open("logger.csv", "w") as logger_csv:
  log_writer = csv.DictWriter(logger_csv, fieldnames=fields)
  log_writer.writeheader()
  for item in access_log:
    log_writer.writerow(item)

#JSON Files
# has its own module, use .load to read
import json
with open('message.json') as message_json:
  message = json.load(message_json)
  print(message['text'])

#use json .dump to write payload to json
import json
data_payload = [
  {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   'follow up': 'But enough talk!'}
]
with open("data.json", "w") as data_json:
  json.dump(data_payload, data_json)

#    Open up file objects using open() and with.
#    Read a file’s full contents using Python’s .read() method.
#    Read a file line-by-line using .readline() and .readlines()
#    Create new files by opening them in write-mode.
#    Append to a file non-destructively by opening a file in append-mode.
#    Apply all of the above to different types of data-carrying files including CSV and JSON!
