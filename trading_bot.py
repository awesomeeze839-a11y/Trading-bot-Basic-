import pandas as pd

prices = [100, 102, 101, 105, 110, 108, 107, 111]
df = pd.DataFrame(prices, columns=["price"])

df["ma"] = df["price"].rolling(3).mean()

balance = 1000
holding = False

for i in range(len(df)):
    if pd.isna(df["ma"][i]):
        continue
    
    if df["price"][i] > df["ma"][i] and not holding:
        buy_price = df["price"][i]
        holding = True
        print("BUY at", buy_price)
    
    elif df["price"][i] < df["ma"][i] and holding:
        sell_price = df["price"][i]
        balance += sell_price - buy_price
        holding = False
        print("SELL at", sell_price)

print("Final balance:", balance)
