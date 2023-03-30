
from yahoo_fin import stock_info as si
from yahoo_fin.stock_info import get_analysts_info
from yahoo_fin.stock_info import get_balance_sheet
from yahoo_fin.stock_info import get_data
from yahoo_fin.stock_info import get_stats
from yahoo_fin.stock_info import get_stats_valuation
import pandas as pd

ticker = input("vloz ticker firmy kterou chceš napr. APPL: ")



data2 = si.get_data(ticker)
print(data2.head())
print(get_balance_sheet(ticker))
print(get_stats(ticker))
valuations = get_stats_valuation(ticker)
print(get_stats_valuation(ticker))

#from valuation get price/sales
print(valuations)
#turn valuation into dataframe
df = pd.DataFrame(valuations)

row= df.loc[df[0] == 'Price/Sales (ttm)']
row1= df.loc[df[0] == 'Price/Book (mrq)']
price_sales = row.iloc[0,1]
price_book = row1.iloc[0,1]
print(price_sales)
print(price_book)

#import pandas_datareader as pdr

#ticker = "AAPL"
#data1 = pdr.get_data_yahoo(ticker)


#import pyfinance as pf

#ticker = "AAPL"
#data = pf.get_data_yahoo(ticker)