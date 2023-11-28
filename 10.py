import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
temperatures = [20, 22, 25, 28, 30, 32, 34, 32, 30, 28, 25, 22]
plt.plot(months, temperatures, marker='o', linestyle='-', color='r', label='Monthly Temperatures')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.title('Monthly Temperature Data')
plt.legend()
plt.show()
rainfall = [50, 40, 60, 30, 20, 10, 5, 15, 25, 35, 45, 55]
plt.scatter(months, rainfall, color='b', label='Monthly Rainfall', marker='o')
plt.xlabel('Month')
plt.ylabel('Rainfall (mm)')
plt.title('Monthly Rainfall Data')
plt.legend()
plt.show()
