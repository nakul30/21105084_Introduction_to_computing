# ***********************************Question 1 ***********************************

print("Write a Python program to find average of three numbers entered by the user.")
print(" ")

# ---(Taking the inputof three no`s from user )---

num_1=int (input ("Enter the first no. : "))
num_2=int (input("Enter the second no. : "))
num_3=int (input("Enter the third no. : "))

average = (num_1+num_2+num_3)/3 #++++finding the average++++

print( "the average of the no's is : " , average ) # printing the average




# *************************************Question 2 *************************************
print("Write a python program to compute a person's income tax.")
print(" ")

gross_income=int(input("Enter the gross income : "))  # taking gross income 
no_of_dependents=int(input("Enter the no of dependents : ")) #taking no of dependents

std_ded= 10000 #defining the standard deduction 
dep_ded= 3000  #defining the dependent deduction

# +++finding the taxable amount++++++
Tax_amt= gross_income-std_ded-(no_of_dependents*dep_ded)

t_tax = Tax_amt*0.20 # finding the total tax to be paid 

print( "total tax to be paid is : " ,t_tax) #printing the total tax 



# ***************************************Question 3 *************************************
print("Write a python program to store different data type values into a list.")
print(" ")

std=['SID', 'Name' , 'Gender' , 'Course name' , 'CGPA' ] #making the list
std1=[ 21105084, 'Nakul', 'M' , 'ECE' , 9.8 ]
std2=[ 21105083, 'disha' , 'F', 'ECE' , 8.9  ]

print(std)
print(std1)
print(std2)

print (" ")





# *******************************Question 4 ********************************************

print("Write a python program to enter marks of 5 students into a list and display them in sorted manner.")
print (" ")

marks=[53,62,100,48,95] #giving input of marks

print('marks before sorted', marks) #printing marks befor sorting

marks.sort() #sorting the marks

print ( 'marks after sortment', marks)#printing final marks

print (" ")

# ******************************Question 5 *************************************************

print("part 1 \nremoving 4th colour")


color =['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

print( color)

del color[3]#deleting 4th color

print ("after deleting the colour")
print (color)               # printng the final color


print(" ")

print ( "part 2 \nRemove Black and Pink from the list and replace them with Purple.")
print(" ")

colour= ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'] # making tht list of colour
print(colour)


print("After replacing Black and Pink")

colour[3:5] = ['purple'] #changing the colour

print(colour)

print (" THE END ")










