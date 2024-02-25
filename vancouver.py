import pandas as pd
import matplotlib.pyplot as plt

file_path = 'street-trees.xlsx' # opendata.vancouver.ca
data_frame = pd.read_excel(file_path) # thanks pandas

street_tree_count = data_frame['STD_STREET'].value_counts().head(25) # just the top 25
street_tree_count.plot(kind='bar', figsize=(10, 6), title='Top 25 Tree Streets')
plt.xlabel('Street')
plt.ylabel('Number of Trees')
plt.xticks(rotation=45)
plt.tight_layout() 
plt.show()