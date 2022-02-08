# Question 1 
print( " Question 1 \n")
string1  = input ( )
string = string1.lower()                             # converting the string to lower case as pyton is case sensitive 
if " " not in string : 
    astring = list(string)                           # splitting in list 
    adict = dict ( )                                
    for chara in astring :                           # iterating characters 
        if chara not in adict :  
            adict[chara] = 1                         # counting characters 
        else: 
            adict [chara]= adict[chara ] + 1 
    print ("the solution is " , adict )              # printing the characters 
else : 
    bstring = string.split( )                        #creating a list of words 
    bdict= dict ()
    for word in bstring :                            # itrating words 
        if word not in bdict :
            bdict[word] = 1                          # counting the words 
        else : 
            bdict[word] =bdict[word] +  1 
    print ("the solution is ", bdict)                # printing the words 
#--------------------------------------------------------------------------------------------------------------------------------------

# taking input for dates and montth and year 
#question 2 
print( " Question 2 \n")
day = int(input("enter day :"))
month = int(input("enter month "))
year = int(input("enter year (use full year ) "))
print( 'date enterd by you  is %d/%d/%d' %(day , month , year ))
if year in range(1800, 2026):                                   #eliminating cases having date greater than or less than mentioned ones 
    if year % 4 != 0 or year % 400 != 0:                        #non leap year condition 
        # applying different cinditins in cse of non leap year 
        if day in range(1, 30) and month % 2 == 0 and month != 2:
            day = day + 1
        elif day==30 and month%2 ==0 and month!=2:
            day = 1
            month =month + 1 
        elif day in range(1, 31) and month % 2 != 0 and month != 2:
            day = day + 1
        elif day==31 and month %2 !=0 and month !=2:
            day = 1
            month = month + 1 
        elif day == 31 and month % 2 != 0 and month != 2:
            day = 1
            month = month + 1
        elif day in range(1, 28) and month == 2:
            day = day + 1
        elif day == 28 and month == 2:
            day = 1
            month = 3
        elif day == 31 and month == 12:
            day = 1
            month = 1 
            year = year + 1 
        else:
            print('not a valid date ')
        print("The next date is  %d/%d/%d" % (day, month, year))
    else:     # leap year 
        # applying different conditions of a leap year 
        if day in range(1, 30) and month % 2 == 0 and month != 2:
            day = day + 1
        elif day==30 and month%2 ==0 and month!=2:
            day = 1
            month =month + 1
        elif day in range(1, 31) and month % 2 != 0 and month != 2:
            day = day + 1
        elif day == 31 and month % 2 != 0 and month != 2:
            day = 1
            month = month + 1
        elif day==31 and month %2 !=0 and month !=2:
            day = 1
            month = month + 1 
        elif day in range(1, 28) and month == 2:
            day += 1
        elif day == 28 and month == 2:
            day = 1
            month = 3
        elif day == 31 and month == 12:
            day = 1
            month = 1
            year = year + 1
        else:
            print('error not a valid date ')
        print(' The next date is  %d/%d/%d ' % (day, month, year)) # printing the correct date 
else:
    print("error , enter date as mentioned in assignment ")     # in case of year not mentioned

#----------------------------------------------------------------------------------------------------------------------------------------

#Question 3 
print("Queston 3\n")
list1 = list()  #takin the list of numbers whose tuple wehavve to make
n = int ( input (  'the no of elements in list ' ))
i = 1 # count of no of elements 
while ( i<=n):
    element = int ( input ("enter no of list "))
    list1.append(element)
    i+=1
print(" the list1 is " , list1)
final_list = list()
for i in list1:  #   iterating a vaaraiable
    tuple1 = (i, i * i)
    final_list.append(tuple1)  #entering the values to list
print("the final list is " , final_list)  # printing  the answer


#---------------------------------------------------------------------------------------------------------------------------------------

# queston 4 
print( " Question 4\n")
# taking the input of grade pointss converted to integer so we dont need to chk condition fpr floating points also 
grade_input = int(input(' enter your grade points '))
if grade_input in range (4,10 ) or grade_input == 10 :
    # applying differnt grade conditions 
    if grade_input == 10:
        letter_grade = 'A+'
        performance = " Outstanding "
    elif grade_input == 9:
        letter_grade = "A"
        performance = "EXCELLENT"
    elif grade_input == 8:
        letter_grade = "B+"
        performance = "VERY GOOD"
    elif grade_input == 7:
        letter_grade = "B"
        performance = "GOOD"
    elif grade_input == 6:
        letter_grade = "C+"
        performance = "AVERAGE"
    elif grade_input == 5:
        letter_grade = "C"
        performance = "BELOW AVERAGE"
    elif grade_input == 4:
        letter_grade = "D"
        performance = "POOR"
    else:
        print(' enter correct grade valur bro')      # error caseencountaered if any possible  
    print ( "Your Grade is %s and %s Performance." %(letter_grade , performance  )) # printing the grade result 
else:
    print("type correct grade points ") # in csase of incorrecat grade points 
 
#---------------------------------------------------------------------------------------------------------------------------------------

 #Question 5
print("Question 5\n")
n = 6  # defining no of rows
for row in range(0, 6):  # for rows
    char = ord("A")  # defining charactera as integr
    print(" " * row, end="")  # printing spaces
    for coloumn in range(0, 2 * (n - row) - 1):  # for printing alphabets
        print(chr(char), end="")
        char = char + 1
    print("")

#------------------------------------------------------------------------------------------------------------------------------------------
#Question 6
print("Queston 6\n")
dic = dict()  # craing a dict for storing values
keyvalue = 0  #initial keyvalue
pair = 0  # pair value
ask = input(' do you want to give input(Disclaimer ENTER Y OR N ONLY ) ')
while ask == 'Y':  # after use inputted yes
    keyvalue = int(input('enter your sid '))  # taking key value and pair value
    pair = input('enter youtr name ')
    dic[keyvalue] = pair  #keeping values in dicctionary
    ask = input('do you want to give input ')  # asking for another input
while ask == "N":
    print("you cant enter more values ")
    break
# part a
print("the dictionary formed is ", dic)  # printing the dictionary
#part b
# as final dictionary formed is dic
for i in sorted(dic.values()):
    for key, values in dic.items():
        z=i
        if z == values:
            print(i, key)
# part c
for key in sorted(dic):  #   printing studets details after
    print('result after sorting is ', key,
          dic[key])  # sorting according to key values
#part d                                         # searching studets name using sid
search = int(input('enter the sid for search  '))
print("the name of the student is ", dic[search])

#------------------------------------------------------------------------------------------------------------------------------------------

#Question 7 
print ( "Question 7\n")
# taking input upto which series should print
n = int(input('no upto which sequence is to be printed : '))
start1 = 0                     #entering start numbeer
start2 = 1                     #taking inpur of second number
terms = 1                      # for taking no of terms 
average = list()               # makin a list of nos to later find average
if n == 1:                     # code for print ing the sequence  if only one number
    print(start1)
    average.append(start1)
elif n == 2:                   # code for only two number s
    print(start1)
    print(start2)
    average.append(start1)
    average.append(start2)
elif ( n == 0 or n<0):
    print ( " error" )
else:                          #general purpose code
    while (i <= n):
        print(start1)
        average.append(start1)
        start3 = start1 + start2
        start1, start2 = start2, start3   #changing the values 
        terms += 1

# to find average
if (n!=0 or n<0):
 averagesum = sum(average)
 netans = averagesum / n
 print("the average of the fibonacchi sequence is " , netans)

#----------------------------------------------------------------------------------------------------------------------------------------------
#Question 8 
print( "Question 8\n ")
set1= {1, 2, 3, 4, 5}                     # mentioning the sets 
set2= {2, 4, 6, 8}
set3= {1, 5, 9, 13, 17}
# part a
seta = set1^set2                          # excluding common elements 
print("The solution for the part is : " , seta) 
# part b
setb = set1^set2^set3                     # excluding common from three 
print("The solution for the part is : " , setb)
# part c in exactly 2 sets)               # combinig elements of 2 sets and then excluding common   
setc1 = (set1 &set2)       
setc2 = (set2 &set3)
setc3 = (set1 &set3)
setc = setc1^setc2^setc3
print("The solution for the part is : " , setc)
# part d 
setd1 = set(range(1 , 11 ))               # excuding set 1  from the range 
setd = setd1-set1                    
print("The solution for the part is : " , setd)
# part e  
sete = setd1 - set1 -set2-set3            # excluding all sets from the range 
print("The solution for the part is : " , sete)

#-----------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------
