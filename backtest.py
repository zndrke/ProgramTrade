import pyupbit
import numpy as np

coins = ["KRW-BTC", "KRW-XRP", "KRW-VET", "KRW-SC", "KRW-ETC","KRW-IOST"]
result = pyupbit.get_ohlcv("KRW-BTC", count=0)

for c in coins:
    df = pyupbit.get_ohlcv(c, count=7)
    df['range'] = (df['high'] - df['low']) * 0.5
    df['target'] = df['open'] + df['range'].shift(1)

    df['ror'] = np.where(df['high'] > df['target'],
                        df['close'] / df['target'] ,
                        1)

    df['hpr'] = df['ror'].cumprod()
    df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
    df['name'] = c;
    print("MDD(%): ", df['dd'].max())
    result = result.append(df)
result.to_excel("dd.xlsx")