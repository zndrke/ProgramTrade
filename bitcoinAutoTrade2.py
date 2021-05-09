import time
import pyupbit
import datetime

access = ""
secret = ""

def get_target_price(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price

def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time

def get_current_price(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(tickers=ticker)[0]["orderbook_units"][0]["ask_price"]


def coinAutoTrade(k, ticker, amount):
    now = datetime.datetime.now()
    start_time = get_start_time(ticker)
    end_time = start_time + datetime.timedelta(days=1)

    target_price = get_target_price(ticker, k)
    current_price = get_current_price(ticker)
    # balance가 없으면 0이 나옴
    coin_balance = upbit.get_balance(ticker)
    if coin_balance == 0:
        balance_to_krw = 1;
    else:
        balance_to_krw = current_price * coin_balance 

    if start_time < now < end_time - datetime.timedelta(seconds=30):
        if target_price < current_price and balance_to_krw < 5000 :
            krw = upbit.get_balance("KRW")
            # 잔고가 5000원 이상이면 10만원 한도로 매수
            if krw > amount:
                krw = amount
            if krw > 5000:
                upbit.buy_market_order(ticker, krw*0.9995)
    else:
        if balance_to_krw > 5000:
            upbit.sell_market_order(ticker, coin_balance)
    time.sleep(1)
    return 0

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")

# 자동매매 시작
while True:
    try:
        coinAutoTrade(0.3,"KRW-ADA", 100000)
        coinAutoTrade(0.5,"KRW-BCH", 100000)
        coinAutoTrade(0.7,"KRW-OMG", 100000)
        coinAutoTrade(0.4,"KRW-DOGE", 50000)
        coinAutoTrade(0.5,"KRW-EOS", 50000)
        coinAutoTrade(0.5,"KRW-TRX", 50000)
        coinAutoTrade(0.3,"KRW-NEO", 50000)

    except Exception as e:
        print(e)
        time.sleep(1)