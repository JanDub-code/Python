from datetime import datetime, timedelta
from yahoo_fin import stock_info as si
import numpy as np
import matplotlib.pyplot as plt

# Nastavení tickeru a počtu let
ticker = "^GSPC"
years = 5

# Výpočet datumu před pěti lety
end_date = datetime.today().strftime('%m/%d/%Y')
start_date = (datetime.today() - timedelta(days=years*365)).strftime('%m/%d/%Y')

# Získání historických dat za posledních 5 let
historical_data = si.get_data(ticker, start_date=start_date, end_date=end_date)

# Vytvoření seznamu pro ukládání předpovědí
predictions = []

# Výpočet lineární regrese pro každý den a vytvoření předpovědi o rok dopředu
for i in range(len(historical_data)):
    # Výpočet lineární regrese
    x = np.arange(i+1)
    y = historical_data["close"][:i+1].values
    fit = np.polyfit(x, y, deg=1)
    
    # Vytvoření předpovědi
    future_x = np.arange(i+1, i+13)
    future_y = fit[0] * future_x + fit[1]
    predictions.append(future_y[-1])
    
# Vykreslení grafu s uzavíracími cenami a předpovědmi
plt.plot(historical_data.index, historical_data["close"])
plt.plot(historical_data.index[-1]+timedelta(days=1), predictions[0], 'go', label="Prediction")
plt.plot(historical_data.index[-1:], predictions, 'go--')
plt.title(f"{ticker} - {years} years")
plt.xlabel("Date")
plt.ylabel("Price ($)")
plt.legend()
plt.show()