# A function that returns a string grade.
def grade(x):
    if (x < 0 or x > 100):
        return 'error'
    elif(x < 50):
        return 'F'
    elif(x >= 50 and x < 60):
        return 'C'
    elif(x >= 60 and x < 70):
        return 'B'
    elif(x >= 70 and x < 80):
        return 'A'
    elif(x >= 80 and x <= 100):
        return 'A+'
