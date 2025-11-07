
# Stock Data Intelligence Dashboard — Demo

This is a simple demo project for the internship assignment. It includes:
- A FastAPI backend exposing endpoints to fetch stock data and summaries.
- Data fetching & processing using yfinance + pandas (daily returns, 7-day moving average, volatility).
- A minimal frontend (index.html) using Plotly to visualize close price and compare two symbols.

## Files
- main.py          -> FastAPI application with endpoints:
    /companies
    /data/{symbol}?last=30
    /summary/{symbol}
    /compare?symbol1=...&symbol2=...&last=...
- data_prep.py     -> fetch and process functions
- index.html       -> demo frontend (open in browser)
- requirements.txt

## How it works (high level)
1. The backend uses `yfinance` to download historical daily prices for a given symbol (past ~400 days).
2. `clean_and_add_metrics()` computes:
   - daily return: (CLOSE - OPEN) / OPEN
   - 7-day moving average of CLOSE
   - 30-day volatility (std of daily returns)
   - a simple mock sentiment index (7-day mean of daily returns)
3. `/summary/{symbol}` computes 52-week high/low and average close using the last ~365 days.
4. The frontend calls `/companies` to list symbols, `/data/{symbol}` to plot recent closes or `/compare` to show two series.

## Run locally
1. Create virtualenv (recommended)
   python -m venv venv
   source venv/bin/activate   # Windows: venv\\Scripts\\activate

2. Install requirements
   pip install -r requirements.txt

3. Start the API
   python main.py
   # The API will run on http://localhost:8000

4. Open `index.html` in your browser (you can open file directly or serve it with a simple static server).
   - The frontend expects the API at http://localhost:8000

## Notes & Extensions
- This demo uses an in-memory cache for the session. For production use, persist to a DB (SQLite/Postgres).
- Add Swagger: FastAPI automatically exposes docs at /docs and /redoc.
- Optional improvements: Authentication, pagination, more analytics (correlations, top gainers/losers), predictions (simple ARIMA / linear model), Dockerfile, deployment on Render/AWS.

## Troubleshooting
- If `yfinance` fails due to network or rate limits, you can replace fetch_history with reading local CSV bhavcopy files.
