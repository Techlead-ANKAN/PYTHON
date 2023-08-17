'''
STATEMENTS
'''

# A) break_statement


for i in range(0,20,1):
    print("condition is true ",i)
    if i == 15:       
        break            # this line says that u have been told to print till 20 but now i am breaking it, now u will run till 15
else:
    print("will print when the condition is exhausted ")   # in this case else line will NOT BE PRINTED as the 
                                                           # LOOP IS NOT SUCCESFULLY TERMINATED BY ITSELF IT WAS FORCED TO TERMINATE.



# B) continue_statement

for i in range(0,20,1):
    
    if i == 15:
        continue
    print("condition is true ",i)



# c) pass_statement- it is null statement in python.it instructs to do nothing
i = 5
if i<15:
    pass
print("Ankan")
