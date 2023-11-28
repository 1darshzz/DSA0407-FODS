import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [10000, 12000, 8000, 15000, 11000]
plt.plot(months, sales, marker='o', linestyle='-', color='b', label='Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Monthly Sales Data')
plt.legend()
plt.show()
plt.bar(months, sales, color='b', label='Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Monthly Sales Data')
plt.legend()
plt.show()
