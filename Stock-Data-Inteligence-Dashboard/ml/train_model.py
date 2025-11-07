import pandas as pd,joblib;from sklearn.linear_model import LinearRegression;from pathlib import Path
csv=Path(__file__).parent.parent/'data'/'stock_data.csv';df=pd.read_csv(csv)
for s in df.Symbol.unique():
 d=df[df.Symbol==s].copy().sort_values('Date');d['Prev']=d.Close.shift(1);d=d.dropna()
 joblib.dump(LinearRegression().fit(d[['Prev','7_Day_MA']],d.Close),Path(__file__).parent/f'model_{s}.pkl')