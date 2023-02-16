import streamlit as st

class MeanReversion(bt.Strategy):
    params = (
        ('period', 100),
        ('deviation', 2),
        ('trail_percent', 0.03),
    )

    def __init__(self):
        self.sma = bt.indicators.SimpleMovingAverage(
            self.data.close, period=self.params.period
        )
        self.order = None
        self.stop_price = None

    def next(self):
        if not self.position:
            if self.data.close < self.sma[0] - self.params.deviation:
                self.order = self.buy()
                self.stop_price = self.data.close * (1 - self.params.trail_percent)
        else:
            if self.data.close > self.sma[0] + self.params.deviation:
                self.close()
                self.order = None
                self.stop_price = None
            elif self.data.close < self.stop_price:
                self.close()
                self.order = None
                self.stop_price = None
            else:
                self.stop_price = self.data.close * (1 - self.params.trail_percent)

# Define the Streamlit app
def main():
    # Set the app title
    st.set_page_config(page_title='Backtrader Strategy', page_icon=':chart_with_upwards_trend:')

    # Set the app header
    st.header('Backtrader Strategy')

    # Define the sidebar
    st.sidebar.header('Settings')
    ticker = st.sidebar.text_input('Enter Ticker Symbol', 'AAPL')
    start_date = st.sidebar.date_input('Start Date')
    end_date = st.sidebar.date_input('End Date')

    # Create a Bokeh plot for displaying the strategy
    bokeh_plot = st.plot(style='bar', plot_mode='single')

    # Run the strategy with the given settings
    cerebro = bt.Cerebro()
    data = bt.feeds.YahooFinanceData(dataname=ticker, fromdate=start_date, todate=end_date)
    cerebro.adddata(data)
    cerebro.addstrategy(MeanReversion)
    cerebro.run()

    # Plot the strategy using the Bokeh plot
    bokeh_plot.plot(cerebro)

if __name__ == '__main__':
    main()
