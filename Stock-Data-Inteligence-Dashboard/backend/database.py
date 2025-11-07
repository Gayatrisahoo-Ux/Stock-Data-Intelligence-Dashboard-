import sqlite3,pandas as pd;from pathlib import Path
DB=Path(__file__).parent/'stocks.db';CSV=Path(__file__).parent.parent/'data'/'stock_data.csv'
def init_db(): 
 if DB.exists():return
 df=pd.read_csv(CSV);c=sqlite3.connect(DB);df.to_sql('stocks',c,index=False);c.close()
