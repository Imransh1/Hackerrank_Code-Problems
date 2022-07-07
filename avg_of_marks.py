if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    if query_name in student_marks.keys():
        marks = student_marks[query_name]
        x = 0
        for m in marks:
            x = x+m
        avg = x / len(marks)
        avg = format(avg, '.2f')
        #round(avg,2) 
        print(avg)
    else:
        pass