from requests import NullHandler
from yahooquery import Ticker, ticker
import csv

symbols = {'AAPL', 'ABBV', 'ABT', 'ACN','ADBE','AIG',
'AMGN','AMT','AMZN','AVGO','AXP','BA','BAC','BIIB','BK',
'BKNG','BLK','BMY','BRK.B','C','CAT','CHTR','CL','CMCSA',
'COF','COP','COST','CRM','CSCO','CVS','CVX','DD','DHR',
'DIS','DOW','DUK','EMR','EXC','F','FB','FDX','GD','GE',
'GILD','GM','GOOG','GOOGL','GS','HD','HON','IBM','INTC',
'JNJ','JPM','KHC','KO','LIN','LLY','LMT','LOW','MA','MCD',
'MDLZ','MDT','MET','MMM','MO','MRK','MS','MSFT','NEE','NFLX',
'NKE','NVDA','ORCL','PEP','PFE','PG','PM','PYPL','QCOM','RTX',
'SBUX','SO','SPG','T','TGT','TMO','TMUS','TSLA','TXN',
'UNH','UNP','UPS','USB','V','VZ','WBA','WFC','WMT','XOM'}

tickers = Ticker(symbols)
data = tickers.summary_detail
asset_profile= tickers.asset_profile
calendarEvents= tickers.calendar_events

'I should continue on this one'


for x in symbols:
    a_file = open(f"{x}_summary_detail.csv", "w", encoding="utf-8")
    a_dict = data[x].items()
    if a_dict == None:
        pass
    else:
        writer = csv.writer(a_file)
        for key, value in a_dict:
            writer.writerow([key , value])

        a_file.close()
        print("summary done")

for x in symbols:
    a_file = open(f"{x}_calendarEvents.csv", "w", encoding="utf-8")
    a_dict = calendarEvents[x].items()
    if a_dict == None:
        pass
    else:
        writer = csv.writer(a_file)
        for key, value in a_dict:
            writer.writerow([key , value])

        a_file.close()
        print("calendarEvents done")

for x in symbols:
    a_file = open(f"{x}_asset_profile.csv", "w", encoding="utf-8")
    a_dict = asset_profile[x].items()
    if a_dict == None:
        pass
    else:
        writer = csv.writer(a_file)
        for key, value in a_dict:
            writer.writerow([key , value])

        a_file.close()
        print("asset profile done")





