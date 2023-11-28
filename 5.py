import numpy as np
student_scores = np.array([
    [90, 85, 92, 88],
    [78, 92, 80, 75],
    [85, 88, 90, 87],
    [92, 78, 85, 88],
])
average= np.mean(student_scores, axis=0)
highest = np.argmax(average)
print("Average score for each subject:", average)
print("Subject with the highest average score:",highest)
