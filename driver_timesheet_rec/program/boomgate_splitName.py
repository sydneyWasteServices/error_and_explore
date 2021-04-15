import pandas as pd
import numpy as np

PATH_A = '/media/sf_BLOB_STORAGE/boomgate_weekly/14th_2021.xlsx'

df = pd.read_excel(PATH_A, header=1)

df['Department'] = df.Department.str.lower().str.startswith('operations')

df[["EmployeeID",'Employee']]  = df.Employee.str.lower().str.split("_", 1, expand=True)

df_entry = df[df['Time In'].str.lower().str.startswith('entry')]

df_exit = df[df['Time In'].str.lower().str.startswith('exit')]

df = df[~df['Time In'].str.lower().str.startswith('entry')]

df = df[~df['Time In'].str.lower().str.startswith('exit')]


print(df)

# df['Department'] = df.Department.str.lower()
# 



# driver_df['Employee'] = driver_df['Employee'].str.split(" ").str[-2]

# print(driver_df)




# df
# df['Department'] = df.Department.str.lower()
# df['Employee'] = df.Employee.str.lower()

# driver_df = df[df['Department'].str.startswith('operation')]
# # driver_df[['lastname', 'firstname']] = df['Employee'].str.split(' ', 1, expand=True)

# # clean_df['Employee'] = clean_df.Employee.str.lower()
# # clean_df[clean_df.Employee.str.contains('je')]
# # clean_df['Time In'] = clean_df['Time In'].str.lower()
# # clean_df[clean_df['Time In'].str.startswith('exit')]

# # df[df['Employee'].str.startswith('john')]
# driver_df[["EmployeeID",'Employee']]= driver_df["Employee"].str.split("_", 1, expand=True)

# # driver_df[['Employee','firstname', "lastname"]]
# driver_df.head()
# # driver_df.groupby('EmployeeID')['Employee'].count()
# path_exp = '/media/sf_BLOB_STORAGE/boomgate_weekly/boomgateID.csv'
# driver_df.groupby(['EmployeeID', pd.Grouper('Employee')])['Employee'].count().to_csv(path_exp)

# # driver_df[['Employee','EmployeeID']].to_csv('


# df.dropna(subset=['Department'], how='all')
# df["Department"].str.startswith('Operations').isnull().values
# df.dropna(axis=0, subset=['Department'], how="all")

# df['Employee'] = df['Employee'].str.split(" ").str[-1]

# df['Employee'] = df['Employee'].str.rsplit(' ', 1).str.get(0)

# df['Employee'].str.rsplit(' ', 1,expand=True)

# .str.split(' ', n=1 ,expand=True).str.get(1)

# df['Employee'].str.partition(' ')
# driver_df['Employee'].str.partition(' ')
# df['Employee']