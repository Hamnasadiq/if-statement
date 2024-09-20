age =int (input ("Enter your age:"))
if age>=18:
    print("You are eligible")
    qualification= input("Enter your qualification(e.g inter pass,bachelors,masters): ")
    if qualification.lower()=="inter pass" or qualification.lower()=="bachelors"or qualification.lower()=="masters":
        print("Qualification criteria met")
        gpa=float (input("enter your GPA:"))
        if gpa>= 3.5:
            print("GPA criteria met. You are eligible")
        else:
            print("Your GPA below is below the requirement. You are not eligible.")    
    else:
        print("Your qualification does not meet the requirement. You are not eligible")

else:
    print("You are not eligible")