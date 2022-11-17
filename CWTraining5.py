#Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.

def get_grade(s1, s2, s3):
    avg = avg((s1+s2+s3)/3)
    if 90 <= avg <= 100:
        return ("A")
    elif 80 <= avg <= 90:
        return ("B")
    elif 70 <= avg <= 80:
        return("C")
    elif 60 <=avg <=70:
        return ("D")
    else:
        return ("F")

    