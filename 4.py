import pandas
data = {
    'property ID':[123,456,789,102],
    'location':["TamilNadu","Kerala","Delhi","Andhra"],
    'no.of.beds':[1,28,5,4],
    'area':[400,800,692,851],
    'price':[800000,1600000,1200050, 1605000]
    }
property_data = pandas.DataFrame(data)
print(property_data)
avg_price = property_data.groupby('location')['price'].mean()
print("The average list of property price: ",avg_price)
more_than_4_beds = property_data[('no.of.beds')]>4
print("The no.of.propeties with more than 4 bedrooms : ",more_than_4_beds)
largest_area = property_data.loc[property_data['area'].idxmax()]
print("Largest area : ",largest_area)
