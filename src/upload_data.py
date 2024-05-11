import pandas as pd
import sqlite3


#mytestenv
medicine_data = {
    'name': ['Medicine A', 'Medicine B', 'Medicine C'],
    'price': [10.99, 20.49, 15.75],
    'qty': [100, 50, 75],
    'shelf_num_rows': [3, 2, 1],
    'date_added': ['2024/05/10', '2024/05/10', '2024/05/10']
}

df = pd.DataFrame(medicine_data)


conn = sqlite3.connect('medicine.db')

#If if_exists='replace', it will replace the existing table with the DataFrame data
df.to_sql('medicine_details', conn, if_exists='append', index=False)


conn.close()
