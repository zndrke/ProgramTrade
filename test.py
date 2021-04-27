import pyupbit

access = "l2WOvMzxxkv9PQhEqwuikX6WxEphbNmO80M9ACi5"          # 본인 값으로 변경
secret = "ezvNxU4qbDaO8BtF2fFgT3NwfMru9L9vBTRQvtZJ"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)


##print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회
print(pyupbit.get_current_price(["KRW-BTC", "KRW-XRP", "KRW-VET", "KRW-SC", "KRW-ETC","KRW-IOST"]))

##df = pyupbit.get_ohlcv("KRW-VET", interval="day", count=5, to=None)
##print(df.tail())

##print(upbit.get_balances())

orderbook = pyupbit.get_orderbook("KRW-BTC")
bids_asks = orderbook[0]['orderbook_units']

for bid_ask in bids_asks:
    print(bid_ask)
