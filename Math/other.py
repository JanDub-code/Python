
from yahoo_fin import stock_info as si
from yahoo_fin.stock_info import get_analysts_info
from yahoo_fin.stock_info import get_balance_sheet
from yahoo_fin.stock_info import get_data
from yahoo_fin.stock_info import get_stats
from yahoo_fin.stock_info import get_stats_valuation
import pandas as pd

ticker = "AAPL"
data2 = si.get_data(ticker)
print(data2.head())

	
print(get_balance_sheet("AAPL"))
print(get_stats("AAPL"))
valuations = get_stats_valuation("AAPL")
print(get_stats_valuation("AAPL"))

#from valuation get price/sales
print(valuations)
#turn valuation into dataframe
df = pd.DataFrame(valuations)

row= df.loc[df[0] == 'Price/Sales (ttm)']
price_sales = row.iloc[0,1]
print(price_sales)

#import pandas_datareader as pdr

#ticker = "AAPL"
#data1 = pdr.get_data_yahoo(ticker)


#import pyfinance as pf

#ticker = "AAPL"
#data = pf.get_data_yahoo(ticker)