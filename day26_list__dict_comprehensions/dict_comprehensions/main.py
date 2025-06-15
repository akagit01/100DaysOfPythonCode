import random
import pandas
names=['Alex','Beth','Caroline','Dave','Eleanor','Freddie']
student_scores={name:random.randint(1,100) for name in names}

print(student_scores)

passed_students={name:score for name,score in student_scores.items() if student_scores.get(name) > 60   }
print(passed_students)

student_dict={"student":['ABC','DEF','XYZ'],
              "score":[50,40,60]}

student_data_frame=pandas.DataFrame(student_dict)
print(student_data_frame)

for (index,row) in student_data_frame.iterrows():
    #print(row)
    if row.student == 'ABC':
        print(row.score)


