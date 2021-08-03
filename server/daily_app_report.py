from sqlalchemy import create_engine
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import numpy as np
import datetime

#connection_local
engine_local = create_engine('postgresql://postgres:password@localhost:5432/hubco')
# making connection
conn_str = 'postgresql://gveoaihnqvuuvj:dfe4ed4802ec0afa6cca854eb97b5e5d9a3f1f0bbae6ddba7f7585004f50363c@ec2-34-204-128-77.compute-1.amazonaws.com:5432/dvifbu9viiudm'
engine = create_engine(conn_str)
limit_date = (datetime.datetime.now()-datetime.timedelta(3)).strftime('%Y-%m-%d 00:00:00')

#col_data_input_table = ['kks', 'date', 'value', 'remarks', 'inactive']
#df_data_input_table = pd.DataFrame(columns=col_data_input_table)

col = ['date', 'shift', 'max_value_breached', 'min_value_breached',
       'kks_inactive_count', 'kks_reading_percentage']
data = [[np.nan for i in range(len(col))]]

# loading data tables
df_kks_table = pd.read_sql("""SELECT * FROM kks_description;""",con=engine).drop('id',axis=1)

df_data_input_table = pd.read_sql("""SELECT * FROM data_input_table
                                   WHERE date>='{}';""".format(limit_date),con=engine).drop('id',axis=1)

df_app_daily_stats = pd.read_sql("""SELECT * FROM app_daily_stats
                                   WHERE date>='{}';""".format(limit_date),con=engine).drop('id',axis=1)

latest_date_in_input_table = pd.to_datetime(df_data_input_table.date).max()
if pd.isnull(latest_date_in_input_table):
     latest_date_in_input_table = limit_date[:10]
     

#handling empty report table
if not df_app_daily_stats.empty:
     latest_date_in_report  = pd.to_datetime(df_app_daily_stats.date).max()
else:
     df_reporting_table = pd.DataFrame(data=data,columns=col)
     df_reporting_table.date = latest_date_in_input_table.strftime('%Y-%m-%d')
     latest_date_in_report  = pd.to_datetime(df_reporting_table.date).max()
     
def generate_report():
     df_kks_filter = df_kks_table[['kks','min_value','max_value']]
     df_join = df_kks_filter.merge(df_data_input_table,on = 'kks')
     df_join.date = pd.to_datetime(df_join.date)
     df_join['shift'] = np.where(((df_join.date.dt.hour>=8) & (df_join.date.dt.hour<20)),'Morning Shift','Night Shift')
     df_join['max_value_breached'] = np.where(df_join.value>=df_join.max_value,1,0)
     df_join['min_value_breached'] = np.where(df_join.value<=df_join.min_value,1,0)
     df_join['kks_inactive_count'] = np.where(df_join.inactive.isin(['true','True',1]),1,0)
     df_reporting_table = df_join[['date','shift','max_value_breached','min_value_breached','kks_inactive_count','kks']]
     df_reporting_table = df_reporting_table.groupby([df_reporting_table.date.dt.date,'shift'])\
          .agg({'max_value_breached':sum,'min_value_breached':sum,'kks_inactive_count':sum,'kks':'count'}).reset_index()
     df_reporting_table['kks_reading_percentage'] = round(df_reporting_table.kks*100/(603-df_reporting_table.kks_inactive_count),2)
     df_reporting_table.drop('kks',axis=1,inplace=True)

     if df_reporting_table.empty:
          df_reporting_table = pd.DataFrame(data=data,columns=col)
          #df_reporting_table.date = latest_date_in_input_table.strftime('%Y-%m-%d')          
          record  = df_reporting_table
     else:
          record  = df_reporting_table#[pd.to_datetime(df_reporting_table.date)>latest_date_in_report]

     return record#.to_sql('app_daily_stats', engine, if_exists='append',index=False)

generate_report()
