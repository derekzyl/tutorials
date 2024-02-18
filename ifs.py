

# create a simple calculator using ifelse statement

# a body mas index write a program to detrmine the persons bmi =m*h**2 


# mass =input("please enter your mass in kilograms ")
# height =input("please enter your height in meters ")

# m = float(mass)
# h=float(height)
# bmi = m/h**2

# # optimal = 18.5 -25

# if(bmi >25.0):
#     print("overweight")
# elif(bmi <18.5):
#     print("underweight") 
# elif(bmi>=18.5  and bmi <= 25.0 ):
#     print("optimal") 



# calculator

val1 = float(input("first value ")  )            
computation = input("computation ")              
val2 = float(input("second  value ")  )   

if(computation =="+"):
    print(val1 + val2)
elif(computation =="-"):
    print(val1 - val2)
elif(computation =="*"):
    print(val1 * val2)
elif(computation =="/"):
    print(val1 * val2)
else:
    print("computation coming soon")
    
