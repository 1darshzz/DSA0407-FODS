import numpy as np
fuel_efficiency = np.array([25, 30, 28, 32, 26, 29, 31, 27, 33, 28])
average_fuel_efficiency = np.mean(fuel_efficiency)
print("Average Fuel Efficiency:", average_fuel_efficiency)
model_1 = 0  
model_2 = 3  
fuel_efficiency_model_1 = fuel_efficiency[model_1]
fuel_efficiency_model_2 = fuel_efficiency[model_2]
percentage_improvement = ((fuel_efficiency_model_2 - fuel_efficiency_model_1) / fuel_efficiency_model_1) * 100
print(f"Percentage Improvement from Model {model_1} to Model {model_2}: {percentage_improvement:.2f}%")
