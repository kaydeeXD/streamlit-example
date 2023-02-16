from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


import backtrader as bt
import streamlit as st
import pandas as pd
from datetime import datetime

# Define the Backtrader strategy
class MyStrategy(bt.Strategy):
    params = dict(
        ma_period_fast=10,
        ma_period_slow=20
    )

    def __init__(self):
        self.ma_fast = bt.indicators.SMA(period=self.params.ma_period_fast)
        self.ma_slow = bt.indicators.SMA(period=self.params.ma_period_slow)
        self.crossover = bt.indicators.CrossOver(self.ma_fast, self.ma_slow)

    def next(self):
        if not self.position:
            if self.crossover > 0:
                self.buy()

        elif self.crossover < 0:
            self.sell()

# Define the Streamlit app
def app():
    st.title('Backtrader Strategy')
    st.write('Enter the strategy parameters:')
    ma_period_fast = st.slider('MA Fast Period', 5, 30, 10, 5)
    ma_period_slow = st.slider('MA Slow Period', 10, 60, 20, 10)

    # Load the data
    data = bt.feeds.PandasData(dataname=pd.read_csv('AAPL.csv'), fromdate=datetime(2010, 1, 1), todate=datetime(2021, 1, 1))

    # Create the cerebro engine
    cerebro = bt.Cerebro()

    # Add the data to the engine
    cerebro.adddata(data)

    # Add the strategy to the engine
    cerebro.addstrategy(MyStrategy, ma_period_fast=ma_period_fast, ma_period_slow=ma_period_slow)

    # Run the backtest
    cerebro.run()

    # Plot the results
    st.line_chart(pd.DataFrame(cerebro.broker.get_value(), columns=['Portfolio Value']))

# Run the app
app()
