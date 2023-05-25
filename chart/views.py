from django.shortcuts import render
from django.http import HttpResponse

from binance.spot import Spot
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime

# Create your views here.
def index(request):
    client = Spot()
    var = client.klines("BTCUSDT", "1M")
    client = Spot(api_key='WVLPyTugGloSA58cydZwAe27dDij6dYNvq2BFuUjCayo9UF2WHFTAwzio7YS8hKM', api_secret='dqBNrbhL03lVwjEPRMkLOzPC6cSUv2bzT45vDPqflnGVbhnOpFpoVy0brsbN6gd5')
    candle_stick_df = pd.DataFrame(var, columns = ['open_time', 'open_price', 'high_price', 'low_price', 'close_price', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trade', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'dates'])
    fig = go.Figure(data=[go.Candlestick(x=candle_stick_df['open_time'].apply(lambda x: datetime.fromtimestamp(x/1000.0).date()),
                open=candle_stick_df['open_price'],
                high=candle_stick_df['high_price'],
                low=candle_stick_df['low_price'],
                close=candle_stick_df['close_price'])])
    chart = fig.to_html()
    context = {'chart':chart}
    return render(request,'pages/chart.html',context)    
    #fig.update_layout(xaxis_rangeslider_visible=False)
    # fig.show()
    # response = HttpResponse()
    # response.writelines('<h1>Xinchao<h1>')
    # response.write('day la app home')
    # return response
