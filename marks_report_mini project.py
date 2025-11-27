print("*"*50)
print("          Student marks report")
print("*"*50)
#student details
Name=input("Enter the Name:")
Rollno=input("Enter the Rollno:")
print("\n"+"*"*50)
print("\n TOTAL MARKS IN SUBJECT (OUT/100)")
print("\n"+"*"*50)
#subjects
English=int(input("English :"))
Maths=int(input("Maths :"))
Physics=int(input("Physics :"))
Chemistry=int(input("Chemistry :"))
Python=int(input("python :"))
# Validation for marks
if (English > 100 or Maths > 100 or Physics > 100 or Chemistry > 100 or Python > 100 or
    English < 0 or Maths < 0 or Physics < 0 or Chemistry < 0 or Python < 0):
    print("\n Invalid Marks Entered!")
else:
    #total average
    Total=English+Maths+Physics+Chemistry+Python
    Average=Total/5
    if  English < 35 or Maths< 35 or Physics < 35 or Chemistry < 35 or Python < 35:
        result = "FAIL"
        grade ="U"
    else:
        result = "PASS"
        if Average >= 90:
           grade = "A+"
        elif Average >= 80:
            grade = "A"
        elif Average >= 70:
            grade = "B+"
        elif Average >= 60:
            grade = "B"
        elif Average >= 50:
            grade = "C" 
        else:
            grade = "U"
# Report Card Output
print("\n" + "*" * 50)
print("              REPORT CARD")
print("\n"+"*"*50)
print("Name    :", Name)
print("Roll No :", Rollno)
print("Total   :", Total)
print("Average :", Average)
print("Result  :", result)
print("Grade   :", grade)
print("*" * 50)
