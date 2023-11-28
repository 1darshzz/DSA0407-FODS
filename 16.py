import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score,classification_report

np.random.seed(0)
num_samples = 200
age = np.random.randint(20, 80, size=num_samples)
gender = np.random.choice(['Male', 'Female'], size=num_samples)
blood_pressure = np.random.randint(80, 160, size=num_samples)
cholesterol = np.random.randint(120, 300, size=num_samples)
treatment_outcome = np.random.choice(['Good', 'Bad'], size=num_samples)
data = pd.DataFrame({
'Age': age,
'Gender': gender,
'BloodPressure': blood_pressure,
'Cholesterol': cholesterol,
'Outcome': treatment_outcome
})
data = pd.get_dummies(data, columns=['Gender'], drop_first=True)
features = ['Age', 'BloodPressure', 'Cholesterol', 'Gender_Male']
target = 'Outcome'
X = data[features]
y = data[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, 
random_state=42)
k = 5
model = KNeighborsClassifier(n_neighbors=k)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print(f"Precision: {precision_score(y_test, y_pred, pos_label='Good'):.2f}")
print(f"Recall: {recall_score(y_test, y_pred, pos_label='Good'):.2f}")
print(f"F1-Score: {f1_score(y_test, y_pred, pos_label='Good'):.2f}")
print("Classification Report:")
print(classification_report(y_test, y_pred))
