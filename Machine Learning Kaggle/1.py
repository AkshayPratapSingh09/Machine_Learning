import pandas as pd

# save filepath to variable for easier access
melbourne_file_path = 'C:/Users/Ap/Desktop/Python/Machine Learning Kaggle/archive/melb_data.csv'
# read the data and store data in DataFrame titled melbourne_data
melbourne_data = pd.read_csv(melbourne_file_path) 
# print a summary of the data in Melbourne data
# melbourne_data.describe()
print(melbourne_data)
melbourne_data.columns
Index(['Suburb', 'Address', 'Rooms', 'Type', 'Price', 'Method', 'SellerG',
    'Date', 'Distance', 'Postcode', 'Bedroom2', 'Bathroom', 'Car',
    'Landsize', 'BuildingArea', 'YearBuilt', 'CouncilArea', 'Lattitude',
    'Longtitude', 'Regionname', 'Propertycount'],
    dtype='object')