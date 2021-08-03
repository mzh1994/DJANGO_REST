from json import load
from sqlalchemy import create_engine
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import numpy as np
import datetime
from .load_kks_data_table import load_kks_table

def generate_daily_report():
    n_days = 10 #threshold for report
    # making connection
    # conn_str = 'postgresql://gveoaihnqvuuvj:dfe4ed4802ec0afa6cca854eb97b5e5d9a3f1f0bbae6ddba7f7585004f50363c@ec2-34-204-128-77.compute-1.amazonaws.com:5432/dvifbu9viiudm'
    # engine = create_engine(conn_str)
    conn_str = 'postgresql://postgres:password@localhost:5432/test_db'
    engine = create_engine(conn_str)

    date_limit = (datetime.datetime.now()-datetime.timedelta(n_days)).strftime('%Y-%m-%d 00:00:00')

    # loading data tables
    #df_kks_table = pd.read_sql("""SELECT * FROM kks_description;""",con=engine).drop('id',axis=1)
    df_kks_table = load_kks_table() #loading from local as this table is fixed
    df_data_input_table = pd.read_sql("""SELECT * FROM data_input_table
                                    WHERE date>='{}';""".format(date_limit),con=engine).drop('id',axis=1)
    
    col = ['date', 'shift', 'max_value_breached', 'min_value_breached',
        'kks_inactive_count', 'kks_reading_percentage']

    if df_data_input_table.empty: #create empty df and put date to record empty values
        df = pd.DataFrame(columns=col)
        df.date = datetime.datetime.now().strftime('%Y-%m-%d')
        return df
    else:        
        latest_date_in_input_table = pd.to_datetime(df_data_input_table.date).max()
        #Main report calculation
        df_kks_filter = df_kks_table[['kks','min_value','max_value']]
        df_join = df_kks_filter.merge(df_data_input_table,on = 'kks',how='left')
        df_join.date = pd.to_datetime(df_join.date)
        df_join['shift'] = np.where(((df_join.date.dt.hour>=8) & (df_join.date.dt.hour<20)),'Morning Shift','Night Shift')
        df_join['max_value_breached'] = np.where(df_join.value>=df_join.max_value,1,0)
        df_join['min_value_breached'] = np.where(df_join.value<=df_join.min_value,1,0)
        df_join['kks_inactive_count'] = np.where(df_join.inactive.isin(['true','True',1]),1,0)
        df_reporting_table = df_join[['date','shift','max_value_breached','min_value_breached','kks_inactive_count','kks']]
        df_reporting_table = df_reporting_table.groupby([df_reporting_table.date.dt.date,'shift'])\
            .agg({'max_value_breached':sum,'min_value_breached':sum,'kks_inactive_count':sum,'kks':'count'}).reset_index()
        df_reporting_table['kks_reading_percentage'] = round(
            (df_reporting_table.kks-df_reporting_table.kks_inactive_count)*100/(603-df_reporting_table.kks_inactive_count),2)
        df_reporting_table.drop('kks',axis=1,inplace=True)
        if df_reporting_table.empty:
            df_reporting_table = pd.DataFrame(columns=col)
        else:
            record  = df_reporting_table
        return record