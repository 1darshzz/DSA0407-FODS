import numpy as np
sale_price_column = house_data[:, 2]
more_than_four_bedrooms_mask = house_data[:, 0] > 4   
sale_prices_more_than_four_bedrooms = sale_price_column[more_than_four_bedrooms_mask]
average_sale_price_more_than_four_bedrooms = np.mean(sale_prices_more_than_four_bedrooms)
print("Average Sale Price of Houses with More than Four Bedrooms:", average_sale_price_more_than_four_bedrooms)
