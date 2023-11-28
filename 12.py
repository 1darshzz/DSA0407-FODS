import pandas as pd
sales_data = pd.DataFrame({
    'Product': ['A', 'B','C','D','E','F','G','H','I','K'],
    'Quantity': [10, 5, 8, 12, 3, 15, 9, 7, 14, 6],
    'Date': ['2023-10-05', '2023-10-10', '2023-10-15', '2023-10-20', '2023-10-25', '2023-10-05', '2023-10-20', '2023-10-10', '2023-10-15', '2023-10-25']
})
sales_data['Date'] = pd.to_datetime(sales_data['Date'])
start_date = pd.to_datetime('2023-10-01')
end_date = pd.to_datetime('2023-10-31')
filtered_data = sales_data[(sales_data['Date'] >= start_date) & (sales_data['Date'] <= end_date)]
product_sales = filtered_data.groupby('Product')['Quantity'].sum().reset_index()
sorted_products = product_sales.sort_values(by='Quantity', ascending=False)
top_5_products = sorted_products.head(5)
print(top_5_products)
