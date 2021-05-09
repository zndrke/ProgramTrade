import pyupbit
import numpy as np
coins = ["KRW-BTC", "KRW-ETH", "KRW-DOGE", "KRW-XRP", "KRW-ADA", "KRW-DOT", "KRW-BCH","KRW-LTC","KRW-LINK", "KRW-ETC", "KRW-VET", "KRW-EOS", "KRW-SC","KRW-SXP","KRW-BTT", "KRW-WAVES", "KRW-IOST", "KRW-OMG", "KRW-BTG", "KRW-TRX", "KRW-NEO"]

result = pyupbit.get_ohlcv("KRW-TRX", count=0)

for c in coins:
    df = pyupbit.get_ohlcv(c, interval="day", count=20)
    df['range'] = (df['high'] - df['low']) * 0.5
    df['target'] = df['open'] + df['range'].shift(1)

    df['ror'] = np.where(df['high'] > df['target'],
                        df['close'] / df['target'] ,
                        1)

    df['hpr'] = df['ror'].cumprod()
    df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
    df['name'] = c;
    print("MDD(%): " + c, df['dd'].max())
    result = result.append(df)
result.to_excel("dd.xlsx")