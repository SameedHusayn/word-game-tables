import time #time.sleep to add a delay in program to give it a realistic look
                    #creating a list containg all elements of the table
list1 = ["col-1", "col-2", "col-3", "col-4", "col-5", "col-6", "col-7", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
         "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
#a function to print rows from list1
def print_col(a,b):
    for i in range(a, b):
        if i <= b-2: #before last element of row, it will end with indent
            print(list1[i], end="\t ")
        else: #last element prints directly
            print(list1[i])

print("Think of any word in your mind, and I will guess that word") #asking user to think of a word
time.sleep(0.5)

ltr_count = int(input("How many letters does your word has? for eg cat has 3 letters : "))  #takes input about the letter count
time.sleep(0.25)

print("Look at the table below: ")
print("="*100)  #adds design
print_col(0, 4) #prints the first four elements of list1 i.e: col1, col2, col3 and col4
time.sleep(0.15)

for i in range(7, 28, 4): #similarly prints the rest of the elements of list1 from A to X
    time.sleep(0.05)
    print_col(i, i+4)

time.sleep(0.05)
print_col(31, 33) #prints the letter Y and Z
print("="*100)  # adds design
column = [] #empty list to append inputs from the user
i = 1
while i <= ltr_count:
    time.sleep(0.15)
    col_num = input("Enter column number of letter {}: ".format(i)) #asks the user about the location of letters
    i +=1
    column.append(int(col_num))
print("="*100)  # adds design
time.sleep(0.2)

print_col(0, 7) #after input, prints first 7 elements of list1 from col1 to col7 so transpose can be printed
p = False
q = False       # p q r s boolean operators are added so in case the user thinks
r = False       # of a word with repetitive letters, the transpose of those columns
s =  False      # isn't printed multiple times like for word "SEED" tra1 isn't printed twice
for a in column:
    if a == 1 and not p:
        time.sleep(0.05)
        tra1 = ["A", "E", "I", "M", "Q", "U", "Y"]  #transpose of col1
        for a in tra1:
            print(a, end="\t  ")
        print(" ")
        p = True    # once p is True, tra1 will not be printed again hence making the transpose table look less cluttery
    elif a == 2 and not q:
        time.sleep(0.05)
        tra2 = ["B", "F", "J", "N", "R", "V", "Z"]  # transpose of col2
        for a in tra2:
            print(a, end="\t  ")
        print(" ")
        q = True    # to make sure tra2 is not printed again in case of repetitive letters
    elif a == 3 and not r:
        time.sleep(0.05)
        tra3 = ["C", "G", "K", "O", "S", "W"]  # transpose of col3
        for a in tra3:
            print(a, end="\t  ")
        print(" ")
        r = True    # to make sure tra3 is not printed again
    elif a == 4 and not s:  # a only goes till 4 because in the first table there are only 4 columns hence only 4 possibilities
        time.sleep(0.05)
        tra4 = ["D", "H", "L", "P", "T", "X"]  # transpose of col4
        for a in tra4:
            print(a, end="\t  ")
        print(" ")
        s = True # to make sure tra4 is not printed again

column_transp = [] #empty list to append inputs about the transposed table from user
j = 1
print("="*100)  # adds design
while j <= ltr_count:
    time.sleep(0.15)
    col_num = input("Enter column number of letter {}: ".format(j)) #asks the user about location of letters
    j += 1
    column_transp.append(int(col_num))

time.sleep(0.5)
print("="*100)  # adds design
print("The word you were thinking of is : ", end="")

b = 0
while b < ltr_count:
    for a in column:
        if a == 1:
            print(tra1[column_transp[b]-1],end="")   # b-1 calls input from column_transp
        elif a == 2:                                                     # which is the list containing user input about transpose
            print(tra2[column_transp[b]-1], end="")  # and directly places it in tra1 to call that letter
        elif a == 3:
            print(tra3[column_transp[b]-1],end="")
        elif a == 4:                #a only goes till 4 because in the first table there are only 4 colums hence only 4 possibilities
            print(tra4[column_transp[b]-1],end="")
        b += 1
