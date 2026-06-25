
# print name of students of 2nd lowest marks in asc order

# records = [["chi", 20.0], ["beta", 50.0], ["alpha", 50.0]]
# output:
# alpha
# beta

if __name__ == '__main__':
    students=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        
    # find unique score
    unique_score = sorted(list(set([score for name, score in students])))
    
    # 2nd lowest mark
    second_low_mark = unique_score[1]
    
    # 2nd lowest students
    second_low_students = sorted([name for name, score in students if score==second_low_mark])
    
    # print thier names
    for name in second_low_students:
        print(name)