# Calculating grade by scores as parameters
# Two ways to avoid getting non-number data

# 1. Try-except

def computegrade(score):
    try:
        score = float(score)
        if score >= 0.9 and score <= 1:
            grade = "A"
        elif score >= 0.8 and score < 0.9:
            grade = "B"
        elif score >= 0.7 and score < 0.8:
            grade = "C"
        elif score >= 0.6 and score < 0.7:
            grade = "D"
        elif score < 0.6:
            grade = "F"
        else:
            grade = "Bad score"
        print(grade)
    except:
        grade = "Bad score"
        print(grade)

a = input("Enter score:")
computegrade(a)

# 2. type()

def computegrade(score):
    if type(score) == str:
        grade = "Bad score"
    elif type(score) != str and score >= 0.9 and score <= 1:
        grade = "A"
    elif score >= 0.8 and score < 0.9:
        grade = "B"
    elif score >= 0.7 and score < 0.8:
        grade = "C"
    elif score >= 0.6 and score < 0.7:
        grade = "D"
    elif score < 0.6:
        grade = "F"
    else :
        grade = "Bad score"
    print(grade)

a = input("Enter score:")
computegrade(a)