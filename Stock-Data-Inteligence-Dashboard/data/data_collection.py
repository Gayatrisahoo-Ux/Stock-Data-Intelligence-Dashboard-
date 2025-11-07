import yfinance as yf;import pandas as pd,os
SYMBOLS=['TCS.NS','INFY.NS','RELIANCE.NS'];OUT=os.path.join(os.path.dirname(__file__),'stock_data.csv')
frames=[]
for s in SYMBOLS:
 df=yf.download(s,period='1y',progress=False).reset_index()
 df['Symbol']=s;df['Daily_Return']=(df['Close']-df['Open'])/df['Open']
 df['7_Day_MA']=df['Close'].rolling(7).mean();df['52_Week_High']=df['Close'].rolling(252).max()
 df['52_Week_Low']=df['Close'].rolling(252).min();df['Volatility']=df['Close'].pct_change().rolling(20).std()
 frames.append(df)
pd.concat(frames).to_csv(OUT,index=False)