'''
FILE I/O                                                 
'''


''' Opening a file [open(), function to open  and close(), func. to close the file]      There are different modes for opening a file: (by default itake read mode)
syntax -                                                                                 1) r -> open for reading
open("FILE NAME","MODE")                                                                 2) w -> open for writing    
example - open("sample.text","r")                                                        3) a -> open for appending
                                                                                         4) + -> open for updating  
'''


# # OPENING A FILE TO READ THE CONTENT OF A FILE:
file = open("sample.txt","r")
print(file.read())          
print(file.read(5))      # You can also read the first 5 charcaters of the file

file.close()



# # now another function --> readline()

file = open("sample.txt","r")

# # READS the first line
print(file.readline())          

# # READS the second line
print(file.readline())          

# # READS the third line
print(file.readline())          

# # READS the fourth line .......... and so on
print(file.readline())          


file.close()  # You should close the file at the last .



# # OPENING THE FILE TO WRITE TO THE FILE [use write() function]

file = open("another.txt","w")           
file.write("PLEASE WRITE THESE TEXT TO THE FILE")
print(file)           # these will automatically create  a file with name in  the open function which will have these text.
file.close()


# # OPENING A FILE TO APPEND TO THE FILE [open in append mode]
file = open("another.txt","a")           
file.write("I AM APPENDING.")

print(file)           # these will automatically apend at the end of the file.
file.close()


# #  OPEN AND CLOSE THE FILE BY USING THE with statement
# # with statement -> It is the best way to open and close the file automatically.

with open("another.txt","w") as file:
    print(file.write("Hi this is for checking the with statement"))


#    Method	                       Description

# 1) close()	                  Closes the file
file = open("copy.txt","r")
print(file.read())
file.close

# 2) detach()	              Returns the separated raw stream from the buffer

# 3) fileno()	             Returns a number that represents the stream, from the operating system's perspective

# 4) flush()	             Flushes the internal buffer

# 5) isatty()	             Returns whether the file stream is interactive or not

# 6) read()	                 Returns the file content

# 7) readable()	             Returns whether the file stream can be read or not

# 8) readline()	             Returns one line from the file

# 9) readlines()	         Returns a list of lines from the file

# 10) seek()	             Change the file position

# 11) seekable()	         Returns whether the file allows us to change the file position

# 12) tell()	             Returns the current file position

# 13) truncate()	         Resizes the file to a specified size

# 14) writable()	         Returns whether the file can be written to or not

# 15) write()	             Writes the specified string to the file

# 16) writelines()	         Writes a list of strings to the file