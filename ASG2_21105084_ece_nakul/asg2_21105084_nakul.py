# question no 1

print ( 'question 1 ')
string = 'Python is a case sensitive language'                 # defining the string 

print ( 'part a' )
length= len(string)                                            #function of finding length
print ( "the length of the string is " ,length)                # printing the length

print("\npart b ")
ordere_str= string[::-1]                                       #reversing the order
print (ordere_str)                                             #printing the reversed order

print( '\npart c')
sliced= string[10:26]                                           # defining the new string
print ("printing after storing:",sliced)                        # printing 

print("\npart d ")
cut1=string[:10]                                                # cutting some part of string
cut2=string[26:]
new_added= "object oriented"

new_string =cut1+new_added+cut2  
print("the new made string is: ",new_string)                     # printing the new string

print('\npart e')
ind_a= string.find("a")                                          # finding a     
print ("the index of a is: ", ind_a)                             # printing the index of a 
 
print( "\npart f") 
sp_removed= string.replace(" ", "")                              # removing spaces
print (sp_removed)                                               # printing without spaces  

# //////////////////////////////////Question2//////////////////////////////////////////////
print ("\nquestion 2 ")
# defining variables
name = "Nakul Garg"
SID= "21105084"
department= "ECE"
cgpa= "9.1"
#filling the values
name1="Hey, %s Here!" %(name)
sid1="My SID is %s" %(SID)
cgpa1="I am from %s department and my CGPA is %s" %(department, cgpa)

# printing
print (name1)
print (sid1)
print (cgpa1)


# //////////////////////////////////Question 3 //////////////////////////////////////////////////
print("question 3 ")                                              # giving values
a = 56 
b = 10
print ('\npart a ')
_and= a&b                                                         #using and operator
print(_and)

print ("\npart b ")
_or = a|b                                                         #using or operator
print (_or )

print('\npart c')
_xor= a^b                                                         #using xor operator
print(_xor)

print('\npart d')                                                #using shift left operator
l_shifta= a<<2
l_shiftb= b<<2
print("after left shifting a ",l_shifta ,"\n after left shifting b ", l_shiftb)

print('\npart e')
r_shifta = a>>2                                                  #using right shift operator
r_shiftb = b>>4
print("after right shifting a ",r_shifta ,"\n after rei=ght shifting b ",r_shiftb )

# //////////////////////////////question4//////////////////////////////////////////
print("\nquestion 4 ")                                           
#entering the values
no1 = int(input('\nenter first no. '))
no2 = int (input('enter second no. '))
no3 = int(input ('enter third no. '))

if(no1>no2) :
    if (no1>no3) :                                                  #checking the greater number  
     print('the greatest no is : ' , no1)
    else :
        print ('the greatest no is: ' ,no3)
else :
    if(no2>no3):
        print ('the greatest no is: ' ,no2)
    else:
        print('the greatest no is: ' ,no3)

# ////////////////////////////////queston 5 ////////////////////////////////////////
print('\nquestion 5 ')
string= input("enter the string:" )                                  #taking input of the string
if('name' in string) :                                                # checkiing condition
    print ("Yes")
else :    
    print ("No")


# ///////////////////////////////////question 6 ///////////////////////////////////
print ('\nquestion 6 ')
side1 =int( input("enter first side of triangle :"))                # taking input of values 
side2 =int( input("enter second side of triangle :"))
side3 =int( input("enter third side of triangle :"))

if(side1+side2>side3 and side2+side3>side1 and side3+side1>side2):    # applying the condition using if else statement
    print ("YES")
else:
  print(" NO ")