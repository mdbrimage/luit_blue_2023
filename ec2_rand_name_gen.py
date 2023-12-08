"""
Several departments share an AWS environment. You need to ensure that the EC2s are properly named and are unique so team members can easily tell who the EC2 instances belong to. 
Use Python to create your unique EC2 names that the users can then attach to the instances. The Python Script should:
1. Allow the user to input how many EC2 instances they want names for and output the same amount of unique names.
2. Allow the user to input the name of their department that is used in the unique name.
3. Generate random characters and numbers that will be included in the unique name.
4. Push your code to GitHub and include the link in your LinkedIn write up.

ADVANCED
The only departments that should use this Name Generator are the Marketing, Accounting, and FinOps Departments. 
List these departments as options and if a user puts another department, print a message that they should not use this Name Generator. 
Be sure to account for incorrect upper or lowercase letters in the correct department. Example: a user inputs accounting vs Accounting.

COMPLEX
Turn the above into a Function and execute the Function to verify it works.
"""
import random 

num_ec2 = int(input('How many EC2 instances require names? '))

dept_name = input('What is your department? ')

name = ''

namecounter = 0


for letter in dept_name[0]:
        
        name = name + dept_name[0:3]
        namecounter +=1

        
print(name)

        
        
print(namecounter)
        


'''
while (namecounter < num_ec2):
    
    for letter in name[:3]:
        
        name = name + name[letter]
        namecounter +=1
        
        print(namecounter)
        
   '''     
#print(name)
        
#namecounter +=1
        
#print(namecounter)
        
#print(namecounter)
    
    #print(name)
    
    #print()
    



#while (len(name) < 8):
    