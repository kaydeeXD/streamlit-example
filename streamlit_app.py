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

# Define the Backtrader strategy
class MyStrategy(bt.Strategy):
    params = dict(
        sma_period_fast=20,
        sma_period_slow=50
    )

    def __init__(self):
        self.sma_fast = bt.indicators.SMA(period=self.params.sma_period_fast)
        self.sma_slow = bt.indicators.SMA(period=self.params.sma_period_slow)
        self.crossover = bt.indicators.CrossOver(self.sma_fast, self.sma_slow)

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
    sma_period_fast = st.slider('SMA Fast Period', 10, 100, 20, 10)
    sma_period_slow = st.slider('SMA Slow Period', 30, 200, 50, 10)

    # Load the data
    data = bt.feeds.PandasData(dataname=pd.read_csv('AAPL.csv'), fromdate=datetime(2010, 1, 1), todate=datetime(2021, 1, 1))

    # Create the cerebro engine
    cerebro = bt.Cerebro()

    # Add the data to the engine
    cerebro.adddata(data)

    # Add the strategy to the engine
    cerebro.addstrategy(MyStrategy, sma_period_fast=sma_period_fast, sma_period_slow=sma_period_slow)

    # Run the backtest
    cerebro.run()

    # Plot the results
    st.plotly_chart(cerebro.plot())
