from datetime import datetime, timedelta
from yahoo_fin import stock_info as si
import pandas as pd

# Nastavení tickeru a počtu let
ticker = "^GSPC"
years = 5

# Výpočet datumu před 5 lety
end_date = datetime.today().strftime('%m/%d/%Y')
start_date = (datetime.today() - timedelta(days=years*365)).strftime('%m/%d/%Y')

# Stažení historických dat
historical_data = si.get_data(ticker, start_date=start_date, end_date=end_date)

# Uložení uzavíracích cen do DataFrame
close_prices = historical_data[["close"]].reset_index().rename(columns={"index": "Date"})

print(close_prices)
average_close_price = close_prices["close"].mean()
print(average_close_price)