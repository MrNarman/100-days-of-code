student_scores = [78, 65, 89, 92, 56, 74, 81, 68, 90, 85, 77, 62, 94, 88, 71, 59, 83, 69, 95, 80]

max_score = 0
for score in student_scores:
   if score > max_score:
       max_score = score

print(max_score)