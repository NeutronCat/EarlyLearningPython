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
  
  


