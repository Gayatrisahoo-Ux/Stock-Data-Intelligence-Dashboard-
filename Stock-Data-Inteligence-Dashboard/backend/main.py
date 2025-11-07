from fastapi import FastAPI,HTTPException;import sqlite3,pandas as pd
from pathlib import Path;from . import database;app=FastAPI();DB=Path(__file__).parent/'stocks.db';database.init_db()
def q(s):c=sqlite3.connect(DB);d=pd.read_sql_query(s,c);c.close();return d
@app.get('/companies') 
def c():return q('select distinct Symbol from stocks')['Symbol'].tolist()
@app.get('/data/{s}') 
def d(s,limit:int=30):df=q(f"select * from stocks where Symbol='{s}' order by Date desc limit {limit}")
 return df.to_dict('records') if not df.empty else (_ for _ in ()).throw(HTTPException(404))
