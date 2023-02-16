import streamlit as st
from backtrader_plotting import Bokeh

# Import your Backtrader strategy
from my_strategy import MyStrategy

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
    bokeh_plot = Bokeh(style='bar', plot_mode='single')

    # Run the strategy with the given settings
    cerebro = bt.Cerebro()
    data = bt.feeds.YahooFinanceData(dataname=ticker, fromdate=start_date, todate=end_date)
    cerebro.adddata(data)
    cerebro.addstrategy(MyStrategy)
    cerebro.run()

    # Plot the strategy using the Bokeh plot
    bokeh_plot.plot(cerebro)

if __name__ == '__main__':
    main()
