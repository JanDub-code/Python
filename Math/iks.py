from yahoo_fin import stock_info as si
import pandas as pd

print(si.get_stats_valuation('nflx'))
valuations = si.get_stats_valuation('nflx')
df = pd.DataFrame(valuations)

row= df.loc[df[0] == 'Price/Sales (ttm)']
row1= df.loc[df[0] == 'Price/Book (mrq)']
price_sales = row.iloc[0,1]
price_book = row1.iloc[0,1]
print(price_sales)
print(price_book)





