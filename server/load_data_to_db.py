from sqlalchemy import create_engine
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import numpy as np

# making connection
conn_str = 'postgresql://gveoaihnqvuuvj:dfe4ed4802ec0afa6cca854eb97b5e5d9a3f1f0bbae6ddba7f7585004f50363c@ec2-34-204-128-77.compute-1.amazonaws.com:5432/dvifbu9viiudm'
engine = create_engine(conn_str)

# # loadind kks_description data
# df_kks_table = pd.read_csv(r'C:\Users\M ZOHAIB HASSAN\Desktop\HUBCO\1. Database\kks_description.csv')
# df_kks_filter = df_kks_table.drop_duplicates('kks')
# df_kks_filter = df_kks_filter[~df_kks_table.kks.isnull()]
# #df_kks_filter.to_sql('kks_description', engine, if_exists='append',index=False)


# # loading reporting data
# df_kks_table = pd.read_sql("""SELECT * FROM kks_description;""",con=engine).drop('id',axis=1)
# df_data_input_table = pd.read_sql("""SELECT * FROM data_input_table;""",con=engine).drop('id',axis=1)
# df_app_daily_stats = pd.read_sql("""SELECT * FROM app_daily_stats;""",con=engine).drop('id',axis=1)

# df_kks_filter = df_kks_table[['kks','min_value','max_value']]
# df_join = df_kks_filter.merge(df_data_input_table,on = 'kks')
# df_join.date = pd.to_datetime(df_join.date)
# df_join['shift'] = np.where(((df_join.date.dt.hour>=8) & (df_join.date.dt.hour<20)),'Morning Shift','Night Shift')
# df_join['max_value_breached'] = np.where(df_join.value>=df_join.max_value,1,0)
# df_join['min_value_breached'] = np.where(df_join.value<=df_join.min_value,1,0)
# df_join['kks_inactive_count'] = np.where(df_join.inactive.isin(['true','True',1]),1,0)
# df_reporting_table = df_join[['date','shift','max_value_breached','min_value_breached','kks_inactive_count','kks']]
# df_reporting_table = df_reporting_table.groupby([df_reporting_table.date.dt.date,'shift'])\
#      .agg({'max_value_breached':sum,'min_value_breached':sum,'kks_inactive_count':sum,'kks':'count'}).reset_index()
# df_reporting_table['kks_reading_percentage'] = round(df_reporting_table.kks*100/(603-df_reporting_table.kks_inactive_count),2)
# df_reporting_table.drop('kks',axis=1,inplace=True)

# #df_reporting_table.to_sql('app_daily_stats', engine, if_exists='append',index=False)

#df_dummy_input_data = pd.read_excel(r"C:\Users\M ZOHAIB HASSAN\Desktop\HUBCO\1. Database\13. dummy_input_data.xlsx")
#df_dummy_input_data.kks.dropna(inplace=True)

# df_input = df_dummy_input_data[pd.to_datetime(df_dummy_input_data.date)>=pd.to_datetime('2021-07-24')]
#df_dummy_input_data.to_sql('data_input_table', engine, if_exists='append',index=False)

# df_kks = pd.read_excel(r"C:\Users\M ZOHAIB HASSAN\Desktop\HUBCO\1. Database\kks_description_table.xlsx")
# df_kks.to_sql('kks_description', engine, if_exists='append',index=False)
