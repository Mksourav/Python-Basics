try:
    score = input("Enter Score:")
    score = float(score)
except:
    print("Error! Please enter the numeric value")
    quit()
if score >= 0.0:
    if score <= 1.0:
        if score >= 0.9:
            print ("A")
        elif score >= 0.8:
            print("B")
        elif score >= 0.7:
            print("C")
        elif score >= 0.6:
            print("D")
        else:
            print("F")
    else:
        print("Invalid score(It must be less than or equal to 1.0)")
else:
    print("Invalid score(It must be greater than or equal to 0.0)")
