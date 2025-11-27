while True:
    print("*" * 50)
    print("      STUDENT MARKS REPORT - VERSION 2")
    print("*" * 50)
    #Student details
    Name = input("Enter the Name: ")
    Rollno = input("Enter the Rollno: ")
    print("\n" + "*" * 50)
    print(" TOTAL MARKS IN SUBJECT (OUT OF 100)")
    print("*" * 50)
    #Subjects
    English = int(input("English : "))
    Maths = int(input("Maths   : "))
    Physics = int(input("Physics : "))
    Chemistry = int(input("Chemistry : "))
    Python = int(input("Python : "))
    #Validation for marks
    if (English > 100 or Maths > 100 or Physics > 100 or Chemistry > 100 or Python > 100 or
        English < 0 or Maths < 0 or Physics < 0 or Chemistry < 0 or Python < 0):
        print("\n Invalid Marks Entered! Report is not generated.\n")
    else:
        #Total & Average
        Total = English + Maths + Physics + Chemistry + Python
        Average = Total / 5

        #Result & Grade
        if English < 35 or Maths < 35 or Physics < 35 or Chemistry < 35 or Python < 35:
            result = "FAIL"
            grade = "U"
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

        #Report Card Output on screen
        print("\n" + "*" * 50)
        print("              REPORT CARD")
        print("*" * 50)
        print("Name    :", Name)
        print("Roll No :", Rollno)
        print("English :", English)
        print("Maths   :", Maths)
        print("Physics :", Physics)
        print("Chemistry :", Chemistry)
        print("Python  :", Python)
        print("=" * 50)
        print("Total   :", Total)
        print("Average :", Average)
        print("Result  :", result)
        print("Grade   :", grade)
        print("*" * 50)
        
    #Menu options and run again
    choice = input("Do you want to enter another student? (yes/no): ").lower()
    if choice != "yes":
        print("\n Thank you for using Student Report System Version 3!")
        break
