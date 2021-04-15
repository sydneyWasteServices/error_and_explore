import pandas as pd
import numpy as np

# PATH = '/media/sf_BLOB_STORAGE/employeeID/employeeID.xlsx'

PATH = "/media/sf_BLOB_STORAGE/Tanda_weekly/all_df.csv"
df = pd.read_csv(PATH)
df[['lastname', 'firstname']] = df.Name.str.lower().str.split(" ", 1, expand=True)


# df_1['Name'] = df_1.Name.str.lower()

# # df_1['firstname'] = df_1.firstname.str.partition(' ')[0]
# df_1['firstname'] = df_1['firstname'].str.lstrip()
# df_1[['firstname', 'middlename']] = df_1.firstname.str.split(" ", 1, expand=True)

print(df)