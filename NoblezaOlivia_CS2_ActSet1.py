student = {} 
name = input("Enter your name") 
age = input("Enter your age") 
subject = input("Enter your fav subject") 

student["name"] = name 
student["age"] = age 
student["subject"] = subject 

print("Student Record:") 
print("Name:", student["name"]) 
print("Age:", student["age"]) 
print("Favorite Subject:", student["subject"])