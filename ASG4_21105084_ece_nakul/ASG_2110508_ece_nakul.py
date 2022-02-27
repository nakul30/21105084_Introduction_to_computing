print('Question 1 ')
def tower( discs , a  ,b,c  ): # definingrecursive  function 
    if discs == 0 :    # base condition 
        return 
    elif discs > 0:
        tower(discs -1, a, c, b)
        print(f"Moving disc {discs} from {a} to {c}")
        tower(discs  -1, b,a,c)


tower( 3 , "A", "B", "c"  )  # calling the funcion 

# ---------------------------------------------------------------------------------------------

print("Question 2 ")
n = int ( input ( 'enter the no of rows.'))
# using loops 
print( 'using loops ')
def factorial( a ):     # defing factorial function 
    if a<=0 :
      return 1  
    else :  
      return  a * factorial( a-1)
def ncr( n , r ):         # defingin binomial cofficient 
    solu = factorial(n)//(factorial(r) * factorial(n-r))
    return solu 
for row  in range ( 0 , n ):   # printing the triangle 
    for space in range ( 0 , n-row):
        print( " " , end="")
    for coloumn in range ( 0 , row+1 ):
        print( ncr(row ,coloumn) , end="  ")
    print( "\n")   

# usin recursion 
print ("using recursion ")
def triangle(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    else:
        startrow = [1]
        lastrow = triangle(n-1)
        for i in range(len(lastrow)-1):
            startrow.append(lastrow[i] + lastrow[i+1])
        startrow=startrow +  [1]
    return startrow 
for row  in range ( 0 ,  n): 
    for coloumn  in range ( 0 , n - row + 1 ):
        print ( ' ' , end="")
    print ( triangle( row + 1 ))




# -------------------------------------------------------------------------------------------
print ('Question 3 ')
# taking input of numbers 
number1= int( input ( 'Enter the first number '))
number2= int( input ( 'Enter the second number '))
quotient = 1
remainder = 1  # makin global variables  
# defining function for finding quotient and reaminder  
def quoremain(num1 , num2):
    global  quotient , remainder 
    quotient = num1//num2
    remainder  = num1%num2
    storer  = ( quotient , remainder)
    print(f'the quotient is {quotient} and reaminder is {remainder}')
    return storer 
print('part a ')   # check ing callability 
print ( callable( quoremain) )  # checking that funtion made is callable or not 
print( 'part b ')  # checking set is zero or not 
stored = quoremain(number1 , number2)
print ( stored )
if stored ==(0,0):
    print( 'true , all zero ')
else:
    print('false , all or none is zero ')
print( 'part c ')  # appending new values 
storedlist = list( stored )
for i in range ( 4 , 7 ):
   storedlist.append( i  )
print( 'the new list after adding  is ' , storedlist )

listafterremoving = []
for i in range(len( storedlist)):
    if storedlist[i]<=4:
        listafterremoving.append(storedlist[i])

print( 'list after filtering greater than 4 is ',listafterremoving)        #filter out greater than 4 


print ( 'part d')  # converting ABOVE result  in set data type 
newset = set( listafterremoving )
print ( newset )

print('part e ') # frozen set 
newerset  = frozenset(newset)     # using imutable set funviton 
print ( newerset )

print( 'part f ')
maxvalue = max(set(newerset)) # max set function 
print ( 'the max value is ', maxvalue  )

hashvalue = hash( maxvalue)   # hashvalue functio n
print('the hashvalue is ' , hashvalue)
# -------------------------------------------------------------------------------------------
print ( "Question 4 ")
class Student:  # creating a class named student

    def __init__(self, name, rollno):  # using constructor function
        Student.name = name  # defining attributes
        Student.rollno = rollno
        print('object created and information stored')

    def printer(self):  # defining function to print information
        print(f'Name of student is {self.name} and roll no is {self.rollno}')

    def __del__(self):  #  defing destructor
        print('object destructed so cant be shoen by printing  ')


student1 = Student('Nakul Garg', 21105084)  # creating object

student1.printer()  # using function to print information

del student1  # calling destructon function

# student1.printer() ( THIS CANT BE USED AS IT WILL GIVE ERROR !)
# ---------------------------------------------------------------------------------------------
print('Question 5 ')
class Employee :       # forming a class 
    def __init__(self , name , salary ): # using constructor 
        self.name = name 
        self.salary = salary
        
    def __dele__(self):
        print( f'record deleted of {self.name}')
    def nameprint(self):
        print ( f'The name of the employee is {self.name}')
    def oldsalaryprint(self):
        print( f'the old salary of the employee name {self.name} is {self.salary}')

employee1 = Employee('Mehak' , 40000 )
employee2 = Employee('Ashok' , 50000 )
employee3 = Employee('Viren' , 60000 )

employee1.nameprint()
employee2.nameprint()
employee3.nameprint()

employee1.oldsalaryprint()
employee1.salary = 700000
print (f'the new salary of Mehak is {employee1.salary}') 
del employee3
# employee3.__dele__( )  #( IT CANT BE PRINTED AS IT IS DELETED )
# --------------------------------------------------------------------------------------------------
print("Question 6 ")
george_word = input( 'enter the george word ')  # taking input of the words 
barbie_word = input( 'enter the barbie word ')
def anagrams(s):    # defining anagrams of the funvtion 
    if s == "":
        return [s]
    else:
        ans = []
        for w in anagrams(s[1:]):
            for pos in range(len(w)+1):
                ans.append(w[:pos]+s[0]+w[pos:])
        return ans
storedanagrams  = anagrams(george_word)  # storin anagrams 
if barbie_word in storedanagrams :  # checking barbies word in anagrams 
    meaninful = input ( 'is the word meaningful ?')  # asking shopkeeper th word is meaningful or not 
    if  meaninful == "y" :

       print ( 'true friendship ')
    else :
        print ( 'fake friendship ')
else :
    print ( 'fake friendship ')