from datetime import datetime, timedelta
from yahoo_fin import stock_info as si

# Nastavení tickeru a počtu měsíců
ticker = "^GSPC"
months = 60

# Výpočet datumu před 24 měsíci
end_date = datetime.today().strftime('%m/%d/%Y')
start_date = (datetime.today() - timedelta(days=months*365/12)).strftime('%m/%d/%Y')

# Stažení historických dat
historical_data = si.get_data(ticker, start_date=start_date, end_date=end_date)

# Vykreslení grafu
import matplotlib.pyplot as plt

plt.plot(historical_data.index, historical_data["close"])
plt.title(f"{ticker} - {months} months")
plt.xlabel("Date")
plt.ylabel("Price ($)")
plt.show()