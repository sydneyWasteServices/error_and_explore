import pandas as pd
import numpy as np
from sqlalchemy import (Numeric, create_engine, Table, Column, 
                        Integer, String, MetaData, Float, Date, 
                        Time, SmallInteger, Text)


def inspect_row_error(path):
    print(path)
#     encoding='iso8859' encoding='cp1252'
    df = (
            pd
             .read_csv(
                       path,
                       dtype={
                           "Schd Time Start" : str,
                           "PO": str,
                           "Route number" : str},
                       encoding='iso8859')
    )
    
    df["Date"] = pd.to_datetime(df["Date"], format='%d/%m/%y')
    df[['Route number', 'Weekday']] = df['Route number'].str.split('-', 1, expand=True)
    
    db = "STAGE_TABLES_DB_1"
    sch = "BOOKING"
    tablename = "STAGE_TABLE_1"
    
    status = "append"
    
    user = "SA"
    pwd = "ploi?H8597"
    db = "STAGE_TABLES_DB_1"
    server = "gordonswsmaster"
    driver = "ODBC+Driver+17+for+SQL+Server"
    engine_str = f"mssql+pyodbc://{user}:{pwd}@{server}/{db}?driver={driver}"
    engine = create_engine(engine_str)

# Total Rows
    df_shape = df.shape
# Extract Total Row Number
    num_row = df_shape[0]
    
    for i in num_row:
        try:
                df_1 = df.iloc[[i]]
                df_1.to_sql(name=tablename, con=engine, schema=sch, if_exists=status, dtype={
                    'Job No': Numeric(20, 5),
                    'Date': Date(),
                    'Schd Time Start': String(length=350),
                    'Schd Time End': String(length=350),
                    'Latitude': Numeric(20, 7),
                    'Longitude': Numeric(20, 7),
                    'Customer number': Numeric(20, 5),
                    'Customer Name': String(length=800),
                    'Site Name': String(length=800),
                    'Address 1': String(length=1200),
                    'Address 2': String(length=1200),
                    'City': String(length=500),
                    'State': String(length=30),
                    'PostCode': Integer(),
                    'Zone': String(length=500),
                    'Phone': String(length=600),
                    'Qty Scheduled': SmallInteger(),
                    'Qty Serviced': SmallInteger(),
                    'Serv Type': String(length=600),
                    'Container Type': String(length=20),
                    'Bin Volume': Float(precision=5),
                    'Status': String(length=5),
                    'Truck number': String(length=50),
                    'Route number': String(length=50),
                    'Generate ID': String(length=500),
                    'Initial Entry Date': String(length=350),
                    'Weight': Float(precision=5),
                    'Prorated Weight': Float(precision=5),
                    'Booking Reference 1': String(length=200),
                    'Booking Reference 2': String(length=200),
                    'Alternate Ref No 1': String(length=200),
                    'Alternate Ref No 2': String(length=200),
                    'Alternate Service Ref 1': String(length=200),
                    'Alternate Service Ref 2': String(length=200),
                    'Notes': Text(length=8000),
                    'Directions': Text(length=8000),
                    'CheckLists': String(length=300),
                    'Waste Type': String(length=350),
                    'Tip Site': String(length=450),
                    'Price': Numeric(8, 3),
                    'PO': String(length=200)
                })
            
        except Exception:
            print(Exception)
            print(df_1['Job No'])
        