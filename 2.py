import pandas as pd
mydata = {
    'customer ID': [123, 456, 789],
    'product name': ["Mi", "Apple", "Samsung"],
    'order date': ['12-11-2023', '18-01-2023', '17-12-2023'],
    'order quantity': [3, 2, 1]
}
order_data = pd.DataFrame(mydata)
print(order_data)
avg_quantity = order_data.groupby('product name')['order quantity'].mean()
print("\nThe average order quantity for each product:\n", avg_quantity)
earliest_order_date = order_data['order date'].min()
latest_order_date = order_data['order date'].max()
print("\nEarliest order date:", earliest_order_date)
print("Latest order date:", latest_order_date)
