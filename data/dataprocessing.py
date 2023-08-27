import csv
import pandas as pd

df_main = pd.DataFrame(columns=['sales', 'date', 'region'])
df0 = pd.read_csv('daily_sales_data_0.csv')
df1 = pd.read_csv('daily_sales_data_1.csv')
df2 = pd.read_csv('daily_sales_data_2.csv')

df0['price'] = df0['price'].str.replace('$', '').astype(float)
df1['price'] = df1['price'].str.replace('$', '').astype(float)
df2['price'] = df2['price'].str.replace('$', '').astype(float)

df0['sales'] = df0['price'] * df0['quantity']
df1['sales'] = df1['price'] * df1['quantity']
df2['sales'] = df2['price'] * df2['quantity']

df0['sales'] = '$' + df0['sales'].astype(str)
df1['sales'] = '$' + df1['sales'].astype(str)
df2['sales'] = '$' + df2['sales'].astype(str)

filter_0 = df0['product'] != 'pink morsel'
filter_1 = df1['product'] != 'pink morsel'
filter_2 = df2['product'] != 'pink morsel'

df0 = df0.drop(index=df0[filter_0].index)
df1 = df1.drop(index=df1[filter_1].index)
df2 = df2.drop(index=df2[filter_2].index)

df0 = df0.drop(columns=['product', 'price', 'quantity'])
df1 = df1.drop(columns=['product', 'price', 'quantity'])
df2 = df2.drop(columns=['product', 'price', 'quantity'])

new_columns = ["sales", "date", "region"]
df0 = df0[new_columns]
df1 = df1[new_columns]
df2 = df2[new_columns]

df_main = df_main._append(df0, ignore_index=True)
df_main = df_main._append(df1, ignore_index=True)
df_main = df_main._append(df2, ignore_index=True)

df_main.to_csv('modified_daily_sales.csv', index=False)

print("Modified CSV created!")
