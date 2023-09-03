def gradingStudents(grades):
    # Write your code here
    result = []
    for grade in grades:
        tempo_grade = grade
        while tempo_grade%5 != 0:
            tempo_grade += 1
        else:
            if tempo_grade - grade < 3 and grade >= 38:
                result.append(tempo_grade)
            else:
                result.append(grade)
    return result
