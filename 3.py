import pandas as pd
data = {
    'student ID': [11, 22, 33, 44],
    'course': ["DBMS", "FODS", "PDSD", "M3"],
    'score': [99, 88, 90, 83],
    'studying_hrs': [5, 3, 6, 2]
}
student_data = pd.DataFrame(data)
print("Original DataFrame:")
print(student_data)
correlation_per_course = student_data.groupby('course')[['studying_hrs', 'score']].corr()
print("\nCorrelation coefficient between studying_hrs and score for each course:",correlation_per_course)
strongest_corr_value = correlation_per_course.max()
weakest_corr_value = correlation_per_course.min()
print("\nCourses with the strongest correlation:",strongest_corr_value)
print("\nCourses with the weakest correlation:",weakest_corr_value)
average_stats_per_course = student_data.groupby('course')[['score', 'studying_hrs']].mean().reset_index()
print("\nAverage score and average hours studied for each course:",average_stats_per_course)
