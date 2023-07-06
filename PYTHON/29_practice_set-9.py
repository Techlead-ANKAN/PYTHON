'''
PRACTICE SET - 9
'''

# 1) Write the python code to read the text from poem.txt file and find whether it contains the word "twinkle"
# file = open("poem.txt","r")
# poems = file.read()
# print(f"The text present in the file is: {poems}")

# if "twinkle" in poems:
#     print(f"The word twinkle is present in the file ")
# else:
#     print(f"The word twinkle is not  present in the file ")
# file.close()

# 2) 
# def game():
#     return 44444

# your_score = game()
# with open("hiscore.txt",) as file:
#     hiscore = file.read()
#     hiscore = int(hiscore)

# if hiscore<your_score:
#     with open("hiscore.txt","w") as file:
#         file.write(str(your_score))
#         print(f"The new High_Score is: {file}")
# else:
#     with open("hiscore.txt","r") as file:
#         file.read(str(hiscore))
#         print(f"Still the High_score record is {file}")


# 4) 
# with open("animal","r") as file:
#      content = file.read()

# content = content.replace("donkey","######")

# with open("animal","w") as file:
#     file.write(content)


# 5) 

# words = ["donkey","cow","animal","dog"]   # thses are the list of wprds to be censored if present in the txt file


# with open("animal","r") as file:         # open the file in reda mode
#      cont = file.read()

# for word in words:                   #for each of the words present in that list

#      cont = cont.replace(word,"######")       # replacing those words in the text file        
#      with open("animal","w") as file:
#       file.write(cont)


# 6) 
# with open("log.txt","r")as file:
#      cont = file.read()
# if "python" in cont:
#      print(" The word 'pyhton' is present in the log file.")
# else:
#      print(" The word 'python' is not present in the log file")


# 7) 
# cont = True
# i = 1

# with open("log.txt","r") as file:
#       while cont:
#            cont = file.readline()
#            if 'python' in cont:
#                 print(cont)
#                 print(f"The word 'pyhton' is present in the log file in line number {i}")
#            i +=1



# # 8) 
# with open("this.txt") as file:
#      cont = file.read()

# with open("copy.txt","w") as file2:
#      print(file2.write(cont))


# 9) 
# a = "this.txt"
# b = "copy.txt"
# with open("this.txt","r") as file1:
#      cont1 = file1.read()
# with open("copy.txt","r") as file2:
#      cont2 = file2.read()

# if cont1 == cont2:
#      print(f"The files {a} and {b} are Identical ")
# else:
#      print(f"The files {a} and {b} are Not Identical")


# 10) 
# with open("text_prac.txt","w") as file:
#      wipe = file.write(" ")
#      print(wipe)


# 11) 
# import os

# old_name = "oldfile.txt"
# new_name = "newfile.txt"

# with open(old_name,"r") as file:
#      content = file.read()

# with open(new_name,"w") as file:
#      file.write(content)

# os.remove(old_name)
