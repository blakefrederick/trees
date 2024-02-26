import pandas as pd
import matplotlib.pyplot as plt

file_path = 'street-trees.xlsx' # opendata.vancouver.ca
data_frame = pd.read_excel(file_path) # thanks pandas

# # Trees by Street
street_tree_count = data_frame['STD_STREET'].value_counts().head(25) # just the top 25 streets
street_tree_count.plot(kind='bar', figsize=(10, 6), title='Top 25 Tree Streets')
plt.xlabel('Street')
plt.ylabel('Number of Trees')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# # Trees by Species
species_tree_count = data_frame['COMMON_NAME'].value_counts().head(25)
species_tree_count.plot(kind='bar', figsize=(15, 8), color='forestgreen', title='Top 25 Tree Species')
plt.xlabel('Species')
plt.ylabel('Number of Trees')
plt.xticks(rotation=75)
plt.tick_params(axis='x', which='major', labelsize=8)
plt.tight_layout()
plt.show()

# Trees Planted by Year
data_frame['DATE_PLANTED'] = pd.to_datetime(data_frame['DATE_PLANTED'])
data_frame['YEAR'] = data_frame['DATE_PLANTED'].dt.year # count trees by year
yearly_counts = data_frame.groupby('YEAR').size()
plt.figure(figsize=(15, 8))
yearly_counts.plot(kind='bar', color='indigo') 
plt.title('Trees Planted by Year')
plt.xlabel('Year Planted')
plt.ylabel('Number of Trees Planted')
plt.xticks(rotation=45)
plt.tight_layout() 
plt.show()